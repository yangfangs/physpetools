
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

Physpe workflow
----------------------------------------------------------------------------

.. image:: https://gitlab.com/xiaoxiaoyang/physpetools/raw/master/examples/physpe.png


Physpe workflow includes the following steps:

- Prepare organisms name to reconstruct phylogenetic tree as example `download <https://gitlab.com/xiaoxiaoyang/physpetools/raw/master/examples/organism_example_list.txt>`_.

- Choice the way to reconstruct phylogenetic tree, use 16s RNA or Highly conversion proteins

- Query database and parse retrieve fasta file

- Do multiple sequence alignment by call Muscle

- Concatenate conserved proteins by physpe

- Select conserved blocks by Call Gblosks

- Reconstructing phylogenetic tree by Call RAxML

- Output phylogenetic tree files



Features
--------------------------------------------------------------------------------
- Easy to use(one command line auto construct phylogenetic tree)

- Multi-selection(selection construct phylogenetic tree by highly conversion protein or 16s RNA)

- Adjustable parameters(User can choice any parameters by own)

- Only provide a species list



Install
-------------------------------------------------------------------------------

1. **physpe** is released on PyPI, so all you need install:

.. code-block:: console

	$ pip install physpe

To upgrade to latest version:

.. code-block:: console

	$ pip install --upgrade physpe

2. You can install **physpe** by download the latest released version:

- Download latest released version **.tar.gz** file　`download <https://gitlab.com/xiaoxiaoyang/physpetools/tags>`_.

- Local installation:

.. code-block:: console

	$ pip install physpetools-v*.tar.gz

3. Use git command clone **physpe**:

.. code-block:: console

	$ git clone git@gitlab.com:xiaoxiaoyang/physpetools.git

.. code-block:: console

	$ cd physpetools

.. code-block:: console

	$ python setup.py install

Usage
-------------------------------------------------------------------------------

User should prepare a txt file contain the abbreviation names of organisms example `download <https://gitlab.com/xiaoxiaoyang/physpetools/raw/master/examples/organism_example_list.txt>`_.



.. code-block:: console

    $ physpe -in organism_example_list.txt -out phytree

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


Frequently Asked Questions (FAQ)
--------------------------------------------------------------------------------

Physpe input/output
-------------------

**1.What preparation of user should does for Physpe?**

User should prepare a list contain organisms names(abbreviation name are same with `KEGG DATABASE <http://www.genome.jp/kegg/catalog/org_list.html>`_.),
one line write one species name only such as `organism_example_list <https://gitlab.com/xiaoxiaoyang/physpetools/raw/master/examples/organism_example_list.txt>`_.
you can retrieve the abbreviation names of organisms by `KEGG API <http://rest.kegg.jp/list/organism>`_.


**2.What's Physpe output data mean?**

Physpe output tow data files one is data files contain phylogenetic tree files default names is ``Outdata``, another is a temp files contain
three directory ``conserved_protein``, ``muscle_alignment`` and ``concatenate``
  + conserved_protein: Store the *.fasta format files, which is conserved proteins retrieve by KEGG DATABASE.
  + muscle_alignment: Store files are multiple sequence alignment by muscle.
  + concatenate: Include concatenate highly conserved protein data(*.fasta format file) and Select conserved blocks data(*.fasta-gb1 format file).
Users can check the quality of every aspect of data by these temp files.


Physpe reconstruct phylogenetic tree DB
----------------------------------------
**1.what's the highly conserved proteins are physpe use reconstruct phylogenetic tree?**

Physpe use 31 highly conserved proteins to reconstruct phylogenetic tree. This highly conserved proteins exclusion Horizontal Gene Transfers (HGTs) already.

**cite:**

 Ciccarelli F D, Doerks T, Von Mering C, et al. Toward automatic reconstruction of a highly resolved tree of life[J]. science, 2006, 311(5765): 1283-1287.

31 highly conserved proteins and correspond KEGG DATABASE KO number as follow table:


====================================================   ==============      ===============
Protein Names                                          Eukaryotes KO       Prokaryotes KO
====================================================   ==============      ===============
DNA-directed RNA polymerase subunit alpha              K03040              K03040
Ribosomal protein L1                                   K02865              K02863
Leucyl-tRNA synthetase                                 K01869              K01869
Metal-dependent proteases with chaperone activity      K01409              K01409
Phenylalanine-tRNA synthethase alpha subunit           K01889              K01889
Predicted GTPase probable translation factor           K06942              K06942
Preprotein translocase subunit SecY                    K10956              K10956
Ribosomal protein L11                                  K02868              K02867
Ribosomal protein L13                                  K02873              K02871
Ribosomal protein L14                                  K02875              K02874
Ribosomal protein L15                                  K02877              K17437
Ribosomal protein L16/L10E                             K02866              K02872
Ribosomal protein L18                                  K02883              K02882
Ribosomal protein L22                                  K02891              K02890
Ribosomal protein L3                                   K02925              K02906
Ribosomal protein L5                                   K02932              K02931
Ribosomal protein L6P/L9E                              K02940              K02939
Ribosomal protein S11                                  K02949              K02948
Ribosomal protein S15P/S13E                            K02956              K02956
Ribosomal protein S17                                  K02962              K02961
Ribosomal protein S2                                   K02981              K02967
Ribosomal protein S3                                   K02985              K02982
Ribosomal protein S4                                   K02987              K02986
Ribosomal protein S5                                   K02989              K02988
Ribosomal protein S7                                   K02993              K02992
Ribosomal protein S8                                   K02995              K02994
Ribosomal protein S9                                   K02997              K02996
Seryl-tRNA synthetase                                  K01875              K01875
Arginyl-tRNA synthetase                                K01887              K01887
DNA-directed RNA polymerase beta subunit               K03043              K03043
Ribosomal protein S13                                  K02953              K02952
====================================================   ==============      ===============



**2.How the 16s RAN database to created?**

16s RAN database created by `SILVA <https://www.arb-silva.de/>`_ rRNA database project, version is SILVA SSU 123.1 release
with Sequences haven been truncated. Means that all nucleotides that have not been aligned were removed from the sequence


