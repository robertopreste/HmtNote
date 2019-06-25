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
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class TestBcftoolsCliOffline:
    def test_bcftools_cli_dump(self):
        """Test the dump command of the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["dump"])
        assert result.exit_code == 0
        assert os.path.isfile(os.path.join(BASE_DIR, "hmtnote_dump.pkl"))

    def test_bcftools_cli_annotation_offline(self, bcftools_ann_offline_vcf):
        """Test the full offline annotation of the bcftools VCF file
        using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                          "--offline"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert bcftools_ann_offline_vcf.read() == out.read()

    def test_bcftools_cli_annotation_offline_basic(self,
                                                   bcftools_ann_offline_basic_vcf):
        """Test the basic offline annotation of the bcftools VCF file
        using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                          "--basic", "--offline"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert bcftools_ann_offline_basic_vcf.read() == out.read()

    def test_bcftools_cli_annotation_offline_crossref(self,
                                                      bcftools_ann_offline_crossref_vcf):
        """Test the cross-reference offline annotation of the bcftools
        VCF file using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                          "--crossref", "--offline"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert bcftools_ann_offline_crossref_vcf.read() == out.read()

    def test_bcftools_cli_annotation_offline_variab(self,
                                                    bcftools_ann_offline_variab_vcf):
        """Test the variability offline annotation of the bcftools VCF
        file using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                          "--variab", "--offline"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert bcftools_ann_offline_variab_vcf.read() == out.read()

    def test_bcftools_cli_annotation_offline_predict(self,
                                                     bcftools_ann_offline_predict_vcf):
        """Test the predictions offline annotation of the bcftools VCF
        file using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", BCFTOOLS_VCF, TEST_VCF,
                                          "--predict", "--offline"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert bcftools_ann_offline_predict_vcf.read() == out.read()
