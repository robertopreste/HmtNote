#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
from click.testing import CliRunner
from hmtnote import cli


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
BCFTOOLS_VCF = os.path.join(DATADIR, "bcftools.vcf")
TEST_VCF = os.path.join(DATADIR, "test.vcf")


def test_bcftools_cli_annotation(bcftools_ann_vcf):
    """Test the full annotation of the bcftools VCF file using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert bcftools_ann_vcf.read() == out.read()


def test_bcftools_cli_annotation_basic(bcftools_ann_basic_vcf):
    """Test the basic annotation of the bcftools VCF file using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                      "--basic"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert bcftools_ann_basic_vcf.read() == out.read()


def test_bcftools_cli_annotation_crossref(bcftools_ann_crossref_vcf):
    """Test the cross-reference annotation of the bcftools VCF file using
    the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                      "--crossref"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert bcftools_ann_crossref_vcf.read() == out.read()


def test_bcftools_cli_annotation_variab(bcftools_ann_variab_vcf):
    """Test the variability annotation of the bcftools VCF file using
    the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                      "--variab"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert bcftools_ann_variab_vcf.read() == out.read()


def test_bcftools_cli_annotation_predict(bcftools_ann_predict_vcf):
    """Test the predictions annotation of the bcftools VCF file using
    the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                      "--predict"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert bcftools_ann_predict_vcf.read() == out.read()
