#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
from hmtnote import annotate, dump


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
MULTISAMPLE_VCF = os.path.join(DATADIR, "multisample.vcf")
TEST_VCF = os.path.join(DATADIR, "test.vcf")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class TestMultisampleModuleOffline:
    def test_multisample_module_dump(self):
        """Test the dump command of the module."""
        dump()
        assert os.path.isfile(os.path.join(BASE_DIR, "hmtnote_dump.pkl"))

    def test_multisample_module_annotation_offline(self,
                                                   multisample_ann_offline_vcf):
        """Test the full offline annotation of the multisample VCF file using
        the module."""
        annotate(MULTISAMPLE_VCF, TEST_VCF, offline=True)
        with open(TEST_VCF) as out:
            assert multisample_ann_offline_vcf.read() == out.read()

    def test_multisample_module_annotation_offline_basic(self,
                                                         multisample_ann_offline_basic_vcf):
        """Test the basic offline annotation of the multisample VCF file using
        the module."""
        annotate(MULTISAMPLE_VCF, TEST_VCF, basic=True, offline=True)
        with open(TEST_VCF) as out:
            assert multisample_ann_offline_basic_vcf.read() == out.read()

    def test_multisample_module_annotation_offline_crossref(self,
                                                            multisample_ann_offline_crossref_vcf):
        """Test the cross-reference offline annotation of the multisample VCF
        file using the module."""
        annotate(MULTISAMPLE_VCF, TEST_VCF, crossref=True, offline=True)
        with open(TEST_VCF) as out:
            assert multisample_ann_offline_crossref_vcf.read() == out.read()

    def test_multisample_module_annotation_offline_variab(self,
                                                          multisample_ann_offline_variab_vcf):
        """Test the variability offline annotation of the multisample VCF file
        using the module."""
        annotate(MULTISAMPLE_VCF, TEST_VCF, variab=True, offline=True)
        with open(TEST_VCF) as out:
            assert multisample_ann_offline_variab_vcf.read() == out.read()

    def test_multisample_module_annotation_offline_predict(self,
                                                           multisample_ann_offline_predict_vcf):
        """Test the predictions offline annotation of the multisample VCF file
        using the module."""
        annotate(MULTISAMPLE_VCF, TEST_VCF, predict=True, offline=True)
        with open(TEST_VCF) as out:
            assert multisample_ann_offline_predict_vcf.read() == out.read()
