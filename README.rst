PhySpeTree: automatically reconstructing phylogenetic species tree
==============================================================================

|PyPI version| |Docs| |License|

**PhySpeTree is implemented in Python 2.7, designed for Linux system.**

**Documents**: `PhySpeTree documentation <https://yangfangs.github.io/physpetools>`_.

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

.. image:: https://raw.githubusercontent.com/yangfangs/physpetools/master/docs/docs/img/PhySpeTree_work_follow.png


PhySpeTree workflow includes the following steps:

1. Prepare `abbreviated species names <https://raw.githubusercontent.com/yangfangs/physpetools/master/examples/organism_example_list.txt>`_.

2. Choose the method to reconstruct species trees (SSU rRNA (--srna) or HCP (--hcp)).

3. Query, parse, and retrieve sequences in the FASTA format.

4. Multiple sequence alignment and concatenate HCP.

5. Select conserved blocks.

6. Reconstruct species trees.

7. Output trees.



Features
--------------------------------------------------------------------------------
- Inputs only include species names.

- One command line to build trees.

- HCP and SSU rRNA methods.

- Combine trees.

- View trees with iTOL.

- Versatile software with adjustable parameters.


Install
-------------------------------------------------------------------------------

1. PyPI

.. code-block:: console

	$ pip install PhySpeTree


or `download PhySpeTree <https://pypi.python.org/pypi/PhySpeTree/>`_ and install:

.. code-block:: console

    $ pip install PhySpeTree-*.tar.gz


To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade PhySpeTree

2. GitHub

.. code-block:: console

    $ git clone git@github.com:yangfangs/physpetools.git
    $ cd physpetools
    $ python setup.py install

or `download <https://github.com/yangfangs/physpetools/releases>`_ and install:

.. code-block:: console

    $ pip install physpetools-*.tar.gz



Usage
-------------------------------------------------------------------------------

autobuild
^^^^^^^^^^^^^^^^^^^^

The input of `autobuild` module is a TXT file containing abbreviated species names, for example `organism example list <https://raw.githubusercontent.com/yangfangs/physpetools/master/examples/organism_example_list.txt>`_.

Use **autobuild** in command line like this:

.. code-block:: console

    $ PhySpeTree -i organism_example_list.txt [options]*


autobuild options
#####################

-h
    Print help message and exits.

-i
    Input a TXT file containing abbreviated species names.

-o
    A directory to store outputs. The default is "Outdata".

-t
    Number of processing threads (CPUs). The default is 1.

-e
    FASTA format files to extend the tree with the --ehcp or --esrna option.

--hcp

    HCP (highly conserved protein) method (default).

--ehcp

    HCP method with extended HCP sequences.

--srna

    SSU method.

--esrna

    SSU rRNA method with extended SSU rRNA sequences.


Advance options
#####################

Advanced options of internal software called in PhySpeTree can be set. These options are ``enclosed in single quotes and start with a space``.

Here is an example of setting RAxML advanced options by `--raxml_p`:

.. code-block:: console

    $ PhySpeTree autobuild -i organism_example_list.txt -o test --srna --raxml --raxml_p ' -f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1'

--muscle
    Multiple sequence alignment by MUSCLE (default).


--muscle_p
    Set Muscle advance parameters. The default is ``-maxiter 100``, please see
    `MUSCLE Manual <http://www.drive5.com/muscle/manual/options.html>`_.

    -maxiter
        maximum number of iterations to run is set 100.

--clustalw
    Multiple sequence alignment by clustalw2.

--clustalw_p
    Set clustalw2 advance parameters. Here use clustalw default parameters,
    please see `Clustalw Help <http://www.clustal.org/download/clustalw_help.txt>`_.


--gblocks
    Set Gblocks advance parameters,
    please see `Gblocks documentation <http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_documentation.html>`_.

    -t
        Choice type of sequence(default).

    -e
        Generic File Extension. PhySpeTree set default is "-gbl1".


--raxml
    Reconstruct phylogenetic tree by RAxML (default).

--raxml_p
    Set RAxML advanced parameters. The default is ``-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1``,
    please see `RAxML Manual <http://sco.h-its.org/exelixis/resource/download/NewManual.pdf>`_.

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
    Set FastTree advance parameters,
    please see `FastTree <http://www.microbesonline.org/fasttree/>`_.

build
^^^^^^^^^^^^^^^^^^^^

The `build` module is used to reconstruct species trees with manually prepared sequences. Advanced options are the same as `autobuild` module.

Use **build** in command line to reconstruct phylogenetic tree:

* build phylogenetic tree by HCP method:


.. code-block:: console

    $ PhySpeTree build -i example_hcp -o output --hcp


* build phylogenetic tree by SSU rRNA method:


