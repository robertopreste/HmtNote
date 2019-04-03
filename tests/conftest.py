#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import os

TESTDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_hmtnote")
SAMPLE_VCF = os.path.join(TESTDIR, "HG00119_filt.vcf")
INDELS_VCF = os.path.join(TESTDIR, "indels.vcf")
ANN_VCF = os.path.join(TESTDIR, "HG00119_ann.vcf")
INDELS_ANN_VCF = os.path.join(TESTDIR, "indels_ann.vcf")
ANN_BASIC_VCF = os.path.join(TESTDIR, "HG00119_ann_basic.vcf")
INDELS_ANN_BASIC_VCF = os.path.join(TESTDIR, "indels_ann_basic.vcf")
ANN_CROSSREF_VCF = os.path.join(TESTDIR, "HG00119_ann_crossref.vcf")
INDELS_ANN_CROSSREF_VCF = os.path.join(TESTDIR, "indels_ann_crossref.vcf")
ANN_VARIAB_VCF = os.path.join(TESTDIR, "HG00119_ann_variab.vcf")
INDELS_ANN_VARIAB_VCF = os.path.join(TESTDIR, "indels_ann_variab.vcf")
ANN_PREDICT_VCF = os.path.join(TESTDIR, "HG00119_ann_predict.vcf")
INDELS_ANN_PREDICT_VCF = os.path.join(TESTDIR, "indels_ann_predict.vcf")
ANN_OFFLINE_VCF = os.path.join(TESTDIR, "HG00119_ann_offline.vcf")
INDELS_ANN_OFFLINE_VCF = os.path.join(TESTDIR, "indels_ann_offline.vcf")
ANN_OFFLINE_BASIC_VCF = os.path.join(TESTDIR, "HG00119_ann_offline_basic.vcf")
INDELS_ANN_OFFLINE_BASIC_VCF = os.path.join(TESTDIR, "indels_ann_offline_basic.vcf")
ANN_OFFLINE_CROSSREF_VCF = os.path.join(TESTDIR, "HG00119_ann_offline_crossref.vcf")
INDELS_ANN_OFFLINE_CROSSREF_VCF = os.path.join(TESTDIR, "indels_ann_offline_crossref.vcf")
ANN_OFFLINE_VARIAB_VCF = os.path.join(TESTDIR, "HG00119_ann_offline_variab.vcf")
INDELS_ANN_OFFLINE_VARIAB_VCF = os.path.join(TESTDIR, "indels_ann_offline_variab.vcf")
ANN_OFFLINE_PREDICT_VCF = os.path.join(TESTDIR, "HG00119_ann_offline_predict.vcf")
INDELS_ANN_OFFLINE_PREDICT_VCF = os.path.join(TESTDIR, "indels_ann_offline_predict.vcf")


# basic VCF file

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


@pytest.fixture
def sample_ann_offline_vcf():
    """Open the sample VCF file with full offline annotation."""
    with open(ANN_OFFLINE_VCF) as f:
        yield f


@pytest.fixture
def sample_ann_offline_basic_vcf():
    """Open the sample VCF file with basic offline annotation."""
    with open(ANN_OFFLINE_BASIC_VCF) as f:
        yield f


@pytest.fixture
def sample_ann_offline_crossref_vcf():
    """Open the sample VCF file with crossref offline annotation."""
    with open(ANN_OFFLINE_CROSSREF_VCF) as f:
        yield f


@pytest.fixture
def sample_ann_offline_variab_vcf():
    """Open the sample VCF file with variability offline annotation."""
    with open(ANN_OFFLINE_VARIAB_VCF) as f:
        yield f


@pytest.fixture
def sample_ann_offline_predict_vcf():
    """Open the sample VCF file with predictions offline annotation."""
    with open(ANN_OFFLINE_PREDICT_VCF) as f:
        yield f


# indels VCF file

@pytest.fixture
def indels_vcf():
    """Open the indels VCF file."""
    with open(INDELS_VCF) as f:
        yield f


@pytest.fixture
def indels_ann_vcf():
    """Open the indels VCF file with full annotation."""
    with open(INDELS_ANN_VCF) as f:
        yield f


@pytest.fixture
def indels_ann_basic_vcf():
    """Open the indels VCF file with basic annotation."""
    with open(INDELS_ANN_BASIC_VCF) as f:
        yield f


@pytest.fixture
def indels_ann_crossref_vcf():
    """Open the indels VCF file with crossref annotation."""
    with open(INDELS_ANN_CROSSREF_VCF) as f:
        yield f


@pytest.fixture
def indels_ann_variab_vcf():
    """Open the indels VCF file with variability annotation."""
    with open(INDELS_ANN_VARIAB_VCF) as f:
        yield f


@pytest.fixture
def indels_ann_predict_vcf():
    """Open the indels VCF file with predictions annotation."""
    with open(INDELS_ANN_PREDICT_VCF) as f:
        yield f


@pytest.fixture
def indels_ann_offline_vcf():
    """Open the indels VCF file with full offline annotation."""
    with open(INDELS_ANN_OFFLINE_VCF) as f:
        yield f


@pytest.fixture
def indels_ann_offline_basic_vcf():
    """Open the indels VCF file with basic offline annotation."""
    with open(INDELS_ANN_OFFLINE_BASIC_VCF) as f:
        yield f


@pytest.fixture
def indels_ann_offline_crossref_vcf():
    """Open the indels VCF file with crossref offline annotation."""
    with open(INDELS_ANN_OFFLINE_CROSSREF_VCF) as f:
        yield f


@pytest.fixture
def indels_ann_offline_variab_vcf():
    """Open the indels VCF file with variability offline annotation."""
    with open(INDELS_ANN_OFFLINE_VARIAB_VCF) as f:
        yield f


@pytest.fixture
def indels_ann_offline_predict_vcf():
    """Open the indels VCF file with predictions offline annotation."""
    with open(INDELS_ANN_OFFLINE_PREDICT_VCF) as f:
        yield f
