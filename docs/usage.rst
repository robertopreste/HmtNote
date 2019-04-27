=====
Usage
=====

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

HmtNote will look for data in the dumped database, which was saved as ``hmtnote_dump.pkl``, to perform annotations.
**PLEASE NOTE: when working in *online mode*, HmtNote will retrieve from HmtVar only those entries that correspond to variants contained in the input VCF file; the ``dump`` command, instead, downloads the entire HmtVar database (actually just the subset used by HmtNote) to the local disk.** Although this local database is not bigger than a few dozen MB, the download process may take a while.

**PLEASE NOTE: data in HmtVar is subject to frequent updates, so please remember to run ``hmtnote dump`` as frequently as possible to be sure you're working with the latest data.** Use the *offline mode* at your own risk.

Python Module
=============

HmtNote can also be imported in a Python script and its function ``annotate_vcf()`` can be used to annotate a given VCF::

    from hmtnote import annotate_vcf
    annotate("input.vcf", "annotated.vcf")

By default, ``annotate_vcf()`` will annotate the VCF using all four groups of annotations (basic, cross-reference, variability and predictions). If desired, you can specify which kind of annotation you want, using respectively the ``basic=True``, ``crossref=True``, ``variab=True``, ``predict=True`` arguments, or any combination of them::

    annotate("input.vcf", "annotated_basic.vcf", basic=True)
    annotate("input.vcf", "annotated_crossreferences.vcf", crossref=True)
    annotate("input.vcf", "annotated_variability.vcf", variab=True)
    annotate("input.vcf", "annotated_predictions.vcf", predict=True)
    annotate("input.vcf", "annotate_basic_variability.vcf", basic=True, variab=True)

If you want to work offline, HmtNote offers an *offline mode*, that will download the annotation database so that it can be used when no internet connection is available. The ``dump()`` function allows to download the local HmtNote database::

    from hmtnote import dump
    dump()

Now it is possible to perform offline annotation of VCF files, by simply adding the ``offline=True`` argument to the usual annotation function::

    annotate("input.vcf", "annotated.vcf", offline=True)
    annotate("input.vcf", "annotated_variability.vcf, variab=True, offline=True)

Please read above for potential limitations of the *offline mode*.

Annotations
-----------

HmtNote offers several annotations, grouped for simplicity into basic, cross-reference, variability and predictions, depending on the type of information they provide.

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
