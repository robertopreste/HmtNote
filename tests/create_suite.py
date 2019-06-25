#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import os
from hmtnote import annotate, dump


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
VCFS = ["bcftools.vcf", "multisample.vcf", "simulated.vcf"]


def assert_correct(vcf_online: str, vcf_offline: str):
    """
    Check that two VCF files annotated using online and offline mode are
    identical.

    :param str vcf_online: vcf file annotated with online mode

    :param str vcf_offline: vcf file annotated with offline mode

    :return:
    """
    assert os.path.getsize(vcf_online) == os.path.getsize(vcf_offline)
    with open(vcf_online) as vcf1, open(vcf_offline) as vcf2:
        assert vcf1.read() == vcf2.read()


def check_annotations(input_vcf: str):
    """
    Perform assert_online_offline() on the set of online and offline
    annotated VCF files from the starting VCF file.

    :param str input_vcf: input vcf file name

    :return:
    """
    basename = os.path.splitext(input_vcf)[0]

    click.echo("\nPerforming checks... ", nl=False)
    assert_correct(os.path.join(DATADIR,
                                "{}_ann_basic.vcf".format(basename)),
                   os.path.join(DATADIR,
                                "{}_ann_offline_basic.vcf".format(basename)))
    assert_correct(os.path.join(DATADIR,
                                "{}_ann_crossref.vcf".format(basename)),
                   os.path.join(DATADIR,
                                "{}_ann_offline_crossref.vcf".format(basename)))
    assert_correct(os.path.join(DATADIR,
                                "{}_ann_variab.vcf".format(basename)),
                   os.path.join(DATADIR,
                                "{}_ann_offline_variab.vcf".format(basename)))
    assert_correct(os.path.join(DATADIR,
                                "{}_ann_predict.vcf".format(basename)),
                   os.path.join(DATADIR,
                                "{}_ann_offline_predict.vcf".format(basename)))
    assert_correct(os.path.join(DATADIR,
                                "{}_ann.vcf".format(basename)),
                   os.path.join(DATADIR,
                                "{}_ann_offline.vcf".format(basename)))
    click.echo("All checks passed.")


def launch_annotations(input_vcf: str):
    """
    Perform all the annotations (online and offline) on the given VCF file.

    :param str input_vcf: input vcf file name

    :return:
    """
    basename = os.path.splitext(input_vcf)[0]

    click.echo("Starting online annotations.")
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_basic.vcf".format(basename)),
             basic=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_crossref.vcf".format(basename)),
             crossref=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_variab.vcf".format(basename)),
             variab=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann_predict.vcf".format(basename)),
             predict=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR, "{}_ann.vcf".format(basename)))
    click.echo("Done.")

    click.echo("Starting offline annotations.")
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR,
                          "{}_ann_offline_basic.vcf".format(basename)),
             basic=True, offline=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR,
                          "{}_ann_offline_crossref.vcf".format(basename)),
             crossref=True, offline=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR,
                          "{}_ann_offline_variab.vcf".format(basename)),
             variab=True, offline=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR,
                          "{}_ann_offline_predict.vcf".format(basename)),
             predict=True, offline=True)
    annotate(os.path.join(DATADIR, input_vcf),
             os.path.join(DATADIR,
                          "{}_ann_offline.vcf".format(basename)),
             offline=True)
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
