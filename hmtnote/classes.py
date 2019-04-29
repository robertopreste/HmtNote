#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import json
import requests
import click
import asyncio
import aiohttp
import aiofiles
import os
import pandas as pd
from typing import Union
import vcfpy


class _HmtVarField:
    """
    This class is used to collect data from HmtVar's API for each field
    returned.
    self.element: name of the field to be used in the VCF file
    self.api_slug: name of the field used in HmtVar's API
    self._field_value: value of the given field; automatically instantiated as
    an empty list, is then populated with a single value for each alternate
    allele found in the variant
    """

    def __init__(self, element, api_slug):
        self.element = element
        self.api_slug = api_slug
        self._field_value = []

    @staticmethod
    def _replace_null(element: Union[str, int, float, None]) -> Union[str, int,
                                                                      float]:
        """
        Replace null values returned by HmtVar's API (None) with a '.'
        character.
        :param Union[str, int, float, None] element: value returned by HmtVar
        :return: Union[str, int, float]
        """
        if element is None:
            return "."
        return element

    @property
    def field_value(self):
        """
        List of values parsed from HmtVar's API for each alternate allele of
        the given variant.
        :return:
        """
        return self._field_value

    @field_value.setter
    def field_value(self, value):
        """
        Update the list of values with a new value.
        :param value: new value to be appended to the list of values
        :return:
        """
        self._field_value.append(self._replace_null(value))


class _HmtVarHeader:
    """
    This class is used to create a new header that will be added to the
    annotated VCF file.
    self.element: name of the field to be used in the VCF file
    self.vcf_number: value used in the 'number' attribute of the header line
    self.vcf_type: type of value for this information
    self.vcf_description: description of this information
    """

    def __init__(self, element, vcf_number, vcf_type, vcf_description):
        self.element = element
        self.vcf_number = vcf_number
        self.vcf_type = vcf_type
        self.vcf_description = vcf_description


class _HmtVarVariant:
    """
    This class is used to store a given variant and retrieve the related
    information from HmtVar.
    self.reference: reference allele of the variant
    self.position: position of the variant
    self.alternate: alternate allele of the variant
    self.variant: string-formatted variant, used for the API call
    """

    def __init__(self, reference, position, alternate):
        self.reference = reference
        self.position = position
        self.alternate = alternate
        self._variant = "{}{}".format(self.position, self.alternate.value)

    def _is_deletion(self) -> bool:
        """
        Check whether the current variant refers to a deletion.
        :return: bool
        """
        # e.g. ref CTG | alt C
        return self.alternate.type == "DEL"

    def _is_insertion(self) -> bool:
        """
        Check whether the current variant refers to an insertion.
        :return: bool
        """
        # e.g. ref C | alt CTG
        return self.alternate.type == "INS"

    @property
    def variant(self) -> str:
        """
        Create the proper variant format for deletions, insertions and SNPs.
        :return: str
        """
        if self._is_deletion():
            self._variant = "{}d".format(int(self.position) + 1)
        elif self._is_insertion():
            self._variant = "{}.{}".format(self.position,
                                           self.alternate.value[len(self.reference):])
        else:
            self._variant = "{}{}".format(self.position, self.alternate.value)

        return self._variant

    @property
    def response(self) -> dict:
        """
        Call HmtVar's API to retrieve data related to self.variant.
        :return: dict
        """
        url = "https://www.hmtvar.uniba.it/api/main/mutation/{}".format(self.variant)
        call = requests.get(url)
        # TODO variants not present in HmtVar actually return an empty dictionary
        resp = call.json()
        if resp == {}:
            # TODO: fix this, it's quite ugly
            resp = {"CrossRef": {"none": "."},
                    "Variab": {"none": "."},
                    "Predict": {"none": "."}}
        return resp


