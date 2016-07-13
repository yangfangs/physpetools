
.. image:: https://travis-ci.org/MacHu-GWU/elementary_math-project.svg?branch=master

.. image:: https://img.shields.io/pypi/v/elementary_math.svg

.. image:: https://img.shields.io/pypi/l/elementary_math.svg

.. image:: https://img.shields.io/pypi/pyversions/elementary_math.svg



Welcome to one command auto construct species phylogenetic tree Documentation
==============================================================================
The physpe is a python command line software. Users only need to provide a list file,
which contain the name of the species,the species names must be a abbreviation same with KEGG DATABASE.


Install
-------------------------------------------------------------------------------

``physpe`` is released on PyPI, so all you need install:

.. code-block:: console

	$ pip install physpe

To upgrade to latest version:

.. code-block:: console

	$ pip install --upgrade physpe


Usage
-------------------------------------------------------------------------------

.. code-block:: console

    $ physpe - in organismlist.txt -out ~/phytree/outfile

Options
-------------------------------------------------------------------------------
``-in``  A txt file contain the a abbreviation species name same with KEGG species abbreviation.

``-out`` A directory contain construct Tree files.

``-v`` The version information.

``-t`` Set the threads to construct phylogenetic tree. The default is 1.



Advance options
--------------------------------------------------------------------------------

``-muscle``  Set multiple sequence alignment arguments. The default is ``-maxiter 100``

``-gblocks`` Set gblocks arguments. The default is ``-t=p -e=-gb1``

``-raxml``   Set reconstruct phylogenetic tree arguments the detail see RAxML software arguments. The default is
             ``-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1``



