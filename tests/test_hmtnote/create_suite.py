#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import argparse
import click
import os
from hmtnote import annotate, dump


def check(vcf_online, vcf_offline):
    assert os.path.getsize(vcf_online) == os.path.getsize(vcf_offline)
    with open(vcf_online) as vcf1, open(vcf_offline) as vcf2:
        assert vcf1.read() == vcf2.read()


def main(input_vcf: str):
    """
    Launch all the annotations (online and offline) on the given VCF file.
    :param str input_vcf: input vcf file name
    :return:
    """
    basename = os.path.splitext(input_vcf)[0]

    click.echo("Starting online annotations.")
    click.echo("\tPerforming basic annotation... ", nl=False)
    annotate(input_vcf, "{}_ann_basic.vcf".format(basename), basic=True)
    click.echo("Done.")
    click.echo("\tPerforming crossref annotation... ", nl=False)
    annotate(input_vcf, "{}_ann_crossref.vcf".format(basename), crossref=True)
    click.echo("Done.")
    click.echo("\tPerforming variab annotation... ", nl=False)
    annotate(input_vcf, "{}_ann_variab.vcf".format(basename), variab=True)
    click.echo("Done.")
    click.echo("\tPerforming predict annotation... ", nl=False)
    annotate(input_vcf, "{}_ann_predict.vcf".format(basename), predict=True)
    click.echo("Done.")
    click.echo("\tPerforming full annotation... ", nl=False)
    annotate(input_vcf, "{}_ann.vcf".format(basename))
    click.echo("Done.")

    click.echo(" ")
    dump()
    click.echo(" ")

    click.echo("Starting offline annotations.")
    click.echo("\tPerforming offline basic annotation... ", nl=False)
    annotate(input_vcf, "{}_ann_offline_basic.vcf".format(basename),
             basic=True, offline=True)
    click.echo("Done.")
    click.echo("\tPerforming offline crossref annotation... ", nl=False)
    annotate(input_vcf, "{}_ann_offline_crossref.vcf".format(basename),
             crossref=True, offline=True)
    click.echo("Done.")
    click.echo("\tPerforming offline variab annotation... ", nl=False)
    annotate(input_vcf, "{}_ann_offline_variab.vcf".format(basename),
             variab=True, offline=True)
    click.echo("Done.")
    click.echo("\tPerforming offline predict annotation... ", nl=False)
    annotate(input_vcf, "{}_ann_offline_predict.vcf".format(basename),
             predict=True, offline=True)
    click.echo("Done.")
    click.echo("\tPerforming offline full annotation... ", nl=False)
    annotate(input_vcf, "{}_ann_offline.vcf".format(basename), offline=True)
    click.echo("Done.")

    # Checks
    click.echo("\nPerforming checks... ", nl=False)
    check("{}_ann_basic.vcf".format(basename),
          "{}_ann_offline_basic.vcf".format(basename))
    check("{}_ann_crossref.vcf".format(basename),
          "{}_ann_offline_crossref.vcf".format(basename))
    check("{}_ann_variab.vcf".format(basename),
          "{}_ann_offline_variab.vcf".format(basename))
    check("{}_ann_predict.vcf".format(basename),
          "{}_ann_offline_predict.vcf".format(basename))
    check("{}_ann.vcf".format(basename),
          "{}_ann_offline.vcf".format(basename))
    click.echo("All checks passed.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Create all the 
    required test files given the input vcf provided.""")
    parser.add_argument("input_vcf", help="""Input VCF to annotate.""")
    args = parser.parse_args()

    main(args.input_vcf)


