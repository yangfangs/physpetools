
.. image:: https://travis-ci.org/MacHu-GWU/elementary_math-project.svg?branch=master

.. image:: https://img.shields.io/pypi/v/elementary_math.svg

.. image:: https://img.shields.io/pypi/l/elementary_math.svg

.. image:: https://img.shields.io/pypi/pyversions/elementary_math.svg



Documentation of one command auto construct species phylogenetic tree
==============================================================================

Introduction
------------------------------------------------------------------------------
In some filed combine species phylogenetic tree do some prediction are very important for instance,
protein-protein interactions and gene pathway members prediction. In this predicted construct a exact species phylogenetic tree
is necessary,but the process of constructing the tree species is very tedious.

we developing a command line software **physpe**,which only one command line to construct species phylogenetic tree,User only need to provide a contain species names files
(the species names must be a abbreviation same with **KEGG DATABASE** organisms abbreviation), the **physpe** auto construct species
phylogenetic tree.

Features
--------------------------------------------------------------------------------
- Easy to use(one command line auto construct phylogenetic tree)

- Multi-selection(selection construct phylogenetic tree by highly conversion protein or 16s RNA)

- Adjustable parameters(User can choice any parameters by own)

- Only provide a species list



Install
-------------------------------------------------------------------------------

1.``physpe`` is released on PyPI, so all you need install:

.. code-block:: console

	$ pip install physpe

To upgrade to latest version:

.. code-block:: console

	$ pip install --upgrade physpe

2.You can install ``physpe`` by download the latest released version:

- Download latest released version **.tar.gz** file　`download <https://gitlab.com/xiaoxiaoyang/physpetools/tags>`_.

- Local installation:

.. code-block:: console

	$ pip install physpetools-v*.tar.gz

3.Use git command:

.. code-block:: console

	$ git clone git@gitlab.com:xiaoxiaoyang/physpetools.git

.. code-block:: console

	$ cd physpetools

.. code-block:: console

	$ python setup.py install

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



