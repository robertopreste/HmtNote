#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import argparse
from hmtnote.classes import Annotator, OfflineAnnotator, DataDumper, check_connection


def annotate_vcf(input_vcf: str, output_vcf: str,
                 basic: bool = False,
                 crossref: bool = False,
                 variab: bool = False,
                 predict: bool = False,
                 offline: bool = False):
    """
    Annotate a VCF file using information from HmtVar.

    If neither basic, crossref, variab nor predict are provided, they
    will all default to True, and the VCF will be annotated using all the
    available information.
    If no internet connection is available, use the offline option to use
    the local database for annotation (you must have previously downloaded it
    using the hmtnote dump command).
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
    :param bool offline: annotate VCF using previously downloaded databases (offline mode) (default: False)
    :return:
    """
    if not basic and not crossref and not variab and not predict:
        basic, crossref, variab, predict = True, True, True, True

    if offline:
        vcf = OfflineAnnotator(input_vcf, output_vcf,
                               basic, crossref, variab, predict)
    else:
        if check_connection():
            vcf = Annotator(input_vcf, output_vcf,
                            basic, crossref, variab, predict)
        else:
            # default to offline annotation if no connection available
            # or an error occurs
            print("No connection available!")
            print("Switching to offline annotation...")
            vcf = OfflineAnnotator(input_vcf, output_vcf,
                                   basic, crossref, variab, predict)
    vcf.annotate()

    return


def dump():
    """
    Download databases from HmtVar for offline annotation.
    :return:
    """
    dumper = DataDumper()
    dumper.download_data()

    return


if __name__ == '__main__':
    print("""Direct use of hmtnote.py is not allowed. 
    
    Please check the documentation for correct usage. """)
    # parser = argparse.ArgumentParser(description="""Annotate a VCF file using
    # information from HmtVar. If neither --basic, --crossref, --variab nor
    # --predict are provided, they will all default to True, and the VCF will be
    # annotated using all the available information. """)
    # parser.add_argument("input_vcf", type=str,
    #                     help="""Input VCF file to annotate.""")
    # parser.add_argument("output_vcf", type=str,
    #                     help="""File where the annotated VCF will be saved.""")
    # parser.add_argument("-b", "--basic", action="store_true",
    #                     dest="annot_basic",
    #                     help="""Annotate VCF using basic information (locus,
    #                     pathogenicity, etc.) (default: False)""")
    # parser.add_argument("-c", "--crossref", action="store_true",
    #                     dest="annot_crossref",
    #                     help="""Annotate VCF using cross-reference information
    #                     (Clinvar and dbSNP IDs, etc.) (default: False)""")
    # parser.add_argument("-v", "--variab", action="store_true",
    #                     dest="annot_variab",
    #                     help="""Annotate VCF using variability information
    #                     (nucleotide and aminoacid variability, allele
    #                     frequencies) (default: False)""")
    # parser.add_argument("-p", "--predict", action="store_true",
    #                     dest="annot_predict",
    #                     help="""Annotate VCF using predictions information
    #                     (from MutPred, Panther, Polyphen and other resources)
    #                     (default: False)""")
    #
    # args = parser.parse_args()
    #
    # annotate_vcf(args.input_vcf, args.output_vcf,
    #              args.annot_basic, args.annot_crossref,
    #              args.annot_variab, args.annot_predict)