class _OfflineHmtVarVariant(_HmtVarVariant):
    def __init__(self, reference, position, alternate, database):
        super().__init__(reference, position, alternate)
        self.db = database

    def dbcall(self) -> pd.DataFrame:
        """
        Create the proper database query for deletions, insertions and SNPs.
        :return: pd.DataFrame
        """
        if super()._is_deletion():
            return self.db[(self.db["nt_start"] == (int(self.position) + 1)) &
                           (self.db["alt"] == "d")]
        elif super()._is_insertion():
            return self.db[(self.db["nt_start"] == self.position) &
                           (self.db["alt"] == ".{}".format(
                               self.alternate.value[len(self.reference):]
                           ))]
        else:
            return self.db[(self.db["nt_start"] == self.position) &
                           (self.db["alt"] == self.alternate.value)]

    @property
    def response(self) -> dict:
        """
        Overrides the _HmtVarVariant.response() method to retrieve the data
        from local dumped databases, instead of using HmtVar's API.
        :return: dict
        """
        call = self.dbcall()
        resp = call.to_dict(orient="records")
        if not resp:
            resp = [{"CrossRef": {"none": "."},
                     "Variab": {"none": "."},
                     "Predict": {"none": "."}}]

        return resp[0]


class _HmtVarParser:
    """
    This class is used to parse information collected from HmtVar's API and
    store them in the right format, ready for VCF annotation.
    self.record: variant record as returned by cyvcf2.VCF
    self.basics: basic information from HmtVar
    self.crossrefs: cross-reference information from HmtVar
    self.variabs: variability information from HmtVar
    self.predicts: predictions information from HmtVar
    """

    def __init__(self, record):
        self.record = record
        self.basics = (
            _HmtVarField("Locus", "locus"),
            _HmtVarField("AaChange", "aa_change"),
            _HmtVarField("Pathogenicity", "pathogenicity"),
            _HmtVarField("DiseaseScore", "disease_score"),
            _HmtVarField("HmtVar", "id")
            # _HmtVarField("Haplogroups", "haplogroups")
        )
        self.crossrefs = (
            _HmtVarField("Clinvar", "clinvar"),
            _HmtVarField("dbSNP", "dbSNP"),
            _HmtVarField("OMIM", "omim"),
            _HmtVarField("MitomapAssociatedDiseases",
                         "mitomap_associated_disease"),
            _HmtVarField("MitomapSomaticMutations",
                         "somatic_mutations")
        )
        self.variabs = (
            _HmtVarField("NtVarH", "nt_var"),
            _HmtVarField("NtVarP", "nt_var_patients"),
            _HmtVarField("AaVarH", "aa_var"),
            _HmtVarField("AaVarP", "aa_var_patients"),
            _HmtVarField("AlleleFreqH", "all_freq_h"),
            _HmtVarField("AlleleFreqP", "all_freq_p"),
            _HmtVarField("AlleleFreqH_AF", "all_freq_h_AF"),
            _HmtVarField("AlleleFreqP_AF", "all_freq_p_AF"),
            _HmtVarField("AlleleFreqH_AM", "all_freq_h_AM"),
            _HmtVarField("AlleleFreqP_AM", "all_freq_p_AM"),
            _HmtVarField("AlleleFreqH_AS", "all_freq_h_AS"),
            _HmtVarField("AlleleFreqP_AS", "all_freq_p_AS"),
            _HmtVarField("AlleleFreqH_EU", "all_freq_h_EU"),
            _HmtVarField("AlleleFreqP_EU", "all_freq_p_EU"),
            _HmtVarField("AlleleFreqH_OC", "all_freq_h_OC"),
            _HmtVarField("AlleleFreqP_OC", "all_freq_p_OC")
        )
        self.predicts = (
            _HmtVarField("MutPred_Prediction", "mutPred_pred"),
            _HmtVarField("MutPred_Probability", "mutPred_prob"),
            _HmtVarField("Panther_Prediction", "panther_pred"),
            _HmtVarField("Panther_Probability", "panther_prob"),
            _HmtVarField("PhDSNP_Prediction", "phD_snp_pred"),
            _HmtVarField("PhDSNP_Probability", "phD_snp_prob"),
            _HmtVarField("SNPsGO_Prediction", "snp_go_pred"),
            _HmtVarField("SNPsGO_Probability", "snp_go_prob"),
            _HmtVarField("Polyphen2HumDiv_Prediction",
                         "polyphen2_humDiv_pred"),
            _HmtVarField("Polyphen2HumDiv_Probability",
                         "polyphen2_humDiv_prob"),
            _HmtVarField("Polyphen2HumVar_Prediction",
                         "polyphen2_humVar_pred"),
            _HmtVarField("Polyphen2HumVar_Probability",
                         "polyphen2_humVar_prob")
        )

    def parse(self):
        """
        Update annotations about the given record.
        :return:
        """
        variants = [_HmtVarVariant(self.record.REF, self.record.POS, alt)
                    for alt in self.record.ALT]

        for variant in variants:
            response = variant.response
            for field in self.basics:
                field.field_value = response.get(field.api_slug,
                                                 ".")
            for field in self.crossrefs:
                field.field_value = response.get("CrossRef").get(field.api_slug,
                                                                 ".")
            for field in self.variabs:
                field.field_value = response.get("Variab").get(field.api_slug,
                                                               ".")
            for field in self.predicts:
                field.field_value = response.get("Predict").get(field.api_slug,
                                                                ".")


