=======
History
=======

0.1.0 (2019-03-03)
------------------

* First release on PyPI.


0.1.1 (2019-03-04)
==================

* Clean installation requirements for conda;
* Update documentation.


0.1.2 (2019-03-15)
==================

* Classes and methods are protected where needed;
* Code style is clean.


0.1.3 (2019-03-17)
==================

* Fix issue with `--predict` annotation, which didn't retrieve the correct field from HmtVar.


0.1.4 (2019-03-19)
==================

* Fix issue that prevented importing `annotate_vcf()` into Python scripts.


0.1.5 (2019-03-20)
==================

* Add HmtVar ID of the variant in basic and full annotation;
* Change `Disease Score` annotation to `DiseaseScore`.


0.2.0 (2019-03-25)
------------------

* Add warnings to ``hmtnote`` command to be compliant with future versions;
* Check internet connection before trying to annotate variants.


0.3.0 (2019-03-27)
------------------

* Add options to download the annotation database locally;
* Use local database to annotate variants (instead of calling HmtVar's API);
* Fallback to using local database when no internet connection is available;
* Check if local database actually exists before performing offline annotation;
* Databases are downloaded asynchronously.


0.3.1 (2019-03-29)
==================

* Update installation requirements and documentation.


0.4.0 (2019-04-03)
------------------

* Add support for insertion and deletion annotations;
* Add test suite and files for indels.


0.5.0 (2019-04-28)
------------------

* Replace VCF parsing using VCFpy instead of cyvcf2;
* Rename ``hmtnote.annotate_vcf()`` to ``hmtnote.annotate()`` for compliance with CLI.


0.5.1 (2019-04-29)
------------------

* Fix issue with the new VCFpy implementation where new info where badly reported;
* Update test files restricting the number of entries to 80 for faster testing.
