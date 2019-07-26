#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import os

DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                       "data")
SIMULATED = os.path.join(DATADIR, "simulated.vcf")
# vcf
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
# csv
SIMULATED_ANN_CSV = os.path.join(DATADIR, "simulated_ann.csv")
SIMULATED_ANN_BASIC_CSV = os.path.join(DATADIR, "simulated_ann_basic.csv")
SIMULATED_ANN_CROSSREF_CSV = os.path.join(DATADIR, "simulated_ann_crossref.csv")
SIMULATED_ANN_VARIAB_CSV = os.path.join(DATADIR, "simulated_ann_variab.csv")
SIMULATED_ANN_PREDICT_CSV = os.path.join(DATADIR, "simulated_ann_predict.csv")
SIMULATED_ANN_OFFLINE_CSV = os.path.join(DATADIR, "simulated_ann_offline.csv")
SIMULATED_ANN_OFFLINE_BASIC_CSV = os.path.join(DATADIR, 
                                               "simulated_ann_offline_basic.csv")
SIMULATED_ANN_OFFLINE_CROSSREF_CSV = os.path.join(DATADIR, 
                                                  "simulated_ann_offline_crossref.csv")
SIMULATED_ANN_OFFLINE_VARIAB_CSV = os.path.join(DATADIR, 
                                                "simulated_ann_offline_variab.csv")
SIMULATED_ANN_OFFLINE_PREDICT_CSV = os.path.join(DATADIR, 
                                                 "simulated_ann_offline_predict.csv")

BCFTOOLS = os.path.join(DATADIR, "bcftools.vcf")
# vcf
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
# csv
BCFTOOLS_ANN_CSV = os.path.join(DATADIR, "bcftools_ann.csv")
BCFTOOLS_ANN_BASIC_CSV = os.path.join(DATADIR, "bcftools_ann_basic.csv")
BCFTOOLS_ANN_CROSSREF_CSV = os.path.join(DATADIR, "bcftools_ann_crossref.csv")
BCFTOOLS_ANN_VARIAB_CSV = os.path.join(DATADIR, "bcftools_ann_variab.csv")
BCFTOOLS_ANN_PREDICT_CSV = os.path.join(DATADIR, "bcftools_ann_predict.csv")
BCFTOOLS_ANN_OFFLINE_CSV = os.path.join(DATADIR, "bcftools_ann_offline.csv")
BCFTOOLS_ANN_OFFLINE_BASIC_CSV = os.path.join(DATADIR, 
                                              "bcftools_ann_offline_basic.csv")
BCFTOOLS_ANN_OFFLINE_CROSSREF_CSV = os.path.join(DATADIR, 
                                                 "bcftools_ann_offline_crossref.csv")
BCFTOOLS_ANN_OFFLINE_VARIAB_CSV = os.path.join(DATADIR, 
                                               "bcftools_ann_offline_variab.csv")
BCFTOOLS_ANN_OFFLINE_PREDICT_CSV = os.path.join(DATADIR, 
                                                "bcftools_ann_offline_predict.csv")

MULTISAMPLE = os.path.join(DATADIR, "multisample.vcf")
# vcf
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
# csv
MULTISAMPLE_ANN_CSV = os.path.join(DATADIR, "multisample_ann.csv")
MULTISAMPLE_ANN_BASIC_CSV = os.path.join(DATADIR, "multisample_ann_basic.csv")
MULTISAMPLE_ANN_CROSSREF_CSV = os.path.join(DATADIR, "multisample_ann_crossref.csv")
MULTISAMPLE_ANN_VARIAB_CSV = os.path.join(DATADIR, "multisample_ann_variab.csv")
MULTISAMPLE_ANN_PREDICT_CSV = os.path.join(DATADIR, "multisample_ann_predict.csv")
MULTISAMPLE_ANN_OFFLINE_CSV = os.path.join(DATADIR, "multisample_ann_offline.csv")
MULTISAMPLE_ANN_OFFLINE_BASIC_CSV = os.path.join(DATADIR,
                                                 "multisample_ann_offline_basic.csv")
MULTISAMPLE_ANN_OFFLINE_CROSSREF_CSV = os.path.join(DATADIR,
                                                    "multisample_ann_offline_crossref.csv")
MULTISAMPLE_ANN_OFFLINE_VARIAB_CSV = os.path.join(DATADIR,
                                                  "multisample_ann_offline_variab.csv")
MULTISAMPLE_ANN_OFFLINE_PREDICT_CSV = os.path.join(DATADIR,
                                                   "multisample_ann_offline_predict.csv")


# vcf

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


# csv

@pytest.fixture
def simulated_csv():
    """Open the simulated.csv file."""
    with open(SIMULATED_CSV) as f:
        yield f


@pytest.fixture
def simulated_ann_csv():
    """Open the simulated.csv file with full annotation."""
    with open(SIMULATED_ANN_CSV) as f:
        yield f


@pytest.fixture
def simulated_ann_basic_csv():
    """Open the simulated.csv file with basic annotation."""
    with open(SIMULATED_ANN_BASIC_CSV) as f:
        yield f


@pytest.fixture
def simulated_ann_crossref_csv():
    """Open the simulated.csv file with crossref annotation."""
    with open(SIMULATED_ANN_CROSSREF_CSV) as f:
        yield f


@pytest.fixture
def simulated_ann_variab_csv():
    """Open the simulated.csv file with variability annotation."""
    with open(SIMULATED_ANN_VARIAB_CSV) as f:
        yield f


@pytest.fixture
def simulated_ann_predict_csv():
    """Open the simulated.csv file with predictions annotation."""
    with open(SIMULATED_ANN_PREDICT_CSV) as f:
        yield f


