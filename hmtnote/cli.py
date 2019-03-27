#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys
import click
from hmtnote.classes import Annotator, OfflineAnnotator, DataDumper
from hmtnote.classes import check_connection, check_dump


@click.group()
@click.version_option()
def main():
    pass


@main.command()
@click.argument("input_vcf")
@click.argument("output_vcf")
@click.option("--basic", "-b", is_flag=True, default=False,
              help="""Annotate VCF using basic information (locus, pathogenicity, etc.) 
              (default: False)""")
@click.option("--crossref", "-c", is_flag=True, default=False,
              help="""Annotate VCF using cross-reference information (Clinvar and dbSNP IDs, etc.) 
              (default: False)""")
@click.option("--variab", "-v", is_flag=True, default=False,
              help="""Annotate VCF using variability information (nucleotide and aminoacid 
              variability, allele frequencies) (default: False)""")
@click.option("--predict", "-p", is_flag=True, default=False,
              help="""Annotate VCF using predictions information (from MutPred, Panther, Polyphen 
              and other resources) (default: False)""")
@click.option("--offline", "-o", is_flag=True, default=False,
              help="""Annotate VCF using previously downloaded databases (offline mode) 
              (default: False)""")
def annotate(input_vcf, output_vcf, basic, crossref, variab, predict, offline):
    """
    Annotate a VCF file using data from HmtVar.

    If neither --basic, --crossref, --variab nor --predict are
    provided, they will all default to True, and the VCF will be annotated
    using all the available information.
    If no internet connection is available, use the --offline option to use
    the local database for annotation (you must have previously downloaded it
    using the hmtnote dump command).
    """
    if not basic and not crossref and not variab and not predict:
        basic, crossref, variab, predict = True, True, True, True

    if offline:
        if not check_dump():
            click.echo("""Local annotation database hmtnote_dump.pkl not found.

            Please dump the annotation database first!""")
            return 1
        vcf = OfflineAnnotator(input_vcf, output_vcf,
                               basic, crossref, variab, predict)
    else:
        if check_connection():
            vcf = Annotator(input_vcf, output_vcf,
                            basic, crossref, variab, predict)
        else:
            # default to offline annotation if no connection available
            # or an error occurs
            click.echo("No connection available!")
            click.echo("Switching to offline annotation...")
            if not check_dump():
                click.echo("""Local annotation database hmtnote_dump.pkl not found.

                Please dump the annotation database first!""")
                return 1
            vcf = OfflineAnnotator(input_vcf, output_vcf,
                                   basic, crossref, variab, predict)
    vcf.annotate()

    return 0


@main.command()
def dump():
    """
    Download databases from HmtVar for offline annotation.
    """
    dumper = DataDumper()
    dumper.download_data()

    return 0


if __name__ == "__main__":
    sys.exit(main())
