#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
from hmtnote.hmtnote import annotate_vcf


TESTDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                       "test_hmtnote")
SAMPLE_VCF = os.path.join(TESTDIR, "HG00119_filt.vcf")
INDELS_VCF = os.path.join(TESTDIR, "indels.vcf")
TEST_VCF = os.path.join(TESTDIR, "HG00119_test.vcf")


# basic VCF file

def test_module_annotation(sample_ann_vcf):
    """Test the full annotation of the sample VCF file using the imported
    module."""
    annotate_vcf(SAMPLE_VCF, TEST_VCF)
    with open(TEST_VCF) as out:
        assert sample_ann_vcf.read() == out.read()


def test_module_annotation_basic(sample_ann_basic_vcf):
    """Test the basic annotation of the sample VCF file using the imported
    module."""
    annotate_vcf(SAMPLE_VCF, TEST_VCF, basic=True)
    with open(TEST_VCF) as out:
        assert sample_ann_basic_vcf.read() == out.read()


def test_module_annotation_crossref(sample_ann_crossref_vcf):
    """Test the cross-reference annotation of the sample VCF file using the
    imported module."""
    annotate_vcf(SAMPLE_VCF, TEST_VCF, crossref=True)
    with open(TEST_VCF) as out:
        assert sample_ann_crossref_vcf.read() == out.read()


def test_module_annotation_variab(sample_ann_variab_vcf):
    """Test the variability annotation of the sample VCF file using the
    imported module."""
    annotate_vcf(SAMPLE_VCF, TEST_VCF, variab=True)
    with open(TEST_VCF) as out:
        assert sample_ann_variab_vcf.read() == out.read()


def test_module_annotation_predict(sample_ann_predict_vcf):
    """Test the predictions annotation of the sample VCF file using the
    imported module."""
    annotate_vcf(SAMPLE_VCF, TEST_VCF, predict=True)
    with open(TEST_VCF) as out:
        assert sample_ann_predict_vcf.read() == out.read()


# indels VCF file 

def test_module_indels_annotation(indels_ann_vcf):
    """Test the full annotation of the indels VCF file using the imported
    module."""
    annotate_vcf(INDELS_VCF, TEST_VCF)
    with open(TEST_VCF) as out:
        assert indels_ann_vcf.read() == out.read()


def test_module_indels_annotation_basic(indels_ann_basic_vcf):
    """Test the basic annotation of the indels VCF file using the imported
    module."""
    annotate_vcf(INDELS_VCF, TEST_VCF, basic=True)
    with open(TEST_VCF) as out:
        assert indels_ann_basic_vcf.read() == out.read()


def test_module_indels_annotation_crossref(indels_ann_crossref_vcf):
    """Test the cross-reference annotation of the indels VCF file using the
    imported module."""
    annotate_vcf(INDELS_VCF, TEST_VCF, crossref=True)
    with open(TEST_VCF) as out:
        assert indels_ann_crossref_vcf.read() == out.read()


def test_module_indels_annotation_variab(indels_ann_variab_vcf):
    """Test the variability annotation of the indels VCF file using the
    imported module."""
    annotate_vcf(INDELS_VCF, TEST_VCF, variab=True)
    with open(TEST_VCF) as out:
        assert indels_ann_variab_vcf.read() == out.read()


def test_module_indels_annotation_predict(indels_ann_predict_vcf):
    """Test the predictions annotation of the indels VCF file using the
    imported module."""
    annotate_vcf(INDELS_VCF, TEST_VCF, predict=True)
    with open(TEST_VCF) as out:
        assert indels_ann_predict_vcf.read() == out.read()