class _OfflineHmtVarParser(_HmtVarParser):
    def __init__(self, record, database):
        super().__init__(record)
        self.db = database

    def parse(self):
        """
        Overwrites the _HmtVarParser.parse() method for offline annotation.
        :return:
        """
        variants = [_OfflineHmtVarVariant(self.record.REF, self.record.POS,
                                          alt, self.db)
                    for alt in self.record.ALT]

        for variant in variants:
            response = variant.response
            for field in self.basics:
                field.field_value = response.get(field.api_slug,
                                                 ".")
            for field in self.crossrefs:
                field.field_value = response.get("CrossRef").get(field.api_slug,
                                                                 ".")
            for field in self.variabs:
                field.field_value = response.get("Variab").get(field.api_slug,
                                                               ".")
            for field in self.predicts:
                field.field_value = response.get("Predict").get(field.api_slug,
                                                                ".")


class Annotator:
    """
    Main entry point for VCF annotation.

    This class is the main entry point for VCF annotation. It will
    traverse a given input VCF and annotate each variant found, then save
    the annotated VCF.
    self.vcf_in: input VCF filename
    self.vcf_out: output VCF filename
    self.basic: bool flag to enable annotation of basic information
    self.crossref bool flag to enable annotation of cross-reference information
    self.variab: bool flag to enable annotation of variability information
    self.predict: bool flag to enable annotation of predictions information
    self.reader: input VCF reader (provided by cyvcf2.VCF)
    self.basic_heads: header to be used for basic information
    self.crossref_heads: header to be used for cross-reference information
    self.variab_heads: header to be used for variability information
    self.predict_heads: header to be used for predictions information
    self.writer: output VCF writer (provided by cyvcf2.Writer), instantiated
    after the header has been updated according to new header to be used
    """

    def __init__(self, vcf_in, vcf_out, basic, crossref, variab, predict):
        self.vcf_in = vcf_in
        self.vcf_out = vcf_out
        self.basic = basic
        self.crossref = crossref
        self.variab = variab
        self.predict = predict
        self.reader = vcfpy.Reader.from_path(vcf_in)
        self.basic_heads = (
            _HmtVarHeader("Locus", "A", "String",
                          "Locus to which the variant belongs"),
            _HmtVarHeader("AaChange", "A", "String",
                          "Aminoacidic change determined"),
            _HmtVarHeader("Pathogenicity", "A", "String",
                          "Pathogenicity predicted by HmtVar"),
            _HmtVarHeader("DiseaseScore", "A", "String",
                          "Disease score calculated by HmtVar"),
            _HmtVarHeader("HmtVar", "A", "String",
                          "HmtVar ID of the variant (can be used to view the related VariantCard on https://www.hmtvar.uniba.it/varCard/<HmtVarID>)")
            # _HmtVarHeader("Haplogroups", "A", "String",
            #              "Haplogroups defined by the variant")
        )
        self.crossref_heads = (
            _HmtVarHeader("Clinvar", "A", "String",
                          "Clinvar ID of the variant"),
            _HmtVarHeader("dbSNP", "A", "String",
                          "dbSNP ID of the variant"),
            _HmtVarHeader("OMIM", "A", "String",
                          "OMIM ID of the variant"),
            _HmtVarHeader("MitomapAssociatedDiseases", "A", "String",
                          "Diseases associated to the variant according to Mitomap"),
            _HmtVarHeader("MitomapSomaticMutations", "A", "String",
                          "Diseases associated to the variant according to Mitomap Somatic Mutations")
        )
        self.variab_heads = (
            _HmtVarHeader("NtVarH", "A", "String",
                          "Nucleotide variability of the position in healthy individuals"),
            _HmtVarHeader("NtVarP", "A", "String",
                          "Nucleotide variability of the position in patient individuals"),
            _HmtVarHeader("AaVarH", "A", "String",
                          "Aminoacid variability of the position in healthy individuals"),
            _HmtVarHeader("AaVarP", "A", "String",
                          "Aminoacid variability of the position in patient individuals"),
            _HmtVarHeader("AlleleFreqH", "A", "String",
                          "Allele frequency of the variant in healthy individuals overall"),
            _HmtVarHeader("AlleleFreqP", "A", "String",
                          "Allele frequency of the variant in patient individuals overall"),
            _HmtVarHeader("AlleleFreqH_AF", "A", "String",
                          "Allele frequency of the variant in healthy individuals from Africa"),
            _HmtVarHeader("AlleleFreqP_AF", "A", "String",
                          "Allele frequency of the variant in patient individuals from Africa"),
            _HmtVarHeader("AlleleFreqH_AM", "A", "String",
                          "Allele frequency of the variant in healthy individuals from America"),
            _HmtVarHeader("AlleleFreqP_AM", "A", "String",
                          "Allele frequency of the variant in patient individuals from America"),
            _HmtVarHeader("AlleleFreqH_AS", "A", "String",
                          "Allele frequency of the variant in healthy individuals from Asia"),
            _HmtVarHeader("AlleleFreqP_AS", "A", "String",
                          "Allele frequency of the variant in patient individuals from Asia"),
            _HmtVarHeader("AlleleFreqH_EU", "A", "String",
                          "Allele frequency of the variant in healthy individuals from Europe"),
            _HmtVarHeader("AlleleFreqP_EU", "A", "String",
                          "Allele frequency of the variant in patient individuals from Europe"),
            _HmtVarHeader("AlleleFreqH_OC", "A", "String",
                          "Allele frequency of the variant in healthy individuals from Oceania"),
            _HmtVarHeader("AlleleFreqP_OC", "A", "String",
                          "Allele frequency of the variant in patient individuals from Oceania")
        )
        self.predict_heads = (
            _HmtVarHeader("MutPred_Prediction", "A", "String",
                          "Pathogenicity prediction offered by MutPred"),
            _HmtVarHeader("MutPred_Probability", "A", "String",
                          "Confidence of the pathogenicity prediction offered by MutPred"),
            _HmtVarHeader("Panther_Prediction", "A", "String",
                          "Pathogenicity prediction offered by Panther"),
            _HmtVarHeader("Panther_Probability", "A", "String",
                          "Confidence of the pathogenicity prediction offered by Panther"),
            _HmtVarHeader("PhDSNP_Prediction", "A", "String",
                          "Pathogenicity prediction offered by PhD SNP"),
            _HmtVarHeader("PhDSNP_Probability", "A", "String",
                          "Confidence of the pathogenicity prediction offered by PhD SNP"),
            _HmtVarHeader("SNPsGO_Prediction", "A", "String",
                          "Pathogenicity prediction offered by SNPs & GO"),
            _HmtVarHeader("SNPsGO_Probability", "A", "String",
                          "Confidence of the pathogenicity prediction offered by SNPs & GO"),
            _HmtVarHeader("Polyphen2HumDiv_Prediction", "A", "String",
                          "Pathogenicity prediction offered by Polyphen2 HumDiv"),
            _HmtVarHeader("Polyphen2HumDiv_Probability", "A", "String",
                          "Confidence of the pathogenicity prediction offered by Polyphen2 HumDiv"),
            _HmtVarHeader("Polyphen2HumVar_Prediction", "A", "String",
                          "Pathogenicity prediction offered by Polyphen2 HumVar"),
            _HmtVarHeader("Polyphen2HumVar_Probability", "A", "String",
                          "Confidence of the pathogenicity prediction offered by Polyphen2 HumVar")
        )
        self._update_header()
        self.writer = vcfpy.Writer.from_path(vcf_out, self.reader.header)

    @staticmethod
    def _is_variation(record) -> bool:
        """
        Check whether or not the current record refers to an actual variant.
        :param record: current VCF record
        :return: bool
        """
        return len(record.ALT) > 0 and all([rec["value"] != "."
                                            for rec in record])

    @staticmethod
    def _is_mitochondrial(record) -> bool:
        """
        Check whether or not the current record is a mitochondrial variant; if
        not will avoid sending useless requests to HmtVar.
        :param record: current VCF record
        :return: bool
        """
        return record.CHROM in ["M", "MT", "chrM", "chrMT", "chrRCRS"]

    def _update_header(self):
        """
        Update the header present in the input VCF file according to the flags
        provided (basic, variability, predictions information).
        :return:
        """
        if self.basic:
            for field in self.basic_heads:
                self.reader.header.add_info_line(
                    vcfpy.OrderedDict([
                        ("ID", field.element),
                        ("Number", field.vcf_number),
                        ("Type", field.vcf_type),
                        ("Description", field.vcf_description)
                    ])
                )
        if self.crossref:
            for field in self.crossref_heads:
                self.reader.header.add_info_line(
                    vcfpy.OrderedDict([
                        ("ID", field.element),
                        ("Number", field.vcf_number),
                        ("Type", field.vcf_type),
                        ("Description", field.vcf_description)
                    ])
                )
        if self.variab:
            for field in self.variab_heads:
                self.reader.header.add_info_line(
                    vcfpy.OrderedDict([
                        ("ID", field.element),
                        ("Number", field.vcf_number),
                        ("Type", field.vcf_type),
                        ("Description", field.vcf_description)
                    ])
                )
        if self.predict:
            for field in self.predict_heads:
                self.reader.header.add_info_line(
                    vcfpy.OrderedDict([
                        ("ID", field.element),
                        ("Number", field.vcf_number),
                        ("Type", field.vcf_type),
                        ("Description", field.vcf_description)
                    ])
                )

    def annotate(self):
        """
        Annotate VCF variants.

        Annotate variants according to the flags provided (basic,
        variability, predictions information), and write the output VCF
        file.
        :return:
        """
        for record in self.reader:

            if self._is_variation(record) and self._is_mitochondrial(record):
                annots = _HmtVarParser(record)
                annots.parse()

                if self.basic:
                    for field in annots.basics:
                        record.INFO[field.element] = field.field_value
                if self.crossref:
                    for field in annots.crossrefs:
                        record.INFO[field.element] = field.field_value
                if self.variab:
                    for field in annots.variabs:
                        record.INFO[field.element] = field.field_value
                if self.predict:
                    for field in annots.predicts:
                        record.INFO[field.element] = field.field_value
            self.writer.write_record(record)

        self.reader.close()
        self.writer.close()


