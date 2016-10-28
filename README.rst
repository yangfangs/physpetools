PhySpeTree: automatically reconstructing phylogenetic species tree
==============================================================================

|PyPI version| |Docs| |License|


**Documents**: `PhySpeTree documentation <https://xiaofeiyangyang.github.io/physpetools>`_.

.. contents:: :local:


Introduction
------------------------------------------------------------------------------
Understanding phylogenetic relationships between different species is crucial for evolutionary studies. Reconstructing the
phylogenetic species tree, a branching diagram, is particularly useful in inferring evolutionary relationships. For example,
the tree-of-life provides a remarkable view of organizing principles of the biological world. So, the exact species tree to
be reconstructed is necessary, but the process of reconstructing the species or gene tree is very tedious.

Here, we developed an easy-to-use package named PhySpeTree that is convenient to reconstruct species trees by one command line.
Two independent pipelines were included by using the most adopted small subunit ribosomal RNA (SSU rRNA) and concatenated highly
conserved proteins (HCP), respectively. A distinct advantage is that users only need to input species names and PhySpeTree
automatically downloads and analyzes sequences of SSU rRNA or HCP from about 4,000 organisms.

PhySpeTree workflow
------------------------------------------------------------------------------

.. image:: https://github.com/xiaofeiyangyang/physpetools/blob/master/docs/docs/img/PhySpeTree_work_follow.png


PhySpeTree workflow includes the following steps:

1. Prepare organisms names (abbreviated name) to reconstruct species tree as `example <https://raw.githubusercontent.com/xiaofeiyangyang/physpetools/master/examples/organism_example_list.txt>`_.

2. Two parallel pipelines to reconstruct species tree (SSU rRNA (--sran) or highly conserved proteins (--hcp)).

3. Querying, parsing and retrieving FASTA format data.

4. Multiple sequence alignment by Muscle or ClustalW.

5. Concatenate highly conserved proteins by PhySpeTree.

6. Select conserved blocks by Gblosks.

7. Reconstruct species tree by RAxML or FastTree.

8. Output the reconstruct phylogenetic tree files.



Features
--------------------------------------------------------------------------------
- Easy to use (one command line automatically reconstruct species tree).

- Multi-selection (select reconstruct species tree by HCP method or SSU rRNA method).

- Adjustable parameters (the users can choice any enable parameters with corresponding invoke software).

- Provide species names (species abbreviated names) as input only.

- Combine best phylogenetic tree (combine multiple tree to a consensus tree).

- View tree by iTol (easily use iview module to annotate tree).

- Flexible (more software to be invoked with corresponding enable parameters).

- Versatile software (can build species tree or gene tree and also ability extend new species to tree).


Install
-------------------------------------------------------------------------------

1. PhySpeTree is released on PyPI, so all you need install:

.. code-block:: console

	$ pip install PhySpeTree

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade PhySpeTree



2. Download PhySpeTree released version form PypI:

- `Download PhySpeTree <https://pypi.python.org/pypi/PhySpeTree/>`_ by PypI latest released version

- local installation:

.. code-block:: console

    $ pip install PhySpeTree-*.tar.gz

3. You can install PhySpeTree by downloading the latest released version form github:

- `Download <https://github.com/xiaofeiyangyang/physpetools/releases>`_ latest released version **.tar.gz** file.

- Local installation:

.. code-block:: console

    $ pip install physpetools-v*.tar.gz

4. Use the git command clone PhySpeTree to install it:

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

Users should prepare a TXT file contain the species names (abbreviated names) `example <https://raw.githubusercontent.com/xiaofeiyangyang/physpetools/master/examples/organism_example_list.txt>`_.

Use **autobuild** in command line like this:

.. code-block:: console

    $ PhySpeTree -i organism_example_list.txt [options]*


autobuild options
#####################

-h
    Print help message and exits.

-i
    Input a TXT file contain the species names (abbreviated names) are same with KEGG species abbreviation.

-o
    A directory include output data (tree files). The default output data name is Outdata.

-t
    Specify the number of processing threads (CPUs) to reconstruct phylogenetic tree. The default is 1.

--hcp

    Specify the hcp (highly conserved protein) method to reconstruct phylogenetic tree. The default method is hcp.

--ehcp

    The ehcp mode is use highly conserved proteins with extend highly conserved protein (users provide) to reconstruct phylogenetic tree.

--srna

    The srna (SSU rRNA) method is use SSU rRNA data to reconstruct phylogenetic tree.

--esrna

    The esrna mode is use SSU RNA sequence with extend SSU RNA sequence (users provide) to reconstruct phylogenetic tree.


