=====
Usage
=====

HmtNote can be used as a command line tool, by simply providing the original VCF and the filename where the annotated VCF will be saved::

    hmtnote input_vcf.vcf annotated_vcf.vcf

By default, HmtNote will annotate the VCF using all four groups of annotations (basic, cross-reference, variability and predictions). If desired, you can specify which kind of annotation you want, using respectively ``--basic``, ``--crossref``, ``--variab`` and ``--predict``::

    hmtnote input_vcf.vcf annotated_basic_vcf.vcf --basic
    hmtnote input_vcf.vcf annotated_crossreferences_vcf.vcf --crossref
    hmtnote input_vcf.vcf annotated_variability_vcf.vcf --variability
    hmtnote input_vcf.vcf annotated_predictions_vcf.vcf --predict