class DataDumper:
    """
    Download and store locally the required data from HmtVar.

    This class takes care of downloading the annotation database from
    HmtVar using the specific API for HmtNote, and will store the results
    in hmtnote_dump.pkl.
    self._df_basic: temporary dataframe with basic annotations
    self._df_crossref temporary dataframe with cross-reference annotations
    self._df_variab: temporary dataframe with variability annotations
    self._df_predict: temporary dataframe with prediction annotations
    """

    def __init__(self):
        self._df_basic = None
        self._df_crossref = None
        self._df_variab = None
        self._df_predict = None

    @staticmethod
    async def _download_json(session,
                             url: str,
                             dataset: str):
        """
        Async coroutine to download and save an annotation dataset.

        Will download the given dataset in chunks and write them to a
        JSON-formatted temporary file.
        :param session: aiohttp.ClientSession() to use
        :param str url: base url of HmtVar's API
        :param str dataset: annotation dataset name
        :return:
        """
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        async with session.get(url, ssl=False) as res:
            filename = "dump_{}.json".format(dataset)
            async with aiofiles.open(os.path.join(BASE_DIR, filename), "wb") as f:
                while True:
                    chunk = await res.content.read(1024)
                    if not chunk:
                        break
                    await f.write(chunk)
            click.echo("...{} annotations ready.".format(dataset))
            return await res.release()

    @staticmethod
    async def _looper_download_json(dataset: str):
        """
        Main async function to download and save annotation datasets.
        :param str dataset: annotation dataset name
        :return:
        """
        url = "https://www.hmtvar.uniba.it/hmtnote/{}".format(dataset)
        click.echo("Downloading {} annotations...".format(dataset))
        async with aiohttp.ClientSession() as session:
            await DataDumper._download_json(session, url, dataset)

    def download_data(self):
        """
        Download the annotations and build the local annotation database.

        Call the `_looper_download_json()` function to download the data
        and store them in a single pickled dataframe for later use.
        :return:
        """
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        datasets = ["basic", "crossref", "variab", "predict"]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            asyncio.gather(
                *(self._looper_download_json(dataset) for dataset in datasets)
            )
        )

        click.echo("Building local database... ", nl=False)
        self._df_basic = pd.read_json(
            os.path.join(BASE_DIR, "dump_basic.json"), precise_float=True)
        self._df_crossref = pd.read_json(
            os.path.join(BASE_DIR, "dump_crossref.json"), precise_float=True)
        self._df_variab = pd.read_json(
            os.path.join(BASE_DIR, "dump_variab.json"), precise_float=True)
        self._df_predict = pd.read_json(
            os.path.join(BASE_DIR, "dump_predict.json"), precise_float=True)

        self._df_crossref.drop(["aa_change", "alt", "disease_score", "locus",
                                "nt_start", "pathogenicity", "ref_rCRS"],
                               axis=1, inplace=True)
        self._df_variab.drop(["aa_change", "alt", "disease_score", "locus",
                              "nt_start", "pathogenicity", "ref_rCRS"],
                             axis=1, inplace=True)
        self._df_predict.drop(["aa_change", "alt", "disease_score", "locus",
                               "nt_start", "pathogenicity", "ref_rCRS"],
                              axis=1, inplace=True)

        final_df = (self._df_basic.set_index("id")
                    .join(self._df_crossref.set_index("id"))
                    .join(self._df_variab.set_index("id"))
                    .join(self._df_predict.set_index("id"))).reset_index()
        final_df.fillna(".", inplace=True)
        final_df.to_pickle(os.path.join(BASE_DIR, "hmtnote_dump.pkl"))
        click.echo("Done.")

        click.echo("Removing temporary files... ", nl=False)
        os.remove(os.path.join(BASE_DIR, "dump_basic.json"))
        os.remove(os.path.join(BASE_DIR, "dump_crossref.json"))
        os.remove(os.path.join(BASE_DIR, "dump_variab.json"))
        os.remove(os.path.join(BASE_DIR, "dump_predict.json"))
        click.echo("Done.")
        click.echo("Local HmtNote database saved to hmtnote_dump.pkl for offline use.")