Advance options
#####################

Users enable choice more detail options with PhySpeTree call software, detail advance options input
``must be enclosed in single quotes``.

The following is an example of using RAxML advanced options:

.. code-block:: console

    $ PhySpeTree -i organism_example_list.txt --raxml --raxml_p '-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1'

--muscle
    Multiple sequence alignment by muscle. The default multiple sequence alignment software is Muscle.


--muscle_p
    Set Muscle advance parameters. The default is ``-maxiter 100``. More options about Muscle please to see
    `MUSCLE Manual <http://www.drive5.com/muscle/manual/options.html>`_.

    -maxiter
        maximum number of iterations to run is set 100.

--clustalw
    Multiple sequence alignment by clustalw2.

--clustalw_p
    Set clustalw2 advance parameters. Here use clustalw default parameters. More options about clustalw
    please to see `Clustalw Help <http://www.clustal.org/download/clustalw_help.txt>`_.


--gblocks
    Set Gblocks advance parameters. The default is ``-t=p -e=-gb1``.
    More options about Gblocks please to see
    `Gblocks documentation <http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_documentation.html>`_.

    -t
        Choice type of sequence. The PhySpeTree default set is protein.

    -e
        Eneric file extensionc. PhySpeTree set default is -gbl1.


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
    Set FastTree advance parameters. More options about clustalw
    please to see `FastTree <http://www.microbesonline.org/fasttree/>`_.

build
^^^^^^^^^^^^^^^^^^^^

Users can reconstruct phylogenetic tree use `build` module by manually prepared files. such as, SSU rRNA sequence or highly conserved proteins.

Use **build** in command line to reconstruct phylogenetic tree:

* build phylogenetic tree by highly conserved proteins method:


.. code-block:: console

    $ PhySpeTree build -i example_hcp -o output --hcp


* build phylogenetic tree by SSU rRNA sequence method:


.. code-block:: console

    $ PhySpeTree build -i example_16s_ssurna.fasta -o output --sran

build options
#####################

-h
    Print help message and exits.

-i
    Input a TXT file contain the species names (abbreviated names) are same with KEGG species abbreviation.

-o
    A directory include output data (tree files). The default output data name is Outdata.

-t
    Specify the number of processing threads (CPUs) to reconstruct phylogenetic tree. The default is 1.

--hcp

    Specify the hcp (highly conserved protein) method to reconstruct phylogenetic tree. The default method is hcp.

--srna

    The srna (SSU rRNA) method is use SSU rRNA data to reconstruct phylogenetic tree.





Advance options
#####################

Users enable choice more detail options with PhySpeTree call software, detail advance options input
``must be enclosed in single quotes and Start with a space``.

The following is an example of using RAxML advanced options:

.. code-block:: console

    $ PhySpeTree -i organism_example_list.txt --raxml --raxml_p '-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1'

--muscle
    Multiple sequence alignment by muscle. The default multiple sequence alignment software is Muscle.


--muscle_p
    Set Muscle advance parameters. The default is ``-maxiter 100``. More options about Muscle please to see
    `MUSCLE Manual <http://www.drive5.com/muscle/manual/options.html>`_.

    -maxiter
        maximum number of iterations to run is set 100.

--clustalw
    Multiple sequence alignment by clustalw2.

--clustalw_p
    Set clustalw2 advance parameters. Here use clustalw default parameters. More options about clustalw
    please to see `Clustalw Help <http://www.clustal.org/download/clustalw_help.txt>`_.


--gblocks
    Set Gblocks advance parameters. The default is ``-t=p -e=-gb1``.
    More options about Gblocks please to see
    `Gblocks documentation <http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_documentation.html>`_.

    -t
        Choice type of sequence. The PhySpeTree default set is protein.

    -e
        Eneric file extensionc. PhySpeTree set default is -gbl1.


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
    Set FastTree advance parameters. More options about clustalw
    please to see `FastTree <http://www.microbesonline.org/fasttree/>`_.

combine
^^^^^^^^^^^^^^^^^^^^

The **combine** module for the consensus tree construction.


In Linux you can easy combine more tree to a tree file, for example:

.. code-block:: console

    $ cat tree1.tree tree2.tree > combineTree.tree


Use **combine** in command line like this:

.. code-block:: console

    $ PhySpeTree PhySpeTree combine -i combineTree.tree [options]*


combine options
#####################

-h
    Print help message and exits.

-i
    Input a tree file (PHYLIP format), which contain multiple tree.

-o
    A directory contain combined tree file. The default output data name is combineTree.

--mr
    Compute majority rule consensus tree.

