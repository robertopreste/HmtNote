#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
from click.testing import CliRunner
from hmtnote import cli


TESTDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                       "test_hmtnote")
SAMPLE_VCF = os.path.join(TESTDIR, "HG00119_filt.vcf")
TEST_VCF = os.path.join(TESTDIR, "HG00119_test.vcf")


def test_cli():
    """Test the main CLI command."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "Show the version and exit." in result.output
    assert "Show this message and exit." in result.output


def test_cli_help():
    """Test the CLI help (same as invoking without arguments and options)."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--help'])
    assert result.exit_code == 0
    assert "Show the version and exit." in result.output
    assert 'Show this message and exit.' in result.output


def test_cli_annotation(sample_ann_vcf):
    """Test the full annotation of the sample VCF file using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", SAMPLE_VCF, TEST_VCF])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert sample_ann_vcf.read() == out.read()


def test_cli_annotation_basic(sample_ann_basic_vcf):
    """Test the basic annotation of the sample VCF file using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", SAMPLE_VCF, TEST_VCF,
                                      "--basic"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert sample_ann_basic_vcf.read() == out.read()


def test_cli_annotation_crossref(sample_ann_crossref_vcf):
    """Test the cross-reference annotation of the sample VCF file using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", SAMPLE_VCF, TEST_VCF,
                                      "--crossref"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert sample_ann_crossref_vcf.read() == out.read()


def test_cli_annotation_variab(sample_ann_variab_vcf):
    """Test the variability annotation of the sample VCF file using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", SAMPLE_VCF, TEST_VCF,
                                      "--variab"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert sample_ann_variab_vcf.read() == out.read()


def test_cli_annotation_predict(sample_ann_predict_vcf):
    """Test the predictions annotation of the sample VCF file using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", SAMPLE_VCF, TEST_VCF,
                                      "--predict"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert sample_ann_predict_vcf.read() == out.read()