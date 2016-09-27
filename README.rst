One command line auto reconstruct phylogenetic tree
==============================================================================

|PyPI version| |Docs| |License|


**Documents**: `Physpetools documentation <https://xiaofeiyangyang.github.io/physpetools>`_.

.. contents:: :local:


Introduction
------------------------------------------------------------------------------
In some filed combine species phylogenetic tree do some prediction are very important for instance,
protein-protein interactions and gene pathway members prediction. In this predicted construct a exact species phylogenetic tree
is necessary, but the process of constructing the tree species is very tedious.

We developing a command line software **PhySpeTree**, which only one command line to construct species phylogenetic tree. User need to provide a txt files, witch contain species names only.
(the species names must be a abbreviation same with **KEGG database** organisms abbreviation), the **PhySpeTree** auto reconstruct species phylogenetic tree.

PhySpeTree workflow
----------------------------------------------------------------------------

.. image:: https://raw.githubusercontent.com/xiaofeiyangyang/physpetools/master/examples/physpe2.png


PhySpeTree workflow includes the following steps:

1. Prepare organisms names to reconstruct phylogenetic tree as `example <https://raw.githubusercontent.com/xiaofeiyangyang/physpetools/master/examples/organism_example_list.txt>`_.

2. Choice the way to reconstruct phylogenetic tree, use 16s RNA or Highly conversion proteins.

3. Query database and parse retrieve fasta format files.

4. Do multiple sequence alignment by call Muscle.

5. Concatenate conserved proteins by PhySpeTree.

6. Select conserved blocks by Call Gblosks.

7. Reconstructing phylogenetic tree by Call RAxML.

8. Output reconstruct phylogenetic tree files.



Features
--------------------------------------------------------------------------------
- Easy to use (one command line auto construct phylogenetic tree).

- Multi-selection (selection construct phylogenetic tree by highly conversion protein or 16s RNA).

- Adjustable parameters (user can choice any enable parameters by own).

- User need provide a species list (reconstruct phylogenetic tree organisms) only.

- combine best phylogenetic tree (combine multiple tree to a consensus tree)

- view tree by iTol (easy use iview module to view tree)


Install
-------------------------------------------------------------------------------

1. **PhySpeTree** is released on PyPI, so all you need install:

.. code-block:: console

	$ pip install PhySpeTree

To upgrade to latest version:

.. code-block:: console

	$ pip install --upgrade PhySpeTree



2. Download PhySpeTree released version form PypI:

- `Download by PypI <https://pypi.python.org/pypi/PhySpeTree/>`_ latest released version

- local installation:

.. code-block:: console

    $pip install PhySpeTree-*.tar.gz

3. You can install **PhySpeTree** by download the latest released version:

- `Download <https://github.com/xiaofeiyangyang/physpetools/releases>`_ latest released version **.tar.gz** file.

- Local installation:

.. code-block:: console

	$ pip install physpetools-v*.tar.gz

4. Use git command clone **PhySpeTree**:

.. code-block:: console

	$ git clone git@github.com:xiaofeiyangyang/physpetools.git

.. code-block:: console

	$ cd physpetools

.. code-block:: console

	$ python setup.py install

Usage
-------------------------------------------------------------------------------

autobuild
^^^^^^^^^^^^^^^^^^^^

User should prepare a txt file contain the abbreviation names of organisms `example <https://raw.githubusercontent.com/xiaofeiyangyang/physpetools/master/examples/organism_example_list.txt>`_.

Use **autobuild** in command line like this:

.. code-block:: console

    $ PhySpeTree -i organism_example_list.txt [options]*


autobuild options
#####################

-h
    Print help message and exits.

-i
    Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation.

-o
    A directory include output data (reconstruct tree files). The default output data name is Outdata.

-t
    Specify the number of processing threads (CPUs) to use for PhySpeTree to reconstruct phylogenetic tree. The default is 1.

