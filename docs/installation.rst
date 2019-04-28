============
Installation
============

**PLEASE NOTE: HmtNote only supports Python 3!**

Stable release
--------------

To install HmtNote, run this command in your terminal:

.. code-block:: console

    $ pip install hmtnote

This is the preferred method to install HmtNote, as it will always install the most recent stable
release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/

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

    $ cd HmtNote/
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
