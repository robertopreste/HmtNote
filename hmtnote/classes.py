#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import requests
from typing import Union
from vcf.model import _Record
from pysam import VariantFile


class HmtVarField:
    def __init__(self, element, api_slug):
        self.element = element
        self.api_slug = api_slug
        self._field_value = []

    @staticmethod
    def replace_null(element: Union[str, int, float, None]) -> Union[str, int, float]:
        """
        Replace null values returned by HmtVar's API (None) with a '.' character.
        :param Union[str, int, float, None] element: value returned by HmtVar
        :return: Union[str, int, float]
        """
        if element is None:
            return "."
        return element

    @property
    def field_value(self):
        return self._field_value

    @field_value.setter
    def field_value(self, value):
        self._field_value.append(self.replace_null(value))
        
        
class HmtVarHeader: 
    def __init__(self, element, vcf_number, vcf_type, vcf_description):
        self.element = element
        self.vcf_number = vcf_number
        self.vcf_type = vcf_type
        self.vcf_description = vcf_description


class Variant:
    def __init__(self, reference, position, alternate):
        self.reference = reference
        self.position = position
        self.alternate = alternate
        self.variant = f"{self.reference}{self.position}{self.alternate}"

    @property
    def response(self) -> dict:
        """
        Call HmtVar's API to retrieve data related to self.variant.
        :return: dict
        """
        url = f"https://www.hmtvar.uniba.it/api/main/mutation/{self.variant}"
        call = requests.get(url)
        # TODO variants not present in HmtVar actually return an empty dictionary
        resp = call.json()
        if resp == {}:
            resp = {"CrossRef": ".", "Variab": ".", "Predict": "."}
        return resp


class RecordAnnotator:
    def __init__(self, record):
        self.record = record
        self.basics = (
            HmtVarField("Locus", "locus"),
            HmtVarField("AaChange", "aa_change"),
            HmtVarField("Pathogenicity", "pathogenicity"),
            HmtVarField("Haplogroups", "haplogroups")
        )
        self.crossrefs = (
            HmtVarField("Clinvar", "clinvar"),
            HmtVarField("dbSNP", "dbSNP"),
            HmtVarField("OMIM", "omim"),
            HmtVarField("MitomapAssociatedDiseases", "mitomap_associated_disease"),
            HmtVarField("MitomapSomaticMutations", "mitomap_somatic_mutations")
        )
        self.variabs = (
            HmtVarField("NtVarH", "nt_var"),
            HmtVarField("NtVarP", "nt_var_patients"),
            HmtVarField("AaVarH", "aa_var"),
            HmtVarField("AaVarP", "aa_var_patients"),
            HmtVarField("AlleleFreqH", "all_freq_h"),
            HmtVarField("AlleleFreqP", "all_freq_p"),
            HmtVarField("AlleleFreqH_AF", "all_freq_h_AF"),
            HmtVarField("AlleleFreqP_AF", "all_freq_p_AF"),
            HmtVarField("AlleleFreqH_AM", "all_freq_h_AM"),
            HmtVarField("AlleleFreqP_AM", "all_freq_p_AM"),
            HmtVarField("AlleleFreqH_AS", "all_freq_h_AS"),
            HmtVarField("AlleleFreqP_AS", "all_freq_p_AS"),
            HmtVarField("AlleleFreqH_EU", "all_freq_h_EU"),
            HmtVarField("AlleleFreqP_EU", "all_freq_p_EU"),
            HmtVarField("AlleleFreqH_OC", "all_freq_h_OC"),
            HmtVarField("AlleleFreqP_OC", "all_freq_p_OC")
        )
        self.predicts = (
            HmtVarField("MutPred_Prediction", "mutPred_pred"),
            HmtVarField("MutPred_Probability", "mutPred_prob"),
            HmtVarField("Panther_Prediction", "panther_pred"),
            HmtVarField("Panther_Probability", "panther_prob"),
            HmtVarField("PhDSNP_Prediction", "phD_snp_pred"),
            HmtVarField("PhDSNP_Probability", "phD_snp_prob"),
            HmtVarField("SNPsGO_Prediction", "snp_go_pred"),
            HmtVarField("SNPsGO_Probability", "snp_go_prob"),
            HmtVarField("Polyphen2HumDiv_Prediction", "polyphen2_humDiv_pred"),
            HmtVarField("Polyphen2HumDiv_Probability", "polyphen2_humDiv_prob"),
            HmtVarField("Polyphen2HumVar_Prediction", "polyphen2_humVar_pred"),
            HmtVarField("Polyphen2HumVar_Probability", "polyphen2_humVar_prob")
        )

    def is_variation(self) -> bool:
        """
        Check whether or not the current record refers to an actual variant.
        :return: bool
        """
        if self.record.alts is not None:
            return True
        return False

    def has_multiple_alts(self) -> bool:
        """
        Check whether or not the current record has multiple alternate alleles.
        :return: bool
        """
        if len(self.record.alts) > 1:
            return True
        return False

    def parse_annotations(self):
        """
        Update annotations about the given record using the above-defined functions.
        :return:
        """
        variants = [Variant(self.record.ref, self.record.pos, alt) for alt in self.record.alts]
        for variant in variants:
            response = variant.response
            for field in self.basics:
                field.field_value = response.get(field.api_slug, ".")
            for field in self.crossrefs:
                field.field_value = response.get("CrossRef").get(field.api_slug, ".")
            for field in self.variabs:
                field.field_value = response.get("Variab").get(field.api_slug, ".")
            for field in self.predicts:
                field.field_value = response.get("Predict").get(field.api_slug, ".")

    def annotate(self, basic: bool = True, variab: bool = True, predict: bool = True):
        """
        Add new updated annotations to the input record, which is then ready to be written out.
        :param bool basic: update record with basic annotations
        :param bool variab: update record with variability annotations
        :param bool predict: update record with prediction annotations
        :return:
        """
        if basic:
            for field in self.basics:
                self.record.info[field.element] = ",".join(map(str, field.field_value))
            for field in self.crossrefs:
                self.record.info[field.element] = ",".join(map(str, field.field_value))
        if variab:
            for field in self.variabs:
                self.record.info[field.element] = ",".join(map(str, field.field_value))
        if predict:
            for field in self.predicts:
                self.record.info[field.element] = ",".join(map(str, field.field_value))

        return self.record