--hcp

    The hcp (highly conserved protein) mode is use conserved proteins to reconstruct phylogenetic tree. The default mode is hcp.

--ehcp

    The ehcp (highly conserved protein) mode is use highly conserved proteins and extend highly protein (user provide) to reconstruct phylogenetic tree.

--srna

    The 16srna (16 ssu RNA) mode is use 16s RNA data to reconstruct phylogenetic tree.

--esrna

    The 16srna (16 SSU RNA) mode is use 16s SSU RNA data and extend 16s SSU RNA (user provide) to reconstruct phylogenetic tree.


Advance options
#####################

User enable choice more detail options with PhySpeTree call software, detail advance options input
``must be enclosed in single quotes``.

The follow is to use RAxML advance options example:

.. code-block:: console

    $ PhySpeTree -i organism_example_list.txt --raxml --raxml_p '-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1'

--muscle
    Multiple sequence alignment by muscle. The default aligned software is Muscle.


--muscle_p
    Set multiple sequence alignment parameters. The default is ``-maxiter 100``. More options about muslce please to see
    `MUSCLE Manual <http://www.drive5.com/muscle/manual/options.html>`_.

    -maxiter
        maximum number of iterations to run is set 100.
--clustalw
    Multiple sequense alignment by clustalw2.

--clustalw_p
    Set more detail clustalw2 parameters. Here use clustalw default parameters. More options about clustalw
    please to see `Clustalw Help <http://www.clustal.org/download/clustalw_help.txt>`_.


--gblocks
    Set Gblocks parameters. The default is ``-t=p -e=-gb1``.
    More options about Gblocks please to see
    `Gblocks documentation <http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_documentation.html>`_.

    -t
        Choice type of sequence. The PhySpeTree default set is protein.

    -e
        Eneric file extensionc. physep set default is -gbl1.


--raxml
    Reconstruct phylogenetic tree by RAxML. The default build tree software is RAxML.

--raxml_p
    Set reconstruct phylogenetic tree arguments with RAxML. The default is ``-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1``.
    More options about RAxMl please to see `RAxML Manual <http://sco.h-its.org/exelixis/resource/download/NewManual.pdf>`_.

    -f
        select algorithm. The PhySpeTree default set is ``a``, rapid Bootstrap analysis and search for best­scoring ML tree in one program run.

    -m
        Model of Binary (Morphological), Nucleotide, Multi­State, or Amino Acid Substitution. The PhySpeTree default set is PROTGAMMAJTTX.

    -p
        Specify a random number seed for the parsimony inferences. The physep default set is 12345.

    -x
        Specify an integer number (random seed) and turn on rapid bootstrapping. The PhySpeTree default set is 12345.

    -N
        The same with -# specify the number of alternative runs on distinct starting trees. The PhySpeTree default set is 100.


--fasttree
    Reconstruct phylogenetic tree by FastTree.

--fasttree_p
    Set more detail RAxML parameters.More options about clustalw
    please to see `FastTree <http://www.microbesonline.org/fasttree/>`_.

build
^^^^^^^^^^^^^^^^^^^^

User can build tree by own 16s rna data or highly conserved proteins.

Use **build** in command line to reconstruct phylogenetic tree:

* build phylogenetic tree by highly conserved proteins


.. code-block:: console

    $ PhySpeTree build -i example_hcp -o output --hcp


* build phylogenetic tree by 16s ssu rna data


.. code-block:: console

    $ PhySpeTree build -i example_16s_ssurna.fasta -o output --sran

build options
#####################

-h
    Print help message and exits.

-i
    Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation.

-o
    A directory include output data (reconstruct tree files). The default output data name is Outdata.

-t
    Specify the number of processing threads (CPUs) to use for PhySpeTree to reconstruct phylogenetic tree. The default is 1.

--hcp

    The hcp (highly conserved protein) mode is use conserved proteins to reconstruct phylogenetic tree. The default mode is hcp.

