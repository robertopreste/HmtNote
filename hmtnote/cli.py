#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys
import click
from hmtnote.classes import Annotator


@click.command()
@click.argument("input_vcf")
@click.argument("output_vcf")
@click.option("--basic", "-b", is_flag=True, default=False,
              help="""Annotate VCF using basic information (locus, pathogenicity, Clinvar and dbSNP 
              IDs, etc.) (default: False)""")
@click.option("--variab", "-v", is_flag=True, default=False,
              help="""Annotate VCF using variability information (nucleotide and aminoacid 
              variability, allele frequencies) (default: False)""")
@click.option("--predict", "-p", is_flag=True, default=False,
              help="""Annotate VCF using predictions information (from MutPred, Panther, Polyphen 
              and other resources) (default: False)""")
@click.version_option()
def main(input_vcf, output_vcf, basic, variab, predict):
    """
    Annotate a VCF file using data from HmtVar.

    If neither --basic, --variab nor --predict are
    provided, they will all default to True, and the VCF will be annotated using all the available
    information.
    """

    if not basic and not variab and not predict:
        basic, variab, predict = True, True, True

    vcf = Annotator(input_vcf, output_vcf, basic, variab, predict)
    vcf.annotate()

    return 0


if __name__ == "__main__":
    sys.exit(main())
