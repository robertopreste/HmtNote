#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
from click.testing import CliRunner
from hmtnote import cli


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
MULTISAMPLE_VCF = os.path.join(DATADIR, "multisample.vcf")
TEST_VCF = os.path.join(DATADIR, "test.vcf")


def test_multisample_cli_annotation(multisample_ann_vcf):
    """Test the full annotation of the multisample VCF file using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", MULTISAMPLE_VCF, TEST_VCF])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert multisample_ann_vcf.read() == out.read()


def test_multisample_cli_annotation_basic(multisample_ann_basic_vcf):
    """Test the basic annotation of the multisample VCF file using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", MULTISAMPLE_VCF, TEST_VCF,
                                      "--basic"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert multisample_ann_basic_vcf.read() == out.read()


def test_multisample_cli_annotation_crossref(multisample_ann_crossref_vcf):
    """Test the cross-reference annotation of the multisample VCF file using
    the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", MULTISAMPLE_VCF, TEST_VCF,
                                      "--crossref"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert multisample_ann_crossref_vcf.read() == out.read()


def test_multisample_cli_annotation_variab(multisample_ann_variab_vcf):
    """Test the variability annotation of the multisample VCF file using
    the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", MULTISAMPLE_VCF, TEST_VCF,
                                      "--variab"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert multisample_ann_variab_vcf.read() == out.read()


def test_multisample_cli_annotation_predict(multisample_ann_predict_vcf):
    """Test the predictions annotation of the multisample VCF file using
    the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["annotate", MULTISAMPLE_VCF, TEST_VCF,
                                      "--predict"])
    assert result.exit_code == 0
    with open(TEST_VCF) as out:
        assert multisample_ann_predict_vcf.read() == out.read()
