============
Installation
============

**PLEASE NOTE: HmtNote only supports Python 3!**

Stable release
--------------

The recommended way of installing HmtNote is in a conda environment, which seems to better manage
one of the core dependencies of HmtNote (namely the `cyvcf2` module):

.. code-block:: console

    $ conda create -n HmtNote
    $ conda activate HmtNote
    $ conda install requests
    $ conda install -c bioconda cyvcf2

And then to install HmtNote, run this command in your terminal:

.. code-block:: console

    $ pip install hmtnote

This is the preferred method to install HmtNote, as it will always install the most recent stable
release.

Should you have issues with the installation process, there are a few tricks you can try.

* If the error message mentions a `gcc` issue, you can install it using ``apt install gcc`` (this command works on Ubuntu, please check your distribution's documentation for details); then retry ``pip install hmtnote``.

* If still failing, try ``apt install zlib1g-dev`` and then ``pip install hmtnote``.

* If the installations still fails, you should first make sure you have pyOpenSSL_ installed (otherwise you can ``pip install pyOpenSSL``), and then you should export the following environment variables in your shell, before launching the ``pip install hmtnote`` command again::

    LDFLAGS = "-L/usr/local/opt/openssl/lib"
    CPPFLAGS = "-I/usr/local/opt/openssl/include"
    PKG_CONFIG_PATH = "/usr/local/opt/openssl/lib/pkgconfig"
    LC_ALL = "en_US.UTF-8"
    LANG = "en_US.UTF-8"

Please refer to the details of your shell to check the right way to export environment variables.

In case you still have issues with the installation, please read below how to install HmtNote from
sources.

.. _pyOpenSSL: https://pyopenssl.org/en/stable/


From sources
------------

The sources for HmtNote can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone https://github.com/robertopreste/HmtNote

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/robertopreste/HmtNote/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install

If you have issues with this installation, try creating a new conda environment from the given
`environment.yml` file:

.. code-block:: console

    $ conda env create -f environment.yml

This command should create a conda env called HmtNote, which contains the requirements for HmtNote.
You can then activate this environment and install HmtNote:

.. code-block:: console

    $ conda activate HmtNote
    $ pip install HmtNote

If none of these methods works for you, please feel free to open an issue_ on GitHub, and I'll be happy to help.

.. _Github repo: https://github.com/robertopreste/HmtNote
.. _tarball: https://github.com/robertopreste/HmtNote/tarball/master
.. _issue: https://github.com/robertopreste/HmtNote/issues
