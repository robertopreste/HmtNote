#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from hmtnote.classes import Annotator


def annotate_vcf(input_vcf: str, output_vcf: str,
                 basic: bool = False,
                 variab: bool = False,
                 predict: bool = False):
    """
    Annotate a VCF file using information from HmtVar.

    If neither --basic, --variab nor --predict are provided, they will all default to True, and
    the VCF will be annotated using all the available information.
    :param str input_vcf: input VCF file to annotate
    :param str output_vcf: file where the annotated VCF will be saved
    :param bool basic: annotate VCF using basic information (locus, pathogenicity, Clinvar and dbSNP
    IDs, etc.) (default: False)
    :param bool variab: annotate VCF using variability information (nucleotide and aminoacid
    variability, allele frequencies) (default: False)
    :param bool predict: annotate VCF using predictions information (from MutPred, Panther,
    Polyphen and other resources) (default: False)
    :return:
    """
    if not basic and not variab and not predict:
        basic, variab, predict = True, True, True

    vcf = Annotator(input_vcf, output_vcf, basic, variab, predict)
    vcf.annotate()

    return

