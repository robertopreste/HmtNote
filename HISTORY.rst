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


0.2.0 (WIP)
===========

* Add options to download the required databases locally;
* Use local databases to annotate variants (instead of calling HmtVar's API);
* Fallback to using local databases when web connection is not available;
* Check if local databases actually exist before performing offline annotation;
* Database download is performed with async.
