============
Installation
============


Stable release
--------------

To install HmtNote, run this command in your terminal:

.. code-block:: console

    $ pip install hmtnote

This is the preferred method to install HmtNote, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

Should you have issues with the installation process, you should first make sure you have pyOpenSSL_ and Cython installed (otherwise you can ``pip install pyOpenSSL Cython``, and then you should export the following environment variables in your shell, before launching the ``pip install hmtnote`` command::

    LDFLAGS = "-L/usr/local/opt/openssl/lib"
    CPPFLAGS = "-I/usr/local/opt/openssl/include"
    PKG_CONFIG_PATH = "/usr/local/opt/openssl/lib/pkgconfig"
    LC_ALL = "en_US.UTF-8"
    LANG = "en_US.UTF-8"

Please refer to the details of your shell to check the right way to export environment variables.

In case you still have issues with the installation, please read below how to install HmtNote from sources.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/
.. _pyOpenSSL: https://pyopenssl.org/en/stable/


From sources
------------

The sources for HmtNote can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/robertopreste/HmtNote

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/robertopreste/HmtNote/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/robertopreste/HmtNote
.. _tarball: https://github.com/robertopreste/HmtNote/tarball/master