.. code-block:: console

    $ PhySpeTree build -i example_16s_ssurna.fasta -o output --sran

build options
#####################

-h
    Print help message and exits.

-i
    Input a TXT file containing abbreviated species names.

-o
    A directory to store outputs. The default is "Outdata".

-t
    Number of processing threads (CPUs). The default is 1.

--hcp

    HCP method (default).

--srna

    SSU rRNA method.

combine
^^^^^^^^^^^^^^^^^^^^

The **combine** module is used to combine trees generated from different methods. It contains two steps, at first merge different tree files into the same file. You can use `cat` bash command in the Linux system, for example:

.. code-block:: console

    $ cat tree1.tree tree2.tree > combineTree.tree


Then, use **combine**

.. code-block:: console

    $ PhySpeTree PhySpeTree combine -i combineTree.tree [options]*


combine options
#####################

-h
    Print help message and exits.

-i
    Input PHYLIP format file containing multiple trees.

-o
    Output directory. The default is "combineTree".

--mr
    Majority rule trees..

--mre
    Extended majority rule trees.

--strict
    Strict consensus trees.


iview
^^^^^^^^^^^^^^^^^^^^

PhySpeTree provides the `iview` module to annotate taxonomic information (kingdom, phylum, class, or order) of output trees and to generate configure files linked to `iTol <http://itol.embl.de/)>`_.


Use **iview** in command line like this:

.. code-block:: console

    $ PhySpeTree iview -i organism_example_list.txt --range


iview options
#####################


-h
    Print help message and exits.

-i
    Input a TXT file containing abbreviated species names.

-o
    A directory to store outputs. The default is "iview".

-r
    Annotating labels with ranges by kingdom, phylum, class or order. The default is phylum.

-c
    Annotating labels without ranges by kingdom, phylum, class or order. The default is phylum.

-a
    Colored ranges by users assign, users can choice from [kingdom, phylum, class and order].

-l
    Change species labels from abbreviated names to full names.

check
^^^^^^^^^^^^^^^^^^^^

The `check` module is used to check whether input organisms are in pre-built databases.


.. code-block:: console

    $ PhySpeTree check -i organism_example_list.txt -out check --ehcp



check options
#####################



-h
    Print help message and exits.

-i
    Input a TXT file containing abbreviated species names.

-o
    A directory to store outputs. The default is "check".

--hcp
   Check whether organisms are supported in the KEGG database.

--ehcp
    Check input organisms prepare for extend autobuild tree module.

--srna
    Check whether organisms are supported in the SILVA database.


Frequently Asked Questions (FAQ)
--------------------------------------------------------------------------------

**1.What is the input of PhySpeTree?**

Users only need to prepare a TXT file containing `KEGG <http://www.genome.jp/kegg/catalog/org_list.html>`_ abbreviated species names. For example, `organism example list <https://raw.githubusercontent.com/yangfangs/physpetools/master/examples/organism_example_list.txt>`_.

**2.How to explain PhySpeTree outputs?**

PhySpeTree returns two folders, `Outdata` contains the output species tree and `temp` includes temporary data. Files in `temp` can be used to check the quality of outputs in each step. If HCP method (`--hcp`) is selected, the `temp` folder includes:

  * `conserved_protein`: highly conserved proteins retrieved from the KEGG database.
  * `alignment`: aligned sequences.
  * `concatenate`: concatenated sequences and conserved blocks.

If SSU rRNA method (`--srna`) is selected, the `temp` folder includes:

  * `rna_sequence`: SSU rRNA sequences retrieved from the SILVA database.
  * `rna_alignment`: aligned sequences and conserved blocks.


**What classes of HCP are selected?**

PhySpeTree uses 31 HCP without horizontal transferred genes according to Ciccarelli *et al.*.

**cite:**

 Ciccarelli F D, Doerks T, Von Mering C, et al. Toward automatic reconstruction of a highly resolved tree of life[J]. science, 2006, 311(5765): 1283-1287.

The 31 HCP and corresponding KEGG KO number are shown in the following table:


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



**2.4.How are SSU rRAN created?**

The SSU rRAN sequences are created from the `SILVA <https://www.arb-silva.de/>`_ database (123.1 release). Sequences haven been truncated, which means unaligned nucleotides are removed.



.. |PyPI version| image:: https://img.shields.io/pypi/v/PhySpeTree.svg?style=flat-square
   :target: https://pypi.python.org/pypi/PhySpeTree
.. |Docs| image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat-square
   :target: https://yangfangs.github.io/physpetools/
.. |License| image:: https://img.shields.io/aur/license/yaourt.svg?maxAge=2592000
   :target: https://github.com/yangfangs/physpetools/blob/master/LICENSE.txt