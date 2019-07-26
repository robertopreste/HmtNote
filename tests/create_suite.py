#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import os
from hmtnote import annotate, dump


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
VCFS = ["bcftools.vcf", "multisample.vcf", "simulated.vcf"]


def assert_correct_vcf(vcf_online: str, vcf_offline: str):
    """Check that two VCF files annotated using online and offline mode
    are identical.

    :param str vcf_online: vcf file annotated with online mode

    :param str vcf_offline: vcf file annotated with offline mode

    :return:
    """
    assert os.path.getsize(vcf_online) == os.path.getsize(vcf_offline)
    with open(vcf_online) as vcf1, open(vcf_offline) as vcf2:
        assert vcf1.read() == vcf2.read()


def assert_correct_csv(csv_online: str, csv_offline: str):
    """Check that two CSV files annotated using online and offline mode
    are identical.

    :param str csv_online: csv file annotated with online mode

    :param str csv_offline: csv file annotated with offline mode

    :return:
    """
    assert os.path.getsize(csv_online) == os.path.getsize(csv_offline)
    with open(csv_online) as csv1, open(csv_offline) as csv2:
        assert csv1.read() == csv2.read()


def check_annotations(input_vcf: str):
    """Perform assert_online_offline() on the set of online and offline
    annotated VCF files from the starting VCF file.

    :param str input_vcf: input vcf file name

    :return:
    """
    basename = os.path.splitext(input_vcf)[0]

    click.echo("\nPerforming checks... ", nl=False)
    assert_correct_vcf(os.path.join(DATADIR, "{}_ann_basic.vcf".format(basename)),
                       os.path.join(DATADIR, "{}_ann_offline_basic.vcf".format(basename)))
    assert_correct_csv(os.path.join(DATADIR, "{}_ann_basic.csv".format(basename)),
                       os.path.join(DATADIR, "{}_ann_offline_basic.csv".format(basename)))
    assert_correct_vcf(os.path.join(DATADIR, "{}_ann_crossref.vcf".format(basename)),
                       os.path.join(DATADIR, "{}_ann_offline_crossref.vcf".format(basename)))
    assert_correct_csv(os.path.join(DATADIR, "{}_ann_crossref.csv".format(basename)),
                       os.path.join(DATADIR, "{}_ann_offline_crossref.csv".format(basename)))
    assert_correct_vcf(os.path.join(DATADIR, "{}_ann_variab.vcf".format(basename)),
                       os.path.join(DATADIR, "{}_ann_offline_variab.vcf".format(basename)))
    assert_correct_csv(os.path.join(DATADIR, "{}_ann_variab.csv".format(basename)),
                       os.path.join(DATADIR, "{}_ann_offline_variab.csv".format(basename)))
    assert_correct_vcf(os.path.join(DATADIR, "{}_ann_predict.vcf".format(basename)),
                       os.path.join(DATADIR, "{}_ann_offline_predict.vcf".format(basename)))
    assert_correct_csv(os.path.join(DATADIR, "{}_ann_predict.csv".format(basename)),
                       os.path.join(DATADIR, "{}_ann_offline_predict.csv".format(basename)))
    assert_correct_vcf(os.path.join(DATADIR, "{}_ann.vcf".format(basename)),
                       os.path.join(DATADIR, "{}_ann_offline.vcf".format(basename)))
    assert_correct_csv(os.path.join(DATADIR, "{}_ann.csv".format(basename)),
                       os.path.join(DATADIR, "{}_ann_offline.csv".format(basename)))
    click.echo("All checks passed.")


def launch_annotations(input_vcf: str):
    """Perform all the annotations (online, offline and conversion to
    CSV) on the given VCF file.

    :param str input_vcf: input vcf file name

    :return:
    """
    basename = os.path.splitext(input_vcf)[0]

    click.echo("Starting online annotations.")
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_basic.vcf".format(basename)),
             basic=True, csv=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_crossref.vcf".format(basename)),
             crossref=True, csv=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_variab.vcf".format(basename)),
             variab=True, csv=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_predict.vcf".format(basename)),
             predict=True, csv=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann.vcf".format(basename)), csv=True)
    click.echo("Done.")

    click.echo("Starting offline annotations.")
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_offline_basic.vcf".format(basename)),
             basic=True, offline=True, csv=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_offline_crossref.vcf".format(basename)),
             crossref=True, offline=True, csv=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_offline_variab.vcf".format(basename)),
             variab=True, offline=True, csv=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_offline_predict.vcf".format(basename)),
             predict=True, offline=True, csv=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_offline.vcf".format(basename)),
             offline=True, csv=True)
    click.echo("Done.")


def main():
    """
    First dump the annotation database for offline annotations, then
    annotate each VCF file listed in VCFS.

    :return:
    """
    click.echo("Dumping local database...\n")
    dump()
    click.echo(" ")

    for vcf in VCFS:
        click.echo("\n--- VCF file {} ---\n".format(vcf))
        launch_annotations(vcf)
        check_annotations(vcf)


if __name__ == '__main__':
    main()
