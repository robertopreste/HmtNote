#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import os

DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                       "data")
SIMULATED = os.path.join(DATADIR, "simulated.vcf")
SIMULATED_ANN = os.path.join(DATADIR, "simulated_ann.vcf")
SIMULATED_ANN_BASIC = os.path.join(DATADIR, "simulated_ann_basic.vcf")
SIMULATED_ANN_CROSSREF = os.path.join(DATADIR, "simulated_ann_crossref.vcf")
SIMULATED_ANN_VARIAB = os.path.join(DATADIR, "simulated_ann_variab.vcf")
SIMULATED_ANN_PREDICT = os.path.join(DATADIR, "simulated_ann_predict.vcf")
SIMULATED_ANN_OFFLINE = os.path.join(DATADIR, "simulated_ann_offline.vcf")
SIMULATED_ANN_OFFLINE_BASIC = os.path.join(DATADIR, 
                                           "simulated_ann_offline_basic.vcf")
SIMULATED_ANN_OFFLINE_CROSSREF = os.path.join(DATADIR, 
                                              "simulated_ann_offline_crossref.vcf")
SIMULATED_ANN_OFFLINE_VARIAB = os.path.join(DATADIR, 
                                            "simulated_ann_offline_variab.vcf")
SIMULATED_ANN_OFFLINE_PREDICT = os.path.join(DATADIR, 
                                             "simulated_ann_offline_predict.vcf")

BCFTOOLS = os.path.join(DATADIR, "bcftools.vcf")
BCFTOOLS_ANN = os.path.join(DATADIR, "bcftools_ann.vcf")
BCFTOOLS_ANN_BASIC = os.path.join(DATADIR, "bcftools_ann_basic.vcf")
BCFTOOLS_ANN_CROSSREF = os.path.join(DATADIR, "bcftools_ann_crossref.vcf")
BCFTOOLS_ANN_VARIAB = os.path.join(DATADIR, "bcftools_ann_variab.vcf")
BCFTOOLS_ANN_PREDICT = os.path.join(DATADIR, "bcftools_ann_predict.vcf")
BCFTOOLS_ANN_OFFLINE = os.path.join(DATADIR, "bcftools_ann_offline.vcf")
BCFTOOLS_ANN_OFFLINE_BASIC = os.path.join(DATADIR, 
                                          "bcftools_ann_offline_basic.vcf")
BCFTOOLS_ANN_OFFLINE_CROSSREF = os.path.join(DATADIR, 
                                             "bcftools_ann_offline_crossref.vcf")
BCFTOOLS_ANN_OFFLINE_VARIAB = os.path.join(DATADIR, 
                                           "bcftools_ann_offline_variab.vcf")
BCFTOOLS_ANN_OFFLINE_PREDICT = os.path.join(DATADIR, 
                                            "bcftools_ann_offline_predict.vcf")

MULTISAMPLE = os.path.join(DATADIR, "multisample.vcf")
MULTISAMPLE_ANN = os.path.join(DATADIR, "multisample_ann.vcf")
MULTISAMPLE_ANN_BASIC = os.path.join(DATADIR, "multisample_ann_basic.vcf")
MULTISAMPLE_ANN_CROSSREF = os.path.join(DATADIR, "multisample_ann_crossref.vcf")
MULTISAMPLE_ANN_VARIAB = os.path.join(DATADIR, "multisample_ann_variab.vcf")
MULTISAMPLE_ANN_PREDICT = os.path.join(DATADIR, "multisample_ann_predict.vcf")
MULTISAMPLE_ANN_OFFLINE = os.path.join(DATADIR, "multisample_ann_offline.vcf")
MULTISAMPLE_ANN_OFFLINE_BASIC = os.path.join(DATADIR, 
                                          "multisample_ann_offline_basic.vcf")
MULTISAMPLE_ANN_OFFLINE_CROSSREF = os.path.join(DATADIR, 
                                             "multisample_ann_offline_crossref.vcf")
MULTISAMPLE_ANN_OFFLINE_VARIAB = os.path.join(DATADIR, 
                                           "multisample_ann_offline_variab.vcf")
MULTISAMPLE_ANN_OFFLINE_PREDICT = os.path.join(DATADIR, 
                                            "multisample_ann_offline_predict.vcf")


@pytest.fixture
def simulated_vcf():
    """Open the simulated.vcf file."""
    with open(SIMULATED) as f:
        yield f


@pytest.fixture
def simulated_ann_vcf():
    """Open the simulated.vcf file with full annotation."""
    with open(SIMULATED_ANN) as f:
        yield f


@pytest.fixture
def simulated_ann_basic_vcf():
    """Open the simulated.vcf file with basic annotation."""
    with open(SIMULATED_ANN_BASIC) as f:
        yield f


@pytest.fixture
def simulated_ann_crossref_vcf():
    """Open the simulated.vcf file with crossref annotation."""
    with open(SIMULATED_ANN_CROSSREF) as f:
        yield f


@pytest.fixture
def simulated_ann_variab_vcf():
    """Open the simulated.vcf file with variability annotation."""
    with open(SIMULATED_ANN_VARIAB) as f:
        yield f


@pytest.fixture
def simulated_ann_predict_vcf():
    """Open the simulated.vcf file with predictions annotation."""
    with open(SIMULATED_ANN_PREDICT) as f:
        yield f


@pytest.fixture
def simulated_ann_offline_vcf():
    """Open the simulated.vcf file with full offline annotation."""
    with open(SIMULATED_ANN_OFFLINE) as f:
        yield f


