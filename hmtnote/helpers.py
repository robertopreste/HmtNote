#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste


class HmtVarValue:
    def __init__(self, element, api_slug, vcf_number, vcf_type, vcf_description):
        self.element = element
        self.api_slug = api_slug
        self.vcf_number = vcf_number
        self.vcf_type = vcf_type
        self.vcf_description = vcf_description


basics = (
    HmtVarValue("Locus", "locus", "A", "String",
                "Locus to which the variant belongs"),
    HmtVarValue("AaChange", "aa_change", "A", "String",
                "Aminoacidic change determined"),
    HmtVarValue("Pathogenicity", "pathogenicity", "A", "String",
                "Pathogenicity predicted by HmtVar"),
    HmtVarValue("Haplogroups", "haplogroups", "A", "String",
                "Haplogroups defined by the variant")
)

crossrefs = (
    HmtVarValue("Clinvar", "clinvar", "A", "String",
                "Clinvar ID of the variant"),
    HmtVarValue("dbSNP", "dbSNP", "A", "String",
                "dbSNP ID of the variant"),
    HmtVarValue("OMIM", "omim", "A", "String",
                "OMIM ID of the variant"),
    HmtVarValue("MitomapAssociatedDiseases", "mitomap_associated_disease" "A", "String",
                "Diseases associated to the variant according to Mitomap Associated Diseases"),
    HmtVarValue("MitomapSomaticMutations", "mitomap_somatic_mutations", "A", "String",
                "Diseases associated to the variant according to Mitomap Somatic Mutations")
)

variabs = (
    HmtVarValue("NtVarH", "nt_var", "A", "Float",
                "Nucleotide variability of the position in healthy individuals"),
    HmtVarValue("NtVarP", "nt_var_patients", "A", "Float",
                "Nucleotide variability of the position in patient individuals"),
    HmtVarValue("AaVarH", "aa_var", "A", "Float",
                "Aminoacid variability of the position in healthy individuals"),
    HmtVarValue("AaVarP", "aa_var_patients", "A", "Float",
                "Aminoacid variability of the position in patient individuals"),
    HmtVarValue("AlleleFreqH", "all_freq_h", "A", "Float",
                "Allele frequency of the variant in healthy individuals overall"),
    HmtVarValue("AlleleFreqP", "all_freq_p", "A", "Float",
                "Allele frequency of the variant in patient individuals overall"),
    HmtVarValue("AlleleFreqH_AF", "all_freq_h_AF", "A", "Float",
                "Allele frequency of the variant in healthy individuals from Africa"),
    HmtVarValue("AlleleFreqP_AF", "all_freq_p_AF", "A", "Float",
                "Allele frequency of the variant in patient individuals from Africa"),
    HmtVarValue("AlleleFreqH_AM", "all_freq_h_AM", "A", "Float",
                "Allele frequency of the variant in healthy individuals from America"),
    HmtVarValue("AlleleFreqP_AM", "all_freq_p_AM", "A", "Float",
                "Allele frequency of the variant in patient individuals from America"),
    HmtVarValue("AlleleFreqH_AS", "all_freq_h_AS", "A", "Float",
            "Allele frequency of the variant in healthy individuals from Asia"),
    HmtVarValue("AlleleFreqP_AS", "all_freq_p_AS", "A", "Float",
                "Allele frequency of the variant in patient individuals from Asia"),
    HmtVarValue("AlleleFreqH_EU", "all_freq_h_EU", "A", "Float",
            "Allele frequency of the variant in healthy individuals from Europe"),
    HmtVarValue("AlleleFreqP_EU", "all_freq_p_EU", "A", "Float",
                "Allele frequency of the variant in patient individuals from Europe"),
    HmtVarValue("AlleleFreqH_OC", "all_freq_h_OC", "A", "Float",
            "Allele frequency of the variant in healthy individuals from Oceania"),
    HmtVarValue("AlleleFreqP_OC", "all_freq_p_OC", "A", "Float",
                "Allele frequency of the variant in patient individuals from Oceania")
)

predicts = (
    HmtVarValue("MutPred_Prediction", "mutPred_pred", "A", "String",
                "Pathogenicity prediction offered by MutPred"),
    HmtVarValue("MutPred_Probability", "mutPred_prob", "A", "Float",
                "Confidence of the pathogenicity prediction offered by MutPred"),
    HmtVarValue("Panther_Prediction", "panther_pred", "A", "String",
                "Pathogenicity prediction offered by Panther"),
    HmtVarValue("Panther_Probability", "panther_prob", "A", "Float",
                "Confidence of the pathogenicity prediction offered by Panther"),
    HmtVarValue("PhDSNP_Prediction", "phD_snp_pred", "A", "String",
                "Pathogenicity prediction offered by PhD SNP"),
    HmtVarValue("PhDSNP_Probability", "phD_snp_prob", "A", "Float",
                "Confidence of the pathogenicity prediction offered by PhD SNP"),
    HmtVarValue("SNPsGO_Prediction", "snp_go_pred", "A", "String",
                "Pathogenicity prediction offered by SNPs & GO"),
    HmtVarValue("SNPsGO_Probability", "snp_go_prob", "A", "Float",
                "Confidence of the pathogenicity prediction offered by SNPs & GO"),
    HmtVarValue("Polyphen2HumDiv_Prediction", "polyphen2_humDiv_pred", "A", "String",
                "Pathogenicity prediction offered by Polyphen2 HumDiv"),
    HmtVarValue("Polyphen2HumDiv_Probability", "polyphen2_humDiv_prob", "A", "Float",
                "Confidence of the pathogenicity prediction offered by Polyphen2 HumDiv"),
    HmtVarValue("Polyphen2HumVar_Prediction", "polyphen2_humVar_pred", "A", "String",
            "Pathogenicity prediction offered by Polyphen2 HumVar"),
    HmtVarValue("Polyphen2HumVar_Probability", "polyphen2_humVar_prob", "A", "Float",
                "Confidence of the pathogenicity prediction offered by Polyphen2 HumVar")
)

