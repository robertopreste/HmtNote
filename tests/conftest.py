#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import os

TESTDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_hmtnote")


@pytest.fixture
def sample_vcf():
    """Open the sample VCF file."""
    vcf = os.path.join(TESTDIR, "HG00119_filt.vcf")
    with open(vcf) as f:
        yield f


@pytest.fixture
def sample_ann_vcf():
    """Open the sample VCF file with full annotation."""
    vcf = os.path.join(TESTDIR, "HG00119_ann.vcf")
    with open(vcf) as f:
        yield f


@pytest.fixture
def sample_ann_basic_vcf():
    """Open the sample VCF file with basic annotation."""
    vcf = os.path.join(TESTDIR, "HG00119_ann_basic.vcf")
    with open(vcf) as f:
        yield f


@pytest.fixture
def sample_ann_crossref_vcf():
    """Open the sample VCF file with crossref annotation."""
    vcf = os.path.join(TESTDIR, "HG00119_ann_crossref.vcf")
    with open(vcf) as f:
        yield f


@pytest.fixture
def sample_ann_variab_vcf():
    """Open the sample VCF file with variability annotation."""
    vcf = os.path.join(TESTDIR, "HG00119_ann_variab.vcf")
    with open(vcf) as f:
        yield f


@pytest.fixture
def sample_ann_predict_vcf():
    """Open the sample VCF file with predictions annotation."""
    vcf = os.path.join(TESTDIR, "HG00119_ann_predict.vcf")
    with open(vcf) as f:
        yield f
