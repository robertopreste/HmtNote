=======
HmtNote
=======


.. image:: https://img.shields.io/pypi/v/hmtnote.svg
        :target: https://pypi.python.org/pypi/hmtnote

.. image:: https://www.repostatus.org/badges/latest/wip.svg
        :alt: Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
        :target: https://www.repostatus.org/#wip

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

.. image:: https://pepy.tech/badge/hmtnote
        :target: https://pepy.tech/project/hmtnote
        :alt: Downloads

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/robertopreste

Human mitochondrial variants annotation using HmtVar.


* Free software: MIT license
* Documentation: https://hmtnote.readthedocs.io
* GitHub repo: https://github.com/robertopreste/HmtNote
* Publication: https://doi.org/10.1101/600619


Features
--------

HmtNote is a bioinformatics Python module and command line interface that can be used to annotate human mitochondrial variants from a VCF file, using data available on HmtVar_.

Annotations are grouped into basic, cross-reference, variability and predictions, depending on the type of information they provide. It is possible to either use all of them to fully annotate a VCF file, or choose specific annotations of interest.

HmtNote works by pulling the required data from HmtVar_ on the fly, but if you're planning to annotate VCF files offline, it is possible to download the annotation database so that HmtNote can use it when no internet connection is available.

For more information, please refer to the Usage_ section of the documentation.


Installation
------------

**PLEASE NOTE: HmtNote only supports Python 3!**

The preferred installation method for HmtNote is using ``pip``:

.. code-block:: console

    $ pip install hmtnote

For more information, please refer to the Installation_ section of the documentation.


Usage
-----

Command Line Interface
======================

HmtNote can be used as a command line tool, using the ``annotate`` command and providing the input VCF file name and the file name or path where the annotated VCF will be saved::

    hmtnote annotate input.vcf annotated.vcf

By default, HmtNote will annotate the VCF file using all four groups of annotations (basic, cross-reference, variability and predictions). If desired, you can select which specific annotation you want, using respectively ``--basic``, ``--crossref``, ``--variab`` and ``--predict`` (or ``-b``, ``-c``, ``-v``, ``-p``), or any combination of these options::

    hmtnote annotate input.vcf annotated_basic.vcf --basic
    hmtnote annotate input.vcf annotated_crossreferences.vcf --crossref
    hmtnote annotate input.vcf annotated_variability.vcf --variab
    hmtnote annotate input.vcf annotated_predictions.vcf --predict
    hmtnote annotate input.vcf annotate_basic_variability.vcf --basic --variab

By default, HmtNote works by pulling the required data from HmtVar_ on the fly, but if you're planning to annotate VCF files offline, first download the annotation database using the ``dump`` command::

    hmtnote dump

After that, HmtNote is capable of working even when no internet connection is available; this can be achieved using the ``--offline`` option after the usual annotation command::

    hmtnote annotate input.vcf annotated.vcf --offline
    hmtnote annotate input.vcf annotated_variability.vcf --variab --offline

For more information, please refer to the Usage_ section of the documentation.

Python Module
=============

HmtNote can also be imported in a Python script and its function ``annotate_vcf()`` can be used to annotate a given VCF::

    from hmtnote import annotate
    annotate("input.vcf", "annotated.vcf")

By default, ``annotate_vcf()`` will annotate the VCF using all four groups of annotations (basic, cross-reference, variability and predictions). If desired, you can specify which kind of annotation you want, using respectively the ``basic=True``, ``crossref=True``, ``variab=True``, ``predict=True`` arguments, or any combination of them::

    annotate("input.vcf", "annotated_basic.vcf", basic=True)
    annotate("input.vcf", "annotated_crossreferences.vcf", crossref=True)
    annotate("input.vcf", "annotated_variability.vcf", variab=True)
    annotate("input.vcf", "annotated_predictions.vcf", predict=True)

It is also possible to download the annotation database using the ``dump()`` function, and perform offline annotation of VCF files by simply adding the ``offline=True`` argument to ``annotate_vcf()``::

    from hmtnote import dump
    dump()
    annotate("input.vcf", "annotated.vcf", offline=True)

For more information, please refer to the Usage_ section of the documentation.

Citing HmtNote
--------------

If you find HmtNote useful for your research, please cite this work:

    Preste R. *et al* - Human mitochondrial variant annotation with HmtNote (doi: https://doi.org/10.1101/600619)

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
.. _Installation: https://hmtnote.readthedocs.io/en/latest/installation.html
.. _Usage: https://hmtnote.readthedocs.io/en/latest/usage.html
