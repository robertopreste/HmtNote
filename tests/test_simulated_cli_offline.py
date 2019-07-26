#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
from click.testing import CliRunner
from hmtnote import cli


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
SIMULATED_VCF = os.path.join(DATADIR, "simulated.vcf")
TEST_VCF = os.path.join(DATADIR, "test.vcf")
TEST_CSV = os.path.join(DATADIR, "test.csv")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class TestSimulatedCliOffline:

    def test_simulated_cli_dump(self):
        """Test the dump command of the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["dump"])
        assert result.exit_code == 0
        assert os.path.isfile(os.path.join(BASE_DIR, "hmtnote_dump.pkl"))

    def test_simulated_cli_annotation_offline(self,
                                              simulated_ann_offline_vcf,
                                              simulated_ann_offline_csv):
        """Test the full offline annotation of the simulated VCF file
        using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", SIMULATED_VCF, TEST_VCF,
                                          "--offline", "--csv"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert simulated_ann_offline_vcf.read() == out.read()
        with open(TEST_CSV) as out:
            assert simulated_ann_offline_csv.read() == out.read()

    def test_simulated_cli_annotation_offline_basic(self,
                                                    simulated_ann_offline_basic_vcf,
                                                    simulated_ann_offline_basic_csv):
        """Test the basic offline annotation of the simulated VCF file
        using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", SIMULATED_VCF, TEST_VCF,
                                          "--basic", "--offline", "--csv"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert simulated_ann_offline_basic_vcf.read() == out.read()
        with open(TEST_CSV) as out:
            assert simulated_ann_offline_basic_csv.read() == out.read()

    def test_simulated_cli_annotation_offline_crossref(self,
                                                       simulated_ann_offline_crossref_vcf,
                                                       simulated_ann_offline_crossref_csv):
        """Test the cross-reference offline annotation of the simulated
        VCF file using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", SIMULATED_VCF, TEST_VCF,
                                          "--crossref", "--offline", "--csv"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert simulated_ann_offline_crossref_vcf.read() == out.read()
        with open(TEST_CSV) as out:
            assert simulated_ann_offline_crossref_csv.read() == out.read()

    def test_simulated_cli_annotation_offline_variab(self,
                                                     simulated_ann_offline_variab_vcf,
                                                     simulated_ann_offline_variab_csv):
        """Test the variability offline annotation of the simulated VCF
        file using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", SIMULATED_VCF, TEST_VCF,
                                          "--variab", "--offline", "--csv"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert simulated_ann_offline_variab_vcf.read() == out.read()
        with open(TEST_CSV) as out:
            assert simulated_ann_offline_variab_csv.read() == out.read()

    def test_simulated_cli_annotation_offline_predict(self,
                                                      simulated_ann_offline_predict_vcf,
                                                      simulated_ann_offline_predict_csv):
        """Test the predictions offline annotation of the simulated VCF
        file using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", SIMULATED_VCF, TEST_VCF,
                                          "--predict", "--offline", "--csv"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert simulated_ann_offline_predict_vcf.read() == out.read()
        with open(TEST_CSV) as out:
            assert simulated_ann_offline_predict_csv.read() == out.read()