class Updater:
    # TODO: this will embrace the RecordAnnotator class, so I can reference the straight record
    def __init__(self, vcf_in, vcf_out, basic, variab, predict):
        self.vcf_in = vcf_in
        self.vcf_out = vcf_out
        self.basic = basic
        self.variab = variab
        self.predict = predict
        self.reader = VariantFile(vcf_in, "r")
        self.basics = (
            HmtVarHeader("Locus", "A", "String",
                         "Locus to which the variant belongs"),
            HmtVarHeader("AaChange", "A", "String",
                         "Aminoacidic change determined"),
            HmtVarHeader("Pathogenicity", "A", "String",
                         "Pathogenicity predicted by HmtVar"),
            HmtVarHeader("Haplogroups", "A", "String",
                         "Haplogroups defined by the variant")
        )
        self.crossrefs = (
            HmtVarHeader("Clinvar", "A", "String",
                         "Clinvar ID of the variant"),
            HmtVarHeader("dbSNP", "A", "String",
                         "dbSNP ID of the variant"),
            HmtVarHeader("OMIM", "A", "String",
                         "OMIM ID of the variant"),
            HmtVarHeader("MitomapAssociatedDiseases", "A", "String",
                         "Diseases associated to the variant according to Mitomap Associated Diseases"),
            HmtVarHeader("MitomapSomaticMutations", "A", "String",
                         "Diseases associated to the variant according to Mitomap Somatic Mutations")
        )
        self.variabs = (
            HmtVarHeader("NtVarH", "A", "String",
                         "Nucleotide variability of the position in healthy individuals"),
            HmtVarHeader("NtVarP", "A", "String",
                         "Nucleotide variability of the position in patient individuals"),
            HmtVarHeader("AaVarH", "A", "String",
                         "Aminoacid variability of the position in healthy individuals"),
            HmtVarHeader("AaVarP", "A", "String",
                         "Aminoacid variability of the position in patient individuals"),
            HmtVarHeader("AlleleFreqH", "A", "String",
                         "Allele frequency of the variant in healthy individuals overall"),
            HmtVarHeader("AlleleFreqP", "A", "String",
                         "Allele frequency of the variant in patient individuals overall"),
            HmtVarHeader("AlleleFreqH_AF", "A", "String",
                         "Allele frequency of the variant in healthy individuals from Africa"),
            HmtVarHeader("AlleleFreqP_AF", "A", "String",
                         "Allele frequency of the variant in patient individuals from Africa"),
            HmtVarHeader("AlleleFreqH_AM", "A", "String",
                         "Allele frequency of the variant in healthy individuals from America"),
            HmtVarHeader("AlleleFreqP_AM", "A", "String",
                         "Allele frequency of the variant in patient individuals from America"),
            HmtVarHeader("AlleleFreqH_AS", "A", "String",
                         "Allele frequency of the variant in healthy individuals from Asia"),
            HmtVarHeader("AlleleFreqP_AS", "A", "String",
                         "Allele frequency of the variant in patient individuals from Asia"),
            HmtVarHeader("AlleleFreqH_EU", "A", "String",
                         "Allele frequency of the variant in healthy individuals from Europe"),
            HmtVarHeader("AlleleFreqP_EU", "A", "String",
                         "Allele frequency of the variant in patient individuals from Europe"),
            HmtVarHeader("AlleleFreqH_OC", "A", "String",
                         "Allele frequency of the variant in healthy individuals from Oceania"),
            HmtVarHeader("AlleleFreqP_OC", "A", "String",
                         "Allele frequency of the variant in patient individuals from Oceania")
        )
        self.predicts = (
            HmtVarHeader("MutPred_Prediction", "A", "String",
                         "Pathogenicity prediction offered by MutPred"),
            HmtVarHeader("MutPred_Probability", "A", "String",
                         "Confidence of the pathogenicity prediction offered by MutPred"),
            HmtVarHeader("Panther_Prediction", "A", "String",
                         "Pathogenicity prediction offered by Panther"),
            HmtVarHeader("Panther_Probability", "A", "String",
                         "Confidence of the pathogenicity prediction offered by Panther"),
            HmtVarHeader("PhDSNP_Prediction", "A", "String",
                         "Pathogenicity prediction offered by PhD SNP"),
            HmtVarHeader("PhDSNP_Probability", "A", "String",
                         "Confidence of the pathogenicity prediction offered by PhD SNP"),
            HmtVarHeader("SNPsGO_Prediction", "A", "String",
                         "Pathogenicity prediction offered by SNPs & GO"),
            HmtVarHeader("SNPsGO_Probability", "A", "String",
                         "Confidence of the pathogenicity prediction offered by SNPs & GO"),
            HmtVarHeader("Polyphen2HumDiv_Prediction", "A", "String",
                         "Pathogenicity prediction offered by Polyphen2 HumDiv"),
            HmtVarHeader("Polyphen2HumDiv_Probability", "A", "String",
                         "Confidence of the pathogenicity prediction offered by Polyphen2 HumDiv"),
            HmtVarHeader("Polyphen2HumVar_Prediction", "A", "String",
                         "Pathogenicity prediction offered by Polyphen2 HumVar"),
            HmtVarHeader("Polyphen2HumVar_Probability", "A", "String",
                         "Confidence of the pathogenicity prediction offered by Polyphen2 HumVar")
        )
        self.update_header()
        self.writer = VariantFile(vcf_out, "w", header=self.reader.header)
        self.update_variants()

    def update_header(self):
        if self.basic:
            for field in self.basics:
                self.reader.header.info.add(field.element, field.vcf_number, field.vcf_type,
                                            field.vcf_description)
            for field in self.crossrefs:
                self.reader.header.info.add(field.element, field.vcf_number, field.vcf_type,
                                            field.vcf_description)
        if self.variab:
            for field in self.variabs:
                self.reader.header.info.add(field.element, field.vcf_number, field.vcf_type,
                                            field.vcf_description)
        if self.predict:
            for field in self.predicts:
                self.reader.header.info.add(field.element, field.vcf_number, field.vcf_type,
                                            field.vcf_description)

    def update_variants(self):
        for element in self.reader:
            # print(element)
            record = RecordAnnotator(element)
            # print(record.is_variation())
            if record.is_variation():
                record.parse_annotations()
                # print(record.info["Locus"])
                # print(record.basics)
                self.writer.write(record.annotate(self.basic, self.variab, self.predict))
        self.reader.close()
        self.writer.close()