@pytest.fixture
def simulated_ann_offline_basic_vcf():
    """Open the simulated.vcf file with basic offline annotation."""
    with open(SIMULATED_ANN_OFFLINE_BASIC) as f:
        yield f


@pytest.fixture
def simulated_ann_offline_crossref_vcf():
    """Open the simulated.vcf file with crossref offline annotation."""
    with open(SIMULATED_ANN_OFFLINE_CROSSREF) as f:
        yield f


@pytest.fixture
def simulated_ann_offline_variab_vcf():
    """Open the simulated.vcf file with variability offline annotation."""
    with open(SIMULATED_ANN_OFFLINE_VARIAB) as f:
        yield f


@pytest.fixture
def simulated_ann_offline_predict_vcf():
    """Open the simulated.vcf file with predictions offline annotation."""
    with open(SIMULATED_ANN_OFFLINE_PREDICT) as f:
        yield f


@pytest.fixture
def bcftools_vcf():
    """Open the bcftools.vcf file."""
    with open(BCFTOOLS) as f:
        yield f


@pytest.fixture
def bcftools_ann_vcf():
    """Open the bcftools.vcf file with full annotation."""
    with open(BCFTOOLS_ANN) as f:
        yield f


@pytest.fixture
def bcftools_ann_basic_vcf():
    """Open the bcftools.vcf file with basic annotation."""
    with open(BCFTOOLS_ANN_BASIC) as f:
        yield f


@pytest.fixture
def bcftools_ann_crossref_vcf():
    """Open the bcftools.vcf file with crossref annotation."""
    with open(BCFTOOLS_ANN_CROSSREF) as f:
        yield f


@pytest.fixture
def bcftools_ann_variab_vcf():
    """Open the bcftools.vcf file with variability annotation."""
    with open(BCFTOOLS_ANN_VARIAB) as f:
        yield f


@pytest.fixture
def bcftools_ann_predict_vcf():
    """Open the bcftools.vcf file with predictions annotation."""
    with open(BCFTOOLS_ANN_PREDICT) as f:
        yield f


@pytest.fixture
def bcftools_ann_offline_vcf():
    """Open the bcftools.vcf file with full offline annotation."""
    with open(BCFTOOLS_ANN_OFFLINE) as f:
        yield f


@pytest.fixture
def bcftools_ann_offline_basic_vcf():
    """Open the bcftools.vcf file with basic offline annotation."""
    with open(BCFTOOLS_ANN_OFFLINE_BASIC) as f:
        yield f


@pytest.fixture
def bcftools_ann_offline_crossref_vcf():
    """Open the bcftools.vcf file with crossref offline annotation."""
    with open(BCFTOOLS_ANN_OFFLINE_CROSSREF) as f:
        yield f


@pytest.fixture
def bcftools_ann_offline_variab_vcf():
    """Open the bcftools.vcf file with variability offline annotation."""
    with open(BCFTOOLS_ANN_OFFLINE_VARIAB) as f:
        yield f


@pytest.fixture
def bcftools_ann_offline_predict_vcf():
    """Open the bcftools.vcf file with predictions offline annotation."""
    with open(BCFTOOLS_ANN_OFFLINE_PREDICT) as f:
        yield f


@pytest.fixture
def multisample_vcf():
    """Open the multisample.vcf file."""
    with open(MULTISAMPLE) as f:
        yield f


@pytest.fixture
def multisample_ann_vcf():
    """Open the multisample.vcf file with full annotation."""
    with open(MULTISAMPLE_ANN) as f:
        yield f


@pytest.fixture
def multisample_ann_basic_vcf():
    """Open the multisample.vcf file with basic annotation."""
    with open(MULTISAMPLE_ANN_BASIC) as f:
        yield f


@pytest.fixture
def multisample_ann_crossref_vcf():
    """Open the multisample.vcf file with crossref annotation."""
    with open(MULTISAMPLE_ANN_CROSSREF) as f:
        yield f


@pytest.fixture
def multisample_ann_variab_vcf():
    """Open the multisample.vcf file with variability annotation."""
    with open(MULTISAMPLE_ANN_VARIAB) as f:
        yield f


@pytest.fixture
def multisample_ann_predict_vcf():
    """Open the multisample.vcf file with predictions annotation."""
    with open(MULTISAMPLE_ANN_PREDICT) as f:
        yield f


@pytest.fixture
def multisample_ann_offline_vcf():
    """Open the multisample.vcf file with full offline annotation."""
    with open(MULTISAMPLE_ANN_OFFLINE) as f:
        yield f


@pytest.fixture
def multisample_ann_offline_basic_vcf():
    """Open the multisample.vcf file with basic offline annotation."""
    with open(MULTISAMPLE_ANN_OFFLINE_BASIC) as f:
        yield f


@pytest.fixture
def multisample_ann_offline_crossref_vcf():
    """Open the multisample.vcf file with crossref offline annotation."""
    with open(MULTISAMPLE_ANN_OFFLINE_CROSSREF) as f:
        yield f


@pytest.fixture
def multisample_ann_offline_variab_vcf():
    """Open the multisample.vcf file with variability offline annotation."""
    with open(MULTISAMPLE_ANN_OFFLINE_VARIAB) as f:
        yield f


@pytest.fixture
def multisample_ann_offline_predict_vcf():
    """Open the multisample.vcf file with predictions offline annotation."""
    with open(MULTISAMPLE_ANN_OFFLINE_PREDICT) as f:
        yield f
