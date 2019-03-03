#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import os

TESTDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_hmtnote")
SAMPLE_VCF = os.path.join(TESTDIR, "HG00119_filt.vcf")
ANN_VCF = os.path.join(TESTDIR, "HG00119_ann.vcf")
ANN_BASIC_VCF = os.path.join(TESTDIR, "HG00119_ann_basic.vcf")
ANN_CROSSREF_VCF = os.path.join(TESTDIR, "HG00119_ann_crossref.vcf")
ANN_VARIAB_VCF = os.path.join(TESTDIR, "HG00119_ann_variab.vcf")
ANN_PREDICT_VCF = os.path.join(TESTDIR, "HG00119_ann_predict.vcf")


@pytest.fixture
def sample_vcf():
    """Open the sample VCF file."""
    with open(SAMPLE_VCF) as f:
        yield f


@pytest.fixture
def sample_ann_vcf():
    """Open the sample VCF file with full annotation."""
    with open(ANN_VCF) as f:
        yield f


@pytest.fixture
def sample_ann_basic_vcf():
    """Open the sample VCF file with basic annotation."""
    with open(ANN_BASIC_VCF) as f:
        yield f


@pytest.fixture
def sample_ann_crossref_vcf():
    """Open the sample VCF file with crossref annotation."""
    with open(ANN_CROSSREF_VCF) as f:
        yield f


@pytest.fixture
def sample_ann_variab_vcf():
    """Open the sample VCF file with variability annotation."""
    with open(ANN_VARIAB_VCF) as f:
        yield f


@pytest.fixture
def sample_ann_predict_vcf():
    """Open the sample VCF file with predictions annotation."""
    with open(ANN_PREDICT_VCF) as f:
        yield f
