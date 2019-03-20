=======
HmtNote
=======


.. image:: https://img.shields.io/pypi/v/hmtnote.svg
        :target: https://pypi.python.org/pypi/hmtnote

.. image:: https://travis-ci.com/robertopreste/HmtNote.svg?token=zzk3yyGKDnWjk4pFXFuz&branch=master
    :target: https://travis-ci.com/robertopreste/HmtNote

.. image:: https://circleci.com/gh/robertopreste/HmtNote.svg?style=svg&circle-token=b910c3491e8df21fee34293ace05a35a116759c7
    :target: https://circleci.com/gh/robertopreste/HmtNote

.. image:: https://codecov.io/gh/robertopreste/HmtNote/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/robertopreste/HmtNote

.. image:: https://readthedocs.org/projects/hmtnote/badge/?version=latest
        :target: https://hmtnote.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/robertopreste/HmtNote/shield.svg
     :target: https://pyup.io/repos/github/robertopreste/HmtNote/
     :alt: Updates


Human mitochondrial variants annotation using HmtVar.


* Free software: MIT license
* Documentation: https://hmtnote.readthedocs.io.


Features
--------

HmtNote is a bioinformatics tool that can be used to annotate human mitochondrial variants from a VCF, using data available on HmtVar_.

Annotations are grouped into basic, cross-reference, variability and predictions, depending on the type of information they provide.

Basic
=====

Basic information about the variant; they include:

* Locus: Locus to which the variant belongs
* AaChange: Aminoacidic change determined
* Pathogenicity: Pathogenicity predicted by HmtVar
* DiseaseScore: Disease score calculated by HmtVar
* HmtVar: HmtVar_ ID of the variant (can be used to view the related VariantCard on `https://www.hmtvar.uniba.it/varCard/<HmtVarID>`)

Cross-reference
===============

Cross-reference information about the variant; they include:

* Clinvar: Clinvar_ ID of the variant
* dbSNP: dbSNP_ ID of the variant
* OMIM: OMIM_ ID of the variant
* MitomapAssociatedDiseases: Diseases associated to the variant according to Mitomap_
* MitomapSomaticMutations: Diseases associated to the variant according to `Mitomap Somatic Mutations`_

Variability
===========

Variability and allele frequency data about the variant; they include:

* NtVarH: Nucleotide variability of the position in healthy individuals
* NtVarP: Nucleotide variability of the position in patient individuals
* AaVarH: Aminoacid variability of the position in healthy individuals
* AaVarP: Aminoacid variability of the position in patient individuals
* AlleleFreqH: Allele frequency of the variant in healthy individuals overall
* AlleleFreqP: Allele frequency of the variant in patient individuals overall
* AlleleFreqH_AF: Allele frequency of the variant in healthy individuals from Africa
* AlleleFreqP_AF: Allele frequency of the variant in patient individuals from Africa
* AlleleFreqH_AM: Allele frequency of the variant in healthy individuals from America
* AlleleFreqP_AM: Allele frequency of the variant in patient individuals from America
* AlleleFreqH_AS: Allele frequency of the variant in healthy individuals from Asia
* AlleleFreqP_AS: Allele frequency of the variant in patient individuals from Asia
* AlleleFreqH_EU: Allele frequency of the variant in healthy individuals from Europe
* AlleleFreqP_EU: Allele frequency of the variant in patient individuals from Europe
* AlleleFreqH_OC: Allele frequency of the variant in healthy individuals from Oceania
* AlleleFreqP_OC: Allele frequency of the variant in patient individuals from Oceania

Predictions
===========

Pathogenicity prediction information of the variant from external resources; they include:

* MutPred_Prediction: Pathogenicity prediction offered by MutPred_
* MutPred_Probability: Confidence of the pathogenicity prediction offered by MutPred_
* Panther_Prediction: Pathogenicity prediction offered by Panther_
* Panther_Probability: Confidence of the pathogenicity prediction offered by Panther_
* PhDSNP_Prediction: Pathogenicity prediction offered by `PhD SNP`_
* PhDSNP_Probability: Confidence of the pathogenicity prediction offered by `PhD SNP`_
* SNPsGO_Prediction: Pathogenicity prediction offered by `SNPs & GO`_
* SNPsGO_Probability: Confidence of the pathogenicity prediction offered by `SNPs & GO`_
* Polyphen2HumDiv_Prediction: Pathogenicity prediction offered by Polyphen2_ HumDiv
* Polyphen2HumDiv_Probability: Confidence of the pathogenicity prediction offered by Polyphen2_ HumDiv
* Polyphen2HumVar_Prediction: Pathogenicity prediction offered by Polyphen2_ HumVar
* Polyphen2HumVar_Probability: Confidence of the pathogenicity prediction offered by Polyphen2_ HumVar

Usage
-----

Command Line Interface
======================

HmtNote can be used as a command line tool, by simply providing the original VCF and the filename where the annotated VCF will be saved::

    hmtnote input_vcf.vcf annotated_vcf.vcf

By default, HmtNote will annotate the VCF using all four groups of annotations (basic, cross-reference, variability and predictions). If desired, you can specify which kind of annotation you want, using respectively ``--basic``, ``--crossref``, ``--variab`` and ``--predict`` (or ``-b``, ``-c``, ``-v``, ``-p``)::

    hmtnote input_vcf.vcf annotated_basic_vcf.vcf --basic
    hmtnote input_vcf.vcf annotated_crossreferences_vcf.vcf --crossref
    hmtnote input_vcf.vcf annotated_variability_vcf.vcf --variability
    hmtnote input_vcf.vcf annotated_predictions_vcf.vcf --predict

Python Module
=============

HmtNote can also be imported in a Python script and its function ``annotate_vcf()`` can be used to annotated a given VCF::

    from hmtnote import annotate_vcf
    annotate_vcf("input_vcf.vcf", "annotated_vcf.vcf")

By default, ``annotate_vcf()`` will annotate the VCF using all four groups of annotations (basic, cross-reference, variability and predictions). If desired, you can specify which kind of annotation you want, using respectively the ``basic=True``, ``crossref=True``, ``variab=True``, ``predict=True`` arguments::

    annotate_vcf("input_vcf.vcf", "annotated_basic_vcf.vcf", basic=True)
    annotate_vcf("input_vcf.vcf", "annotated_crossreferences_vcf.vcf", crossref=True)
    annotate_vcf("input_vcf.vcf", "annotated_variability_vcf.vcf", variab=True)
    annotate_vcf("input_vcf.vcf", "annotated_predictions_vcf.vcf", predict=True)

Installation
------------

**PLEASE NOTE: HmtNote only supports Python 3!**

The preferred installation method for HmtNote is using ``pip`` in a conda environment:

.. code-block:: console

    $ conda install requests
    $ conda install -c bioconda cyvcf2
    $ pip install hmtnote

If you have issues, please refer to the Installation_ section of the Documentation_.


Credits
-------

This package was created with Cookiecutter_ and the `cc-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cc-pypackage`: https://github.com/robertopreste/cc-pypackage
.. _HmtVar: https://www.hmtvar.uniba.it
.. _Clinvar: https://www.ncbi.nlm.nih.gov/clinvar/
.. _OMIM: https://www.omim.org
.. _dbSNP: https://www.ncbi.nlm.nih.gov/snp
.. _`Mitomap Somatic Mutations`: https://www.mitomap.org/foswiki/bin/view/MITOMAP/MutationsSomatic
.. _Mitomap: https://www.mitomap.org/MITOMAP/MutationsCodingControl
.. _MutPred: http://mutpred.mutdb.org
.. _Panther: http://pantherdb.org
.. _`PhD SNP`: http://snps.biofold.org/phd-snp/phd-snp.html
.. _`SNPs & GO`: https://snps-and-go.biocomp.unibo.it/snps-and-go/
.. _Polyphen2: http://genetics.bwh.harvard.edu/pph2/
.. _Documentation: https://hmtnote.readthedocs.io
.. _Installation: https://hmtnote.readthedocs.io/en/latest/installation.html