--mre
    Compute extended majority rule consensus tree.

--strict
    Compute strict consensus tree.


iview
^^^^^^^^^^^^^^^^^^^^

Users can Annotating tree by `iview` module by iTol.


Use **iview** in command line like this:

.. code-block:: console

    $ PhySpeTree iview -i organism_example_list.txt -range phylum


iview options
#####################


-h
    Print help message and exits.

-i
    Input a TXT file contain species names (abbreviated names) are same with KEGG species abbreviation.

-o
    A directory contain the generate configure files. The directory name is iview.

-r
    Annotating ranges by kingdom, phylum, class or order. The default is phylum.

-a
    Colored ranges by users assign, users can choice from [kingdom, phylum, class and order].

-l
    Change species labels from abbreviated names to full names.

check
^^^^^^^^^^^^^^^^^^^^

The `check` module design for check input organisms whether match in KEGG database or SILVA database.


.. code-block:: console

    $ PhySpeTree check -i organism_example_list.txt -out check --ehcp



check options
#####################



-h
    Print help message and exits.

-i
    Input a TXT file contain species names (abbreviated names) are same with KEGG species abbreviation.

-o
    A directory contain check result. The default directory name is check.

--hcp
    Check organisms whether supported by KEGG database.

--ehcp
    check input organisms prepare for extend autobuild tree module.

--srna
    Check organisms whether supported by SILVA database.


Frequently Asked Questions (FAQ)
--------------------------------------------------------------------------------

PhySpeTree input/output
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**1.What preparation of users should does for PhySpeTree?**

The users should prepare a TXT file, which contain species name (abbreviated names are same with `KEGG database <http://www.genome.jp/kegg/catalog/org_list.html>`_.),
one line write one species name only. For example, `organism_example_list <https://gitlab.com/xiaoxiaoyang/physpetools/raw/master/examples/organism_example_list.txt>`_.
You can retrieve the Abbreviation of species names by `KEGG API <http://rest.kegg.jp/list/organism>`_.


**2.What's PhySpeTree output data mean?**

PhySpeTree output two data files, the one is a result file default names is `Outdata`, another is a `temp` file.

If you reconstruct phylogenetic tree by `--hcp` (highly conserved protein) method, the temp file sinclude three directory: ``conserved_protein``, ``muscle_alignment`` and ``concatenate``.
  + conserved_protein: Store the FASTA format files, which was highly conserved proteins retrieved from KEGG database.
  + alignment: Store the sequence files has been aligned.
  + concatenate: Include concatenated highly conserved proteins data (FASTA format) and selected conserved blocks data (\*.fasta-gb1 format file).

If you reconstruct phylogenetic tree by `--srna` (SSU rRNA) method, the temp files include two directory: ``rna_sequence`` and ``rna_alignment``.
  + rna_sequence: Store a file named rna_sequence.fasta, contain the SSU rRNA sequence retrieved from SILVA database.
  + ran_alignment: Store in the \*.fasta file is the sequence files has been aligned and the \*.fasta-gb1, \*fasta-gb1.html are select conserved blocks data (use Gblocks software),
    the \*.phy format file is converted from select conserved blocks data by PhySpeTree.

``NOTE:``

*Users can check the quality of every aspect of data by the corresponding temp files.*


PhySpeTree reconstruct phylogenetic tree database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**what's the highly conserved proteins be used to reconstruct phylogenetic tree?**

PhySpeTree use 31 highly conserved proteins to reconstruct phylogenetic tree. This highly conserved proteins exclusion Horizontal Gene Transfers (HGTs) already.

**cite:**

 Ciccarelli F D, Doerks T, Von Mering C, et al. Toward automatic reconstruction of a highly resolved tree of life[J]. science, 2006, 311(5765): 1283-1287.

The 31 highly conserved proteins and corresponding KEGG database KO number as follow table:


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



**2.How the SSU rRAN database was created?**

The SSU rRAN database was created by `SILVA <https://www.arb-silva.de/>`_ SSU rRNA database project (version: SILVA SSU 123.1 release).
In this data the sequences haven been truncated, which means that all nucleotides that have not been aligned were removed from the sequence.



.. |PyPI version| image:: https://img.shields.io/pypi/v/PhySpeTree.svg?style=flat-square
   :target: https://pypi.python.org/pypi/PhySpeTree
.. |Docs| image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat-square
   :target: https://xiaofeiyangyang.github.io/physpetools/
.. |License| image:: https://img.shields.io/aur/license/yaourt.svg?maxAge=2592000
   :target: https://github.com/xiaofeiyangyang/physpetools/blob/master/LICENSE.txt