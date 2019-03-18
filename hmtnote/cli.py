#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys
import click
from hmtnote.classes import Annotator, OfflineAnnotator
from .commands.dump import dump


# @click.group(invoke_without_command=True)
# @click.pass_context
# def main(ctx):
#     print(ctx.args)
#     if ctx.invoked_subcommand is None:
#         return annotate()


# @main.command()
@click.command()
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
              help="""Annotate VCF using previously downloaded database (offline mode) 
              (default: False)""")
@click.version_option()
# def annotate(input_vcf, output_vcf, basic, crossref, variab, predict, offline):
def main(input_vcf, output_vcf, basic, crossref, variab, predict, offline):
    """
    Annotate a VCF file using data from HmtVar.

    If neither --basic, --crossref, --variab nor --predict are
    provided, they will all default to True, and the VCF will be annotated
    using all the available information.
    """
    if not basic and not crossref and not variab and not predict:
        basic, crossref, variab, predict = True, True, True, True

    if offline:
        vcf = OfflineAnnotator(input_vcf, output_vcf,
                               basic, crossref, variab, predict)
        vcf.annotate()
    else:
        vcf = Annotator(input_vcf, output_vcf,
                        basic, crossref, variab, predict)
        vcf.annotate()

    return 0

# can be done with
# "https://stackoverflow.com/questions/52053491/a-command-without-name-in-click"
# main.add_command(dump)


if __name__ == "__main__":
    sys.exit(main())