@pytest.fixture
def simulated_ann_offline_csv():
    """Open the simulated.csv file with full offline annotation."""
    with open(SIMULATED_ANN_OFFLINE_CSV) as f:
        yield f


@pytest.fixture
def simulated_ann_offline_basic_csv():
    """Open the simulated.csv file with basic offline annotation."""
    with open(SIMULATED_ANN_OFFLINE_BASIC_CSV) as f:
        yield f


@pytest.fixture
def simulated_ann_offline_crossref_csv():
    """Open the simulated.csv file with crossref offline annotation."""
    with open(SIMULATED_ANN_OFFLINE_CROSSREF_CSV) as f:
        yield f


@pytest.fixture
def simulated_ann_offline_variab_csv():
    """Open the simulated.csv file with variability offline annotation."""
    with open(SIMULATED_ANN_OFFLINE_VARIAB_CSV) as f:
        yield f


@pytest.fixture
def simulated_ann_offline_predict_csv():
    """Open the simulated.csv file with predictions offline annotation."""
    with open(SIMULATED_ANN_OFFLINE_PREDICT_CSV) as f:
        yield f


@pytest.fixture
def bcftools_csv():
    """Open the bcftools.csv file."""
    with open(BCFTOOLS_CSV) as f:
        yield f


@pytest.fixture
def bcftools_ann_csv():
    """Open the bcftools.csv file with full annotation."""
    with open(BCFTOOLS_ANN_CSV) as f:
        yield f


@pytest.fixture
def bcftools_ann_basic_csv():
    """Open the bcftools.csv file with basic annotation."""
    with open(BCFTOOLS_ANN_BASIC_CSV) as f:
        yield f


@pytest.fixture
def bcftools_ann_crossref_csv():
    """Open the bcftools.csv file with crossref annotation."""
    with open(BCFTOOLS_ANN_CROSSREF_CSV) as f:
        yield f


@pytest.fixture
def bcftools_ann_variab_csv():
    """Open the bcftools.csv file with variability annotation."""
    with open(BCFTOOLS_ANN_VARIAB_CSV) as f:
        yield f


@pytest.fixture
def bcftools_ann_predict_csv():
    """Open the bcftools.csv file with predictions annotation."""
    with open(BCFTOOLS_ANN_PREDICT_CSV) as f:
        yield f


@pytest.fixture
def bcftools_ann_offline_csv():
    """Open the bcftools.csv file with full offline annotation."""
    with open(BCFTOOLS_ANN_OFFLINE_CSV) as f:
        yield f


@pytest.fixture
def bcftools_ann_offline_basic_csv():
    """Open the bcftools.csv file with basic offline annotation."""
    with open(BCFTOOLS_ANN_OFFLINE_BASIC_CSV) as f:
        yield f


@pytest.fixture
def bcftools_ann_offline_crossref_csv():
    """Open the bcftools.csv file with crossref offline annotation."""
    with open(BCFTOOLS_ANN_OFFLINE_CROSSREF_CSV) as f:
        yield f


@pytest.fixture
def bcftools_ann_offline_variab_csv():
    """Open the bcftools.csv file with variability offline annotation."""
    with open(BCFTOOLS_ANN_OFFLINE_VARIAB_CSV) as f:
        yield f


@pytest.fixture
def bcftools_ann_offline_predict_csv():
    """Open the bcftools.csv file with predictions offline annotation."""
    with open(BCFTOOLS_ANN_OFFLINE_PREDICT_CSV) as f:
        yield f


@pytest.fixture
def multisample_csv():
    """Open the multisample.csv file."""
    with open(MULTISAMPLE_CSV) as f:
        yield f


@pytest.fixture
def multisample_ann_csv():
    """Open the multisample.csv file with full annotation."""
    with open(MULTISAMPLE_ANN_CSV) as f:
        yield f


@pytest.fixture
def multisample_ann_basic_csv():
    """Open the multisample.csv file with basic annotation."""
    with open(MULTISAMPLE_ANN_BASIC_CSV) as f:
        yield f


@pytest.fixture
def multisample_ann_crossref_csv():
    """Open the multisample.csv file with crossref annotation."""
    with open(MULTISAMPLE_ANN_CROSSREF_CSV) as f:
        yield f


@pytest.fixture
def multisample_ann_variab_csv():
    """Open the multisample.csv file with variability annotation."""
    with open(MULTISAMPLE_ANN_VARIAB_CSV) as f:
        yield f


@pytest.fixture
def multisample_ann_predict_csv():
    """Open the multisample.csv file with predictions annotation."""
    with open(MULTISAMPLE_ANN_PREDICT_CSV) as f:
        yield f


@pytest.fixture
def multisample_ann_offline_csv():
    """Open the multisample.csv file with full offline annotation."""
    with open(MULTISAMPLE_ANN_OFFLINE_CSV) as f:
        yield f


@pytest.fixture
def multisample_ann_offline_basic_csv():
    """Open the multisample.csv file with basic offline annotation."""
    with open(MULTISAMPLE_ANN_OFFLINE_BASIC_CSV) as f:
        yield f


@pytest.fixture
def multisample_ann_offline_crossref_csv():
    """Open the multisample.csv file with crossref offline annotation."""
    with open(MULTISAMPLE_ANN_OFFLINE_CROSSREF_CSV) as f:
        yield f


@pytest.fixture
def multisample_ann_offline_variab_csv():
    """Open the multisample.csv file with variability offline annotation."""
    with open(MULTISAMPLE_ANN_OFFLINE_VARIAB_CSV) as f:
        yield f


@pytest.fixture
def multisample_ann_offline_predict_csv():
    """Open the multisample.csv file with predictions offline annotation."""
    with open(MULTISAMPLE_ANN_OFFLINE_PREDICT_CSV) as f:
        yield f
