=====
Usage
=====

Command Line Interface
----------------------

HmtNote can be used as a command line tool, by simply providing the original VCF and the filename where the annotated VCF will be saved::

    hmtnote input_vcf.vcf annotated_vcf.vcf

By default, HmtNote will annotate the VCF using all four groups of annotations (basic, cross-reference, variability and predictions). If desired, you can specify which kind of annotation you want, using respectively ``--basic``, ``--crossref``, ``--variab`` and ``--predict`` (or ``-b``, ``-c``, ``-v``, ``-p``)::

    hmtnote input_vcf.vcf annotated_basic_vcf.vcf --basic
    hmtnote input_vcf.vcf annotated_crossreferences_vcf.vcf --crossref
    hmtnote input_vcf.vcf annotated_variability_vcf.vcf --variability
    hmtnote input_vcf.vcf annotated_predictions_vcf.vcf --predict

Python Module
-------------

HmtNote can also be imported in a Python script and its function ``annotate_vcf()`` can be used to annotated a given VCF::

    from hmtnote import annotate_vcf
    annotate_vcf("input_vcf.vcf", "annotated_vcf.vcf")

By default, ``annotate_vcf()`` will annotate the VCF using all four groups of annotations (basic, cross-reference, variability and predictions). If desired, you can specify which kind of annotation you want, using respectively the ``basic=True``, ``crossref=True``, ``variab=True``, ``predict=True`` arguments::

    annotate_vcf("input_vcf.vcf", "annotated_basic_vcf.vcf", basic=True)
    annotate_vcf("input_vcf.vcf", "annotated_crossreferences_vcf.vcf", crossref=True)
    annotate_vcf("input_vcf.vcf", "annotated_variability_vcf.vcf", variab=True)
    annotate_vcf("input_vcf.vcf", "annotated_predictions_vcf.vcf", predict=True)
