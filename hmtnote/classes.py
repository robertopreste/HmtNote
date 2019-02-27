#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import requests
from typing import Union
from vcf.model import _Record


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


class Annotator:
    def __init__(self, record):
        self.record = record

        self.basics = [("Locus", "locus", []), ("AaChange", "aa_change", []),
                  ("Pathogenicity", "pathogenicity", []), ("DiseaseScore", "disease_score", []),
                  ("Haplogroups", "haplogroups", [])]
        self.crossrefs = [("Clinvar", "clinvar", []), ("dbSNP", "dbSNP", []), ("OMIM", "omim", []),
                     ("MitomapAssociatedDiseases", "mitomap_associated_disease", []),
                     ("MitomapSomaticMutations", "somatic_mutations", [])]
        self.variabs = [("NtVarH", "nt_var", []), ("NtVarP", "nt_var_patients", []),
                   ("AaVarH", "aa_var", []), ("AaVarP", "aa_var_patients", []),
                   ("AlleleFreqH", "all_freq_h", []), ("AlleleFreqP", "all_freq_p", []),
                   ("AlleleFreqH_AF", "all_freq_h_AF", []), ("AlleleFreqP_AF", "all_freq_p_AF", []),
                   ("AlleleFreqH_AM", "all_freq_h_AM", []), ("AlleleFreqP_AM", "all_freq_p_AM", []),
                   ("AlleleFreqH_AS", "all_freq_h_AS", []), ("AlleleFreqP_AS", "all_freq_p_AS", []),
                   ("AlleleFreqH_EU", "all_freq_h_EU", []), ("AlleleFreqP_EU", "all_freq_p_EU", []),
                   ("AlleleFreqH_OC", "all_freq_h_OC", []), ("AlleleFreqP_OC", "all_freq_p_OC", [])]
        self.predicts = [("MutPred_Prediction", "mutPred_pred", []),
                    ("MutPred_Probability", "mutPred_prob", []),
                    ("Panther_Prediction", "panther_pred", []),
                    ("Panther_Probability", "panther_prob", []),
                    ("PhDSNP_Prediction", "phD_snp_pred", []),
                    ("PhDSNP_Probability", "phD_snp_prob", []),
                    ("SNPsGO_Prediction", "snp_go_pred", []),
                    ("SNPsGO_Probability", "snp_go_prob", []),
                    ("Polyphen2HumDiv_Prediction", "polyphen2_humDiv_pred", []),
                    ("Polyphen2HumDiv_Probability", "polyphen2_humDiv_prob", []),
                    ("Polyphen2HumVar_Prediction", "polyphen2_humVar_pred", []),
                    ("Polyphen2HumVar_Probability", "polyphen2_humVar_prob", [])]

    def is_variation(self) -> bool:
        """
        Check whether or not the current record refers to an actual variant.
        :return: bool
        """
        if self.record.ALT != [None]:
            return True
        return False

    def has_multiple_alts(self) -> bool:
        """
        Check whether or not the current record has multiple alternate alleles.
        :return: bool
        """
        if len(self.record.ALT) > 1:
            return True
        return False

    @staticmethod
    def replace_null(element: Union[str, int, float, None]) -> Union[str, int, float]:
        """
        Replace null values returned by HmtVar (None) with a '.' character.
        :param Union[str, int, float, None] element: value returned by HmtVar
        :return: Union[str, int, float]
        """
        if element is None:
            return "."
        return element

    def annotate_basic(self, response: dict):
        """
        Update self.basics and self.crossrefs using values found in the input variant's response.
        :param dict response: response returned by HmtVar's API
        :return:
        """
        for el in self.basics:
            el[2].append(self.replace_null(response.get(el[1], ".")))
        for el in self.crossrefs:
            el[2].append(self.replace_null(response.get("CrossRef").get(el[1], ".")))

    def annotate_variab(self, response: dict):
        """
        Update self.variabs using values found in the input variant's response.
        :param dict response: response returned by HmtVar's API.
        :return:
        """
        for el in self.variabs:
            el[2].append(self.replace_null(response.get("Variab").get(el[1], ".")))

    def annotate_predict(self, response: dict):
        """
        Update self.predicts using values found in the input variant's response.
        :param dict response: response returned by HmtVar's API.
        :return:
        """
        for el in self.predicts:
            el[2].append(self.replace_null(response.get("Predict").get(el[1], ".")))

    def annotate(self, basic: bool = True,
                 variab: bool = True,
                 predict: bool = True):
        """
        Update annotations about the given record using the above-defined functions.
        :param bool basic: update basic annotations
        :param bool variab: update variability annotations
        :param bool predict: update predictions annotations
        :return:
        """
        variants = [Variant(self.record.REF, self.record.POS, alt) for alt in self.record.ALT]
        for variant in variants:
            if basic:
                self.annotate_basic(variant.response)
            if variab:
                self.annotate_variab(variant.response)
            if predict:
                self.annotate_predict(variant.response)

    def update_record(self, basic: bool = True,
                      variab: bool = True,
                      predict: bool = True) -> _Record:
        """
        Add new updated annotations to the input record, which is then ready to be written out.
        If the record's ALT attribute contains more than one alternate allele, resulting values
        will be merged with a comma, as is common in VCF files.
        :param bool basic: update record with basic annotations
        :param bool variab: update record with variability annotations
        :param bool predict: update record with prediction annotations
        :return: _Record original record with added fields in the INFO column
        """
        if basic:
            for el in self.basics:
                self.record.add_info(el[0], ",".join(map(str, el[2])))
            for el in self.crossrefs:
                self.record.add_info(el[0], ",".join(map(str, el[2])))
        if variab:
            for el in self.variabs:
                self.record.add_info(el[0], ",".join(map(str, el[2])))
        if predict:
            for el in self.predicts:
                self.record.add_info(el[0], ",".join(map(str, el[2])))

        return self.record





