#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
from click.testing import CliRunner
# from hmtnote.hmtnote import annotate_vcf
from hmtnote import cli


TESTDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_hmtnote")


def test_cli():
    """Test the main CLI command. Should exit with an error code 2, since no input and output files
    are specified."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 2


def test_cli_help():
    """Test the CLI help."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output


def test_cli_annotation(sample_ann_vcf):
    """Test the full annotation of the sample VCF file."""
    runner = CliRunner()
    result = runner.invoke(cli.main, [os.path.join(TESTDIR, "HG00119_filt.vcf"),
                                      os.path.join(TESTDIR, "HG00119_test.vcf")])
    assert result.exit_code == 0
    with open(os.path.join(TESTDIR, "HG00119_test.vcf")) as out:
        assert sample_ann_vcf.read() == out.read()


def test_cli_annotation_basic(sample_ann_basic_vcf):
    """Test the basic annotation of the sample VCF file."""
    runner = CliRunner()
    result = runner.invoke(cli.main, [os.path.join(TESTDIR, "HG00119_filt.vcf"),
                                      os.path.join(TESTDIR, "HG00119_test.vcf"),
                                      "--basic"])
    assert result.exit_code == 0
    with open(os.path.join(TESTDIR, "HG00119_test.vcf")) as out:
        assert sample_ann_basic_vcf.read() == out.read()


def test_cli_annotation_crossref(sample_ann_crossref_vcf):
    """Test the crossref annotation of the sample VCF file."""
    runner = CliRunner()
    result = runner.invoke(cli.main, [os.path.join(TESTDIR, "HG00119_filt.vcf"),
                                      os.path.join(TESTDIR, "HG00119_test.vcf"),
                                      "--crossref"])
    assert result.exit_code == 0
    with open(os.path.join(TESTDIR, "HG00119_test.vcf")) as out:
        assert sample_ann_crossref_vcf.read() == out.read()


def test_cli_annotation_variab(sample_ann_variab_vcf):
    """Test the variability annotation of the sample VCF file."""
    runner = CliRunner()
    result = runner.invoke(cli.main, [os.path.join(TESTDIR, "HG00119_filt.vcf"),
                                      os.path.join(TESTDIR, "HG00119_test.vcf"),
                                      "--variab"])
    assert result.exit_code == 0
    with open(os.path.join(TESTDIR, "HG00119_test.vcf")) as out:
        assert sample_ann_variab_vcf.read() == out.read()


def test_cli_annotation_predict(sample_ann_predict_vcf):
    """Test the predictions annotation of the VCF file."""
    runner = CliRunner()
    result = runner.invoke(cli.main, [os.path.join(TESTDIR, "HG00119_filt.vcf"),
                                      os.path.join(TESTDIR, "HG00119_test.vcf"),
                                      "--predict"])
    assert result.exit_code == 0
    with open(os.path.join(TESTDIR, "HG00119_test.vcf")) as out:
        assert sample_ann_predict_vcf.read() == out.read()

