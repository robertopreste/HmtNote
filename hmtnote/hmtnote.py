#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import argparse
import sys
from hmtnote.classes import Annotator, check_connection


def annotate_vcf(input_vcf: str, output_vcf: str,
                 basic: bool = False,
                 crossref: bool = False,
                 variab: bool = False,
                 predict: bool = False):
    """
    Annotate a VCF file using information from HmtVar.

    If neither --basic, --crossref, --variab nor --predict are provided, they
    will all default to True, and the VCF will be annotated using all the
    available information.
    :param str input_vcf: input VCF file to annotate
    :param str output_vcf: file where the annotated VCF will be saved
    :param bool basic: annotate VCF using basic information (locus,
    pathogenicity, etc.) (default: False)
    :param bool crossref: annotate VCF using cross-reference information
    (Clinvar and dbSNP IDs, etc.) (default: False)
    :param bool variab: annotate VCF using variability information (nucleotide
    and aminoacid variability, allele frequencies) (default: False)
    :param bool predict: annotate VCF using predictions information (from
    MutPred, Panther, Polyphen and other resources) (default: False)
    :return:
    """
    if not basic and not crossref and not variab and not predict:
        basic, crossref, variab, predict = True, True, True, True

    if check_connection():
        vcf = Annotator(input_vcf, output_vcf, basic, crossref, variab, predict)
        vcf.annotate()
    else:
        print("No internet connection available!")
        print("Exiting.")
        sys.exit(1)

    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Annotate a VCF file using 
    information from HmtVar. If neither --basic, --crossref, --variab nor 
    --predict are provided, they will all default to True, and the VCF will be 
    annotated using all the available information. """)
    parser.add_argument("input_vcf", type=str,
                        help="""Input VCF file to annotate.""")
    parser.add_argument("output_vcf", type=str,
                        help="""File where the annotated VCF will be saved.""")
    parser.add_argument("-b", "--basic", action="store_true",
                        dest="annot_basic",
                        help="""Annotate VCF using basic information (locus, 
                        pathogenicity, etc.) (default: False)""")
    parser.add_argument("-c", "--crossref", action="store_true",
                        dest="annot_crossref",
                        help="""Annotate VCF using cross-reference information 
                        (Clinvar and dbSNP IDs, etc.) (default: False)""")
    parser.add_argument("-v", "--variab", action="store_true",
                        dest="annot_variab",
                        help="""Annotate VCF using variability information 
                        (nucleotide and aminoacid variability, allele 
                        frequencies) (default: False)""")
    parser.add_argument("-p", "--predict", action="store_true",
                        dest="annot_predict",
                        help="""Annotate VCF using predictions information 
                        (from MutPred, Panther, Polyphen and other resources) 
                        (default: False)""")

    args = parser.parse_args()

    annotate_vcf(args.input_vcf, args.output_vcf,
                 args.annot_basic, args.annot_crossref,
                 args.annot_variab, args.annot_predict)