--ehcp

    The ehcp (highly conserved protein) mode is use highly conserved proteins and extend highly protein (user provide) to reconstruct phylogenetic tree.

--srna

    The 16srna (16 ssu RNA) mode is use 16s RNA data to reconstruct phylogenetic tree.

--esrna

    The 16srna (16 SSU RNA) mode is use 16s SSU RNA data and extend 16s SSU RNA (user provide) to reconstruct phylogenetic tree.



Advance options
#####################

User enable choice more detail options with PhySpeTree call software, detail advance options input
``must be enclosed in single quotes``.

The follow is to use RAxML advance options example:

.. code-block:: console

    $ PhySpeTree -i organism_example_list.txt --raxml --raxml_p '-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1'

--muscle
    Multiple sequence alignment by muscle. The default aligned software is Muscle.


--muscle_p
    Set multiple sequence alignment parameters. The default is ``-maxiter 100``. More options about muslce please to see
    `MUSCLE Manual <http://www.drive5.com/muscle/manual/options.html>`_.

    -maxiter
        maximum number of iterations to run is set 100.
--clustalw
    Multiple sequense alignment by clustalw2.

--clustalw_p
    Set more detail clustalw2 parameters. Here use clustalw default parameters. More options about clustalw
    please to see `Clustalw Help <http://www.clustal.org/download/clustalw_help.txt>`_.


--gblocks
    Set Gblocks parameters. The default is ``-t=p -e=-gb1``.
    More options about Gblocks please to see
    `Gblocks documentation <http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_documentation.html>`_.

    -t
        Choice type of sequence. The PhySpeTree default set is protein.

    -e
        Eneric file extensionc. physep set default is -gbl1.


--raxml
    Reconstruct phylogenetic tree by RAxML. The default build tree software is RAxML.

--raxml_p
    Set reconstruct phylogenetic tree arguments with RAxML. The default is ``-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1``.
    More options about RAxMl please to see `RAxML Manual <http://sco.h-its.org/exelixis/resource/download/NewManual.pdf>`_.

    -f
        select algorithm. The PhySpeTree default set is ``a``, rapid Bootstrap analysis and search for best­scoring ML tree in one program run.

    -m
        Model of Binary (Morphological), Nucleotide, Multi­State, or Amino Acid Substitution. The PhySpeTree default set is PROTGAMMAJTTX.

    -p
        Specify a random number seed for the parsimony inferences. The physep default set is 12345.

    -x
        Specify an integer number (random seed) and turn on rapid bootstrapping. The PhySpeTree default set is 12345.

    -N
        The same with -# specify the number of alternative runs on distinct starting trees. The PhySpeTree default set is 100.


--fasttree
    Reconstruct phylogenetic tree by FastTree.

--fasttree_p
    Set more detail RAxML parameters.More options about clustalw
    please to see `FastTree <http://www.microbesonline.org/fasttree/>`_.

combine
^^^^^^^^^^^^^^^^^^^^

User should prepare a combine tree file by Combine command to combine tree files.


In Linux you can easy combine more tree to a tree file, for example:

.. code-block:: console

    $ cat tree1.tree tree2.tree > combieTree.tree


Use **combine** in command line like this:

.. code-block:: console

    $ PhySpeTree -i organism_example_list.txt [options]*


combine options
#####################

-h
    Print help message and exits.

-i
    Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation.

-o
    A directory contain combine tree file. The default output data name is combinetree.

iview
^^^^^^^^^^^^^^^^^^^^

Annotating tree by iTol use iview module.


Use **iview** in command line like this:

.. code-block:: console

    $ PhySpeTree iview -i organism_example_list.txt -range phylum


iview options
#####################


-h
    Print help message and exits.

-i
    Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation.

-o
    A directory contain range text file. The directory name is iverw.