class OfflineAnnotator(Annotator):
    """
        Main entry point for offline VCF annotation.

        This class is the main entry point for offline VCF annotation. It
        will traverse a given input VCF and annotate each variant found,
        then save the annotated VCF.
        self.vcf_in: input VCF filename
        self.vcf_out: output VCF filename
        self.basic: bool flag to enable annotation of basic information
        self.crossref bool flag to enable annotation of cross-reference information
        self.variab: bool flag to enable annotation of variability information
        self.predict: bool flag to enable annotation of predictions information
        self.reader: input VCF reader (provided by cyvcf2.VCF)
        self.basic_heads: header to be used for basic information
        self.crossref_heads: header to be used for cross-reference information
        self.variab_heads: header to be used for variability information
        self.predict_heads: header to be used for predictions information
        self.writer: output VCF writer (provided by cyvcf2.Writer), instantiated
        after the header has been updated according to new header to be used
        self.db: local annotation database (hmtnote_dump.pkl)
        """

    def __init__(self, vcf_in, vcf_out, basic, crossref, variab, predict):
        super().__init__(vcf_in, vcf_out, basic, crossref, variab, predict)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.db = pd.read_pickle(os.path.join(BASE_DIR, "hmtnote_dump.pkl"))

    def annotate(self):
        """
        Annotate VCF variants.

        Override the Annotator.annotate() method to provide offline
        annotation according to the flags provided (basic, variability,
        predictions information), and write the output VCF file.
        :return:
        """
        for record in self.reader:

            if self._is_variation(record) and self._is_mitochondrial(record):
                annots = _OfflineHmtVarParser(record, self.db)
                annots.parse()

                if self.basic:
                    for field in annots.basics:
                        record.INFO[field.element] = field.field_value
                if self.crossref:
                    for field in annots.crossrefs:
                        record.INFO[field.element] = field.field_value
                if self.variab:
                    for field in annots.variabs:
                        record.INFO[field.element] = field.field_value
                if self.predict:
                    for field in annots.predicts:
                        record.INFO[field.element] = field.field_value
            self.writer.write_record(record)

        self.reader.close()
        self.writer.close()


def check_connection() -> bool:
    """
    Look for a functioning internet connection.
    :return: bool
    """

    url = "https://www.google.com"
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.exceptions.RequestException as e:
        pass
    return False


def check_dump() -> bool:
    """
    Check the presence of the local annotation database hmtnote_dump.pkl.
    :return: bool
    """

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    return os.path.isfile(os.path.join(BASE_DIR, "hmtnote_dump.pkl"))
