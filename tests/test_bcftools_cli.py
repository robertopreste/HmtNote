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
TEST_CSV = os.path.join(DATADIR, "test.csv")


def test_bcftools_cli_annotation(bcftools_ann_vcf, bcftools_ann_csv):
    """Test the full annotation of the bcftools VCF file using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                      "--csv"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert bcftools_ann_vcf.read() == out.read()
    with open(TEST_CSV) as out:
        assert bcftools_ann_csv.read() == out.read()


def test_bcftools_cli_annotation_basic(bcftools_ann_basic_vcf,
                                       bcftools_ann_basic_csv):
    """Test the basic annotation of the bcftools VCF file using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                      "--basic", "--csv"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert bcftools_ann_basic_vcf.read() == out.read()
    with open(TEST_CSV) as out:
        assert bcftools_ann_basic_csv.read() == out.read()


def test_bcftools_cli_annotation_crossref(bcftools_ann_crossref_vcf,
                                          bcftools_ann_crossref_csv):
    """Test the cross-reference annotation of the bcftools VCF file using
    the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                      "--crossref", "--csv"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert bcftools_ann_crossref_vcf.read() == out.read()
    with open(TEST_CSV) as out:
        assert bcftools_ann_crossref_csv.read() == out.read()


def test_bcftools_cli_annotation_variab(bcftools_ann_variab_vcf,
                                        bcftools_ann_variab_csv):
    """Test the variability annotation of the bcftools VCF file using
    the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                      "--variab", "--csv"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert bcftools_ann_variab_vcf.read() == out.read()
    with open(TEST_CSV) as out:
        assert bcftools_ann_variab_csv.read() == out.read()


def test_bcftools_cli_annotation_predict(bcftools_ann_predict_vcf,
                                         bcftools_ann_predict_csv):
    """Test the predictions annotation of the bcftools VCF file using
    the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                      "--predict", "--csv"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert bcftools_ann_predict_vcf.read() == out.read()
    with open(TEST_CSV) as out:
        assert bcftools_ann_predict_csv.read() == out.read()