-r
    Annotating ranges by kingdom, phylum, class or order. The default is phylum.

-a
    Colored ranges by user assign, user can choice from kingdom phylum class and order.

-l
    Change labels from abbreviation names to full names.

check
^^^^^^^^^^^^^^^^^^^^

Use check module  check input organisms match in kegg database or 16s database


.. code-block:: console

    $ PhySpeTree check -i organism_example_list.txt -out check --ehcp



check options
#####################



-h
    Print help message and exits.

-i
    Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation.

-o
    A directory contain check result. The directory name is check.

--echcp

    check input organisms prepare for extend autobuild tree module.


Frequently Asked Questions (FAQ)
--------------------------------------------------------------------------------

PhySpeTree input/output
^^^^^^^^^^^^^^^^^^^

**1.What preparation of user should does for PhySpeTree?**

User should prepare a list contain organisms names (abbreviation name are same with `KEGG database <http://www.genome.jp/kegg/catalog/org_list.html>`_.),
one line write one species name only such as `organism_example_list <https://gitlab.com/xiaoxiaoyang/physpetools/raw/master/examples/organism_example_list.txt>`_.
You can retrieve the abbreviation names of organisms by `KEGG API <http://rest.kegg.jp/list/organism>`_.


**2.What's PhySpeTree output data mean?**

PhySpeTree output tow data files, the one is contain phylogenetic tree files default names is ``Outdata``, another is a temp file.

If you reconstruct phylogenetic tree by HCP (highly conserved protein) model, temp file include three directory ``conserved_protein``, ``muscle_alignment`` and ``concatenate``
  + conserved_protein: Store the \*.fasta format files, which is conserved proteins retrieve by KEGG database.
  + muscle_alignment: Store files are multiple sequence alignment by muscle.
  + concatenate: Include concatenate highly conserved protein data (\*.fasta format file) and select conserved blocks data (\*.fasta-gb1 format file).

If you reconstruct phylogenetic tree by SRNA (16s RNA) model temp file include two directory ``16srnadata`` and ``16srna_alignment``.
  + 16srandata: Stroe  a file name is 16srandata.fata, contain the 16s RNA data retrieve by SILVA database.
  + 16sran_alignment: Store the \*.fasta format is multiple sequence alignment data and the \*.fasta-gb1, \*fasta-gb1.html are select conserved blocks data (use Gblocks software),
    the \*.phy format file is convert to convert from gblok data by PhySpeTree to reconstruct phylogenetic tree.

Users can check the quality of every aspect of data by these temp files.


PhySpeTree reconstruct phylogenetic tree database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**1.what's the highly conserved proteins are PhySpeTree use reconstruct phylogenetic tree?**

PhySpeTree use 31 highly conserved proteins to reconstruct phylogenetic tree. This highly conserved proteins exclusion Horizontal Gene Transfers (HGTs) already.

**cite:**

 Ciccarelli F D, Doerks T, Von Mering C, et al. Toward automatic reconstruction of a highly resolved tree of life[J]. science, 2006, 311(5765): 1283-1287.

31 highly conserved proteins and correspond KEGG database KO number as follow table:


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
Ribosomal protein S15P/S13E                            K02958              K02956
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

The 16s RAN database was created by `SILVA <https://www.arb-silva.de/>`_ rRNA database project (version: SILVA SSU 123.1 release)
with sequences haven been truncated. Means that all nucleotides that have not been aligned were removed from the sequence.



.. |PyPI version| image:: https://img.shields.io/pypi/v/PhySpeTree.svg?style=flat-square
   :target: https://pypi.python.org/pypi/PhySpeTree
.. |Docs| image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat-square
   :target: https://xiaofeiyangyang.github.io/physpetools/
.. |License| image:: https://img.shields.io/aur/license/yaourt.svg?maxAge=2592000
   :target: https://github.com/xiaofeiyangyang/physpetools/blob/master/LICENSE.txt