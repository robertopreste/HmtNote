#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
from hmtnote import annotate, dump


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
BCFTOOLS_VCF = os.path.join(DATADIR, "bcftools.vcf")
TEST_VCF = os.path.join(DATADIR, "test.vcf")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class TestBcftoolsModuleOffline:
    def test_bcftools_module_dump(self):
        """Test the dump command of the module."""
        dump()
        assert os.path.isfile(os.path.join(BASE_DIR, "hmtnote_dump.pkl"))

    def test_bcftools_module_annotation_offline(self,
                                                bcftools_ann_offline_vcf):
        """Test the full offline annotation of the bcftools VCF file using
        the module."""
        annotate(BCFTOOLS_VCF, TEST_VCF, offline=True)
        with open(TEST_VCF) as out:
            assert bcftools_ann_offline_vcf.read() == out.read()

    def test_bcftools_module_annotation_offline_basic(self,
                                                      bcftools_ann_offline_basic_vcf):
        """Test the basic offline annotation of the bcftools VCF file using
        the module."""
        annotate(BCFTOOLS_VCF, TEST_VCF, basic=True, offline=True)
        with open(TEST_VCF) as out:
            assert bcftools_ann_offline_basic_vcf.read() == out.read()

    def test_bcftools_module_annotation_offline_crossref(self,
                                                         bcftools_ann_offline_crossref_vcf):
        """Test the cross-reference offline annotation of the bcftools VCF
        file using the module."""
        annotate(BCFTOOLS_VCF, TEST_VCF, crossref=True, offline=True)
        with open(TEST_VCF) as out:
            assert bcftools_ann_offline_crossref_vcf.read() == out.read()

    def test_bcftools_module_annotation_offline_variab(self,
                                                       bcftools_ann_offline_variab_vcf):
        """Test the variability offline annotation of the bcftools VCF file
        using the module."""
        annotate(BCFTOOLS_VCF, TEST_VCF, variab=True, offline=True)
        with open(TEST_VCF) as out:
            assert bcftools_ann_offline_variab_vcf.read() == out.read()

    def test_bcftools_module_annotation_offline_predict(self,
                                                        bcftools_ann_offline_predict_vcf):
        """Test the predictions offline annotation of the bcftools VCF file
        using the module."""
        annotate(BCFTOOLS_VCF, TEST_VCF, predict=True, offline=True)
        with open(TEST_VCF) as out:
            assert bcftools_ann_offline_predict_vcf.read() == out.read()
