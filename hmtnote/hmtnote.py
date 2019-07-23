#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys
from .classes import Annotator, OfflineAnnotator, DataDumper, \
    check_connection, check_dump


def annotate(input_vcf: str, output_vcf: str,
             basic: bool = False,
             crossref: bool = False,
             variab: bool = False,
             predict: bool = False,
             offline: bool = False,
             csv: bool = False):
    """
    Annotate a VCF file using information from HmtVar.

    If neither ``basic``, ``crossref``, ``variab`` nor ``predict`` are
    provided, they will all default to True, and the VCF will be
    annotated using all the available information.
    If no internet connection is available, use the ``offline`` option to
    use the local database for annotation (you must have previously
    downloaded it using the ``hmtnote dump`` command).
    If ``csv`` is set to True, an additional annotated CSV file will be
    produced (along with the annotated VCF file) with the same base name
    and in the same path as the provided ``output_vcf`` argument.

    :param str input_vcf: input VCF file to annotate

    :param str output_vcf: file where the annotated VCF will be saved

    :param bool basic: annotate VCF using basic information (locus,
        pathogenicity, etc.) (default: False)

    :param bool crossref: annotate VCF using cross-reference information
        (Clinvar and dbSNP IDs, etc.) (default: False)

    :param bool variab: annotate VCF using variability information
        (nucleotide and aminoacid variability, allele frequencies)
        (default: False)

    :param bool predict: annotate VCF using predictions information (from
        MutPred, Panther, Polyphen and other resources) (default: False)

    :param bool offline: annotate VCF using previously downloaded
        databases (offline mode) (default: False)

    :param bool csv: produce an additional annotated CSV file
    (default: False)

    :return:
    """
    if not basic and not crossref and not variab and not predict:
        basic, crossref, variab, predict = True, True, True, True

    if offline:
        if not check_dump():
            print("""Local annotation database hmtnote_dump.pkl not found.
            
            Please dump the annotation database first!""")
            sys.exit(1)
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
            if not check_dump():
                print("""Local annotation database hmtnote_dump.pkl not found.

                Please dump the annotation database first!""")
                sys.exit(1)
            vcf = OfflineAnnotator(input_vcf, output_vcf,
                                   basic, crossref, variab, predict)
    vcf.annotate()
    if csv:
        vcf.to_csv()

    return


def dump():
    """
    Download databases from HmtVar for offline annotation.

    :return:
    """
    dumper = DataDumper()
    dumper.download_data()

    return
