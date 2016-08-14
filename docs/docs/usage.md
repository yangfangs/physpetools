Usage and Examples
==================



Autobuild
----------

User should prepare a txt file contain the abbreviation names of organisms `example <https://raw.githubusercontent.com/xiaofeiyangyang/physpetools/master/examples/organism_example_list.txt>`_.

Use **autobuild** in command line like this:

.. code-block:: console

    $ physpe -i organism_example_list.txt [options]*


Auto options
#####################

-h
    Print help message and exits.

-v
    The version information.

-i
    Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation.

-o
    A directory include output data (reconstruct tree files). The default output data name is Outdata.

-t
    Specify the number of processing threads (CPUs) to use for Physpe to reconstruct phylogenetic tree. The default is 1.

--hcp
    The hcp (highly con.. code-block:: console

    $ physpe -in organism_example_list.txt [options]*served protein) mode is use conserved proteins to reconstruct phylogenetic tree. The default mode is hcp.

--srna
    The 16srna (16 ssu RNA) mode is use 16s RNA data to reconstruct phylogenetic tree.



Advance options
#####################

User enable choice more detail options with Physpe call software, detail advance options input
``must be enclosed in single quotes``.

The follow is to use RAxML advance options example:

.. code-block:: console

    $ physpe -i organism_example_list.txt -raxml '-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1'

--muscle
    Set multiple sequence alignment parameters. The default is ``-maxiter 100``. More options about muslce please to see
    `MUSCLE Manual <http://www.drive5.com/muscle/manual/options.html>`_.

    -maxiter
        maximum number of iterations to run is set 100.

--gblocks
    Set Gblocks parameters. The default is ``-t=p -e=-gb1``.
    More options about Gblocks please to see
    `Gblocks documentation <http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_documentation.html>`_.

    -t
        Choice type of sequence. The physpe default set is protein.

    -e
        Eneric file extensionc. physep set default is -gbl1.

--raxml
    Set reconstruct phylogenetic tree arguments with RAxML. The default is ``-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1``.
    More options about RAxMl please to see `RAxML Manual <http://sco.h-its.org/exelixis/resource/download/NewManual.pdf>`_.

    -f
        select algorithm. The physpe default set is ``a``, rapid Bootstrap analysis and search for best­scoring ML tree in one program run

    -m
        Model of Binary (Morphological), Nucleotide, Multi­State, or Amino Acid Substitution. The physpe default set is PROTGAMMAJTTX.

    -p
        Specify a random number seed for the parsimony inferences. The physep default set is 12345.

    -x
        Specify an integer number (random seed) and turn on rapid bootstrapping. The physpe default set is 12345

    -N
        The same with -# specify the number of alternative runs on distinct starting trees. The physpe default set is 100.


Combine
----------------

User should prepare a combine tree file by Combine command to combine tree files.


In Linux you can easy combine more tree to a tree file, for example:

.. code-block:: console

    $ cat tree1.tree tree2.tree > combieTree.tree


Use **combine** in command line like this:

.. code-block:: console

    $ physpe -i organism_example_list.txt [options]*


Combine options
#####################

-h
    Print help message and exits.

-i
    Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation.

-o
    A directory contain combine tree file. The default output data name is combinetree.

iview
----------------

Annotating tree by iTol by iview module.


Use **iview** in command line like this:

.. code-block:: console

    $ physpe iview -i organism_example_list.txt -range phylum


iview options
#####################


-h
    Print help message and exits.

-i
    Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation.

-o
    A directory contain combine tree file. The default output data name is combinetree.

