#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
from hmtnote import annotate


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
MULTISAMPLE_VCF = os.path.join(DATADIR, "multisample.vcf")
TEST_VCF = os.path.join(DATADIR, "test.vcf")


def test_multisample_module_annotation(multisample_ann_vcf):
    """Test the full annotation of the multisample VCF file using the imported
    module."""
    annotate(MULTISAMPLE_VCF, TEST_VCF)
    with open(TEST_VCF) as out:
        assert multisample_ann_vcf.read() == out.read()


def test_multisample_module_annotation_basic(multisample_ann_basic_vcf):
    """Test the basic annotation of the multisample VCF file using the imported
    module."""
    annotate(MULTISAMPLE_VCF, TEST_VCF, basic=True)
    with open(TEST_VCF) as out:
        assert multisample_ann_basic_vcf.read() == out.read()


def test_multisample_module_annotation_crossref(multisample_ann_crossref_vcf):
    """Test the cross-reference annotation of the multisample VCF file using the
    imported module."""
    annotate(MULTISAMPLE_VCF, TEST_VCF, crossref=True)
    with open(TEST_VCF) as out:
        assert multisample_ann_crossref_vcf.read() == out.read()


def test_multisample_module_annotation_variab(multisample_ann_variab_vcf):
    """Test the variability annotation of the multisample VCF file using the
    imported module."""
    annotate(MULTISAMPLE_VCF, TEST_VCF, variab=True)
    with open(TEST_VCF) as out:
        assert multisample_ann_variab_vcf.read() == out.read()


def test_multisample_module_annotation_predict(multisample_ann_predict_vcf):
    """Test the predictions annotation of the multisample VCF file using the
    imported module."""
    annotate(MULTISAMPLE_VCF, TEST_VCF, predict=True)
    with open(TEST_VCF) as out:
        assert multisample_ann_predict_vcf.read() == out.read()
