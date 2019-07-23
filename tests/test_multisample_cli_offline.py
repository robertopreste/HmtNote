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
TEST_CSV = os.path.join(DATADIR, "test.csv")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class TestMultisampleCliOffline:

    def test_multisample_cli_dump(self):
        """Test the dump command of the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["dump"])
        assert result.exit_code == 0
        assert os.path.isfile(os.path.join(BASE_DIR, "hmtnote_dump.pkl"))

    def test_multisample_cli_annotation_offline(self,
                                                multisample_ann_offline_vcf,
                                                multisample_ann_offline_csv):
        """Test the full offline annotation of the multisample VCF file
        using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", MULTISAMPLE_VCF, TEST_VCF,
                                          "--offline", "--csv"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert multisample_ann_offline_vcf.read() == out.read()
        with open(TEST_CSV) as out:
            assert multisample_ann_offline_csv.read() == out.read()

    def test_multisample_cli_annotation_offline_basic(self,
                                                      multisample_ann_offline_basic_vcf,
                                                      multisample_ann_offline_basic_csv):
        """Test the basic offline annotation of the multisample VCF file
        using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", MULTISAMPLE_VCF, TEST_VCF,
                                          "--basic", "--offline", "--csv"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert multisample_ann_offline_basic_vcf.read() == out.read()
        with open(TEST_CSV) as out:
            assert multisample_ann_offline_basic_csv.read() == out.read()

    def test_multisample_cli_annotation_offline_crossref(self,
                                                         multisample_ann_offline_crossref_vcf,
                                                         multisample_ann_offline_crossref_csv):
        """Test the cross-reference offline annotation of the multisample
        VCF file using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", MULTISAMPLE_VCF, TEST_VCF,
                                          "--crossref", "--offline", "--csv"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert multisample_ann_offline_crossref_vcf.read() == out.read()
        with open(TEST_CSV) as out:
            assert multisample_ann_offline_crossref_csv.read() == out.read()

    def test_multisample_cli_annotation_offline_variab(self,
                                                       multisample_ann_offline_variab_vcf,
                                                       multisample_ann_offline_variab_csv):
        """Test the variability offline annotation of the multisample VCF
        file using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", MULTISAMPLE_VCF, TEST_VCF,
                                          "--variab", "--offline", "--csv"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert multisample_ann_offline_variab_vcf.read() == out.read()
        with open(TEST_CSV) as out:
            assert multisample_ann_offline_variab_csv.read() == out.read()

    def test_multisample_cli_annotation_offline_predict(self,
                                                        multisample_ann_offline_predict_vcf,
                                                        multisample_ann_offline_predict_csv):
        """Test the predictions offline annotation of the multisample VCF
        file using the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main, ["annotate", MULTISAMPLE_VCF, TEST_VCF,
                                          "--predict", "--offline", "--csv"])
        assert result.exit_code == 0
        with open(TEST_VCF) as out:
            assert multisample_ann_offline_predict_vcf.read() == out.read()
        with open(TEST_CSV) as out:
            assert multisample_ann_offline_predict_csv.read() == out.read()
