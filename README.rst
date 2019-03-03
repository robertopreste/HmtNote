=======
HmtNote
=======


.. image:: https://img.shields.io/pypi/v/hmtnote.svg
        :target: https://pypi.python.org/pypi/hmtnote

.. image:: https://travis-ci.com/robertopreste/HmtNote.svg?token=zzk3yyGKDnWjk4pFXFuz&branch=master
    :target: https://travis-ci.com/robertopreste/HmtNote

.. image:: https://circleci.com/gh/robertopreste/HmtNote.svg?style=svg&circle-token=b910c3491e8df21fee34293ace05a35a116759c7
    :target: https://circleci.com/gh/robertopreste/HmtNote

.. image:: https://readthedocs.org/projects/hmtnote/badge/?version=latest
        :target: https://hmtnote.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/robertopreste/hmtnote/shield.svg
     :target: https://pyup.io/repos/github/robertopreste/hmtnote/
     :alt: Updates


Human mitochondrial variants annotation using HmtVar. 


* Free software: MIT license
* Documentation: https://hmtnote.readthedocs.io.


Features
--------

HmtNote is a command line tool that can be used to annotate human mitochondrial variants from a VCF, using data available on HmtVar_.

Annotations are grouped into basic, cross-reference, variability and predictions, and include:

* basic: Basic information about the variant
    - Locus: Locus to which the variant belongs
    - AaChange: Aminoacidic change determined
    - Pathogenicity: Pathogenicity predicted by HmtVar
    - Disease Score: Disease score calculated by HmtVar
* cross-reference: Cross-reference information
    - Clinvar: Clinvar ID of the variant
    - dbSNP: dbSNP ID of the variant
    - OMIM: OMIM ID of the variant
    - MitomapAssociatedDiseases: Diseases associated to the variant according to Mitomap Associated Diseases
    - MitomapSomaticMutations: Diseases associated to the variant according to Mitomap Somatic Mutations
* variability: Variability and allele frequency data
    - NtVarH: Nucleotide variability of the position in healthy individuals
    - NtVarP: Nucleotide variability of the position in patient individuals
    - AaVarH: Aminoacid variability of the position in healthy individuals
    - AaVarP: Aminoacid variability of the position in patient individuals
    - AlleleFreqH: Allele frequency of the variant in healthy individuals overall
    - AlleleFreqP: Allele frequency of the variant in patient individuals overall
    - AlleleFreqH_AF: Allele frequency of the variant in healthy individuals from Africa
    - AlleleFreqP_AF: Allele frequency of the variant in patient individuals from Africa
    - AlleleFreqH_AM: Allele frequency of the variant in healthy individuals from America
    - AlleleFreqP_AM: Allele frequency of the variant in patient individuals from America
    - AlleleFreqH_AS: Allele frequency of the variant in healthy individuals from Asia
    - AlleleFreqP_AS: Allele frequency of the variant in patient individuals from Asia
    - AlleleFreqH_EU: Allele frequency of the variant in healthy individuals from Europe
    - AlleleFreqP_EU: Allele frequency of the variant in patient individuals from Europe
    - AlleleFreqH_OC: Allele frequency of the variant in healthy individuals from Oceania
    - AlleleFreqP_OC: Allele frequency of the variant in patient individuals from Oceania
* predictions: Prediction information from external resources
    - MutPred_Prediction: Pathogenicity prediction offered by MutPred
    - MutPred_Probability: Confidence of the pathogenicity prediction offered by MutPred
    - Panther_Prediction: Pathogenicity prediction offered by Panther
    - Panther_Probability: Confidence of the pathogenicity prediction offered by Panther
    - PhDSNP_Prediction: Pathogenicity prediction offered by PhD SNP
    - PhDSNP_Probability: Confidence of the pathogenicity prediction offered by PhD SNP
    - SNPsGO_Prediction: Pathogenicity prediction offered by SNPs & GO
    - SNPsGO_Probability: Confidence of the pathogenicity prediction offered by SNPs & GO
    - Polyphen2HumDiv_Prediction: Pathogenicity prediction offered by Polyphen2 HumDiv
    - Polyphen2HumDiv_Probability: Confidence of the pathogenicity prediction offered by Polyphen2 HumDiv
    - Polyphen2HumVar_Prediction: Pathogenicity prediction offered by Polyphen2 HumVar
    - Polyphen2HumVar_Probability: Confidence of the pathogenicity prediction offered by Polyphen2 HumVar

Usage
-----

HmtNote can be used as a command line tool, by simply providing the original VCF and the filename where the annotated VCF will be saved::

    hmtnote input_vcf.vcf annotated_vcf.vcf

By default, HmtNote will annotate the VCF using all four groups of annotations (basic, cross-reference, variability and predictions). If desired, you can specify which kind of annotation you want, using respectively ``--basic``, ``--crossref``, ``--variab`` and ``--predict``::

    hmtnote input_vcf.vcf annotated_basic_vcf.vcf --basic
    hmtnote input_vcf.vcf annotated_crossreferences_vcf.vcf --crossref
    hmtnote input_vcf.vcf annotated_variability_vcf.vcf --variability
    hmtnote input_vcf.vcf annotated_predictions_vcf.vcf --predict

Credits
-------

This package was created with Cookiecutter_ and the `cc-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cc-pypackage`: https://github.com/robertopreste/cc-pypackage
.. _HmtVar: https://www.hmtvar.uniba.it
