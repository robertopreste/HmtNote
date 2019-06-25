#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
from hmtnote import annotate


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
BCFTOOLS_VCF = os.path.join(DATADIR, "bcftools.vcf")
TEST_VCF = os.path.join(DATADIR, "test.vcf")


def test_bcftools_module_annotation(bcftools_ann_vcf):
    """Test the full annotation of the bcftools VCF file using the imported
    module."""
    annotate(BCFTOOLS_VCF, TEST_VCF)
    with open(TEST_VCF) as out:
        assert bcftools_ann_vcf.read() == out.read()


def test_bcftools_module_annotation_basic(bcftools_ann_basic_vcf):
    """Test the basic annotation of the bcftools VCF file using the imported
    module."""
    annotate(BCFTOOLS_VCF, TEST_VCF, basic=True)
    with open(TEST_VCF) as out:
        assert bcftools_ann_basic_vcf.read() == out.read()


def test_bcftools_module_annotation_crossref(bcftools_ann_crossref_vcf):
    """Test the cross-reference annotation of the bcftools VCF file using the
    imported module."""
    annotate(BCFTOOLS_VCF, TEST_VCF, crossref=True)
    with open(TEST_VCF) as out:
        assert bcftools_ann_crossref_vcf.read() == out.read()


def test_bcftools_module_annotation_variab(bcftools_ann_variab_vcf):
    """Test the variability annotation of the bcftools VCF file using the
    imported module."""
    annotate(BCFTOOLS_VCF, TEST_VCF, variab=True)
    with open(TEST_VCF) as out:
        assert bcftools_ann_variab_vcf.read() == out.read()


def test_bcftools_module_annotation_predict(bcftools_ann_predict_vcf):
    """Test the predictions annotation of the bcftools VCF file using the
    imported module."""
    annotate(BCFTOOLS_VCF, TEST_VCF, predict=True)
    with open(TEST_VCF) as out:
        assert bcftools_ann_predict_vcf.read() == out.read()
