# Usage and Examples




## autobuild

User should prepare a txt file contain the abbreviation names of organisms [organism_example_list.txt][1]

Use **autobuild** in command line like this:

```bash
$ physpe -i organism_example_list.txt [options]*
```

### Autobuild options

| option |  Description                                                                                                                          |
|:------- |:-------------------------------------------------------------------------------------------------------------------------------------|
|  -h     |  Print help message and exits.                                                                                                       |
|  -i     |  Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation.                                  |
|  -o     |  A directory include output data (reconstruct tree files). The default output data name is Outdata.                                  |
|  -t     |  Specify the number of processing threads (CPUs) to use for Physpe to reconstruct phylogenetic tree. The default is 1.               |
|  -e     |  The extended data should be FASTA format to extend phylogenetic tree by --ehcp or --esrna option.                                  |
|  --hcp  |  The hcp (highly conserved protein) mode is use highly conserved proteins to reconstruct phylogenetic tree. The default mode is hcp. |
|  --ehcp |  The ehcp (extend highly conserved protein) mode is use highly conserved proteins and extend highly protein (user provide) to reconstruct phylogenetic tree. |
|  --srna |  The srna (16s SSU RNA) mode is use 16s SSU RNA data to reconstruct phylogenetic tree.                                              |
|  --esrna|  The esrna (extend 16s SSU RNA) mode is use 16s SSU RNA data and extend 16s SSU RNA (user provide) to reconstruct phylogenetic tree.        |


### example

When use autobuild command to reconstruct phylogenetic tree, user should prepare a organism list with abbreviation names are same with [KEGG organism list][2]

List format like follow or download [organism_example_list.txt][1]

```bash
$ cat organism_example_list.txt
aca
ace
acl
acn
aco
acp
adg
adk
aeh
aeq
```

* Auto build phylogenetic tree by highly conserved proteins:

```bash
$ physpe autobuild -i organism_example_list.txt --hcp
Loading organisms names success.....

The result are store in:Outdata

now loading data and constructing species phylogenetic tree......

```

When auto reconstruct phylogenetic tree completed, you will get file layout like this:

```
log.log
Outdata/
        RAxML_bestTree.T1
        RAxML_bipartitions.T1
        RAxML_bipartitionsBranchLabels.T1
        RAxML_bootstrap.T1
        RAxML_info.T1
   temp/
        conserved_protein20160817210902/
                                       　p1.fasta
                                       　p2.fasta
                                       　p3.fasta
                                       　......
        hcp_alignment20160817210936/
                                    p1.fasta
                                    p2.fasta
                                    p2.fasta
                                    ......
        concatenate20160817210938/
                                  concatenate.fasta
                                  concatenate.fasta-gb1
                                  concatenate.fasta-gb1.htm
                                  concatenate.fasta-gb1.phy
```


* log.log: The log information of physpe.
* Outdata: Contain phylogenetic tree output result. 
    
    - RAxML_bestTree.T1: Reconstruct phylogenetic tree by RAxML, it's best ML search tree. 
    - RAxML_bipartitions.T1: Bipartition tree by RAxML.
    - RAxML_bipartitionsBranchLabels.T1: Bipartition tree by constructed by RAxML with branch length lables.
    - RAxML_bootstrap.T1: Bootstrap result by RAxML
    - RAxML_info.T1: The info of run RAxMl.
    
* temp: The temp data by physpe, `it's very important to user to check the key steps`.

    - conserved_protein: Contain highly conserved proteins retrieve form KEGG database.
    - hcp_alignment: Contain highly conserved proteins do multiple sequence alignment by muscle.
    - concatenate: Contain the concatenate highly conserved proteins result and select conserved blocks data.
    
     + concatenate.fasta: Concatenate highly conserved proteins result.
     + concatenate.fasta-gb1: select conserved blocks result (by Gblocks).
     + concatenate.fasta-gb1.htm: select conserved blocks result view by html format.
     + concatenate.fasta-gb1.phy: Convert FASTA format to PHYLIP format





### Advance options

User enable choice more detail options with Physpe call software, detail advance options input
``must be enclosed in single quotes``.

The follow is to use RAxML advance options example:

```bash
$ physpe -i organism_example_list.txt --raxml '-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1'
```

**--muscle**

  Set multiple sequence alignment parameters. The default is ``-maxiter 100``. More options about muslce please to see[MUSCLE Manual](http://www.drive5.com/muscle/manual/options.html)

The default option:

|  option   | description                                      |
|:----------|:-------------------------------------------------|
|  -maxiter | maximum number of iterations to run is set 100.  |


**--gblocks**

  Set Gblocks parameters. The default is ``-t=p -e=-gb1``. More options about Gblocks please to see [Gblocks documentation](http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_documentation.html).

The default option:

|  option | description                                                 |
|:--------|:------------------------------------------------------------|
|  -t     | Choice type of sequence. The physpe default set is protein. |
|  -e     | Eneric file extensionc. physep set default is -gbl1.        |


**--raxml**

  Set reconstruct phylogenetic tree arguments with RAxML. The default is ``-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1``. More options about RAxMl please to see [RAxML Manual](http://sco.h-its.org/exelixis/resource/download/NewManual.pdf).

The default option:

|  option | description                                                                                                                          |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------ |
|   -f    |  select algorithm. The physpe default set is ``a``, rapid Bootstrap analysis and search for best­scoring ML tree in one program run. |
|   -m    |  Model of Binary (Morphological), Nucleotide, Multi­State, or Amino Acid Substitution. The physpe default set is PROTGAMMAJTTX.      |
|   -p    |  Specify a random number seed for the parsimony inferences. The physep default set is 12345.                                         |
|   -x    |  Specify an integer number (random seed) and turn on rapid bootstrapping. The physpe default set is 12345.                           |
|   -N    |  The same with -# specify the number of alternative runs on distinct starting trees. The physpe default set is 100.                  |




## build

User can build tree by own 16s rna data or highly conserved proteins.

Use **build** in command line to reconstruct phylogenetic tree:

* build phylogenetic tree by highly conserved proteins


```bash
$ physpe build -i example_hcp -o output --hcp
```
* build phylogenetic tree by 16s ssu rna data


```bash
$ physpe build -i example_16s_ssurna.fasta -o output --sran
```



### build options

| option |  Description                                                                                                                          |
|:------- |:-------------------------------------------------------------------------------------------------------------------------------------|
|  -h     |  Print help message and exits.                                                                                                       |
|  -i     |  Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation.                                  |
|  -o     |  A directory include output data (reconstruct tree files). The default output data name is Outdata.                                  |
|  -t     |  Specify the number of processing threads (CPUs) to use for Physpe to reconstruct phylogenetic tree. The default is 1.               |
|  --hcp  |  The hcp (highly conserved protein) mode is use highly conserved proteins to reconstruct phylogenetic tree. The default mode is hcp. |
|  --srna |  The 16srna (16 SSU RNA) mode is use 16s SSU RNA data to reconstruct phylogenetic tree.                                              |


### Advance options

User enable choice more detail options with Physpe call software, detail advance options input
``must be enclosed in single quotes``.

The follow is to use RAxML advance options example:

```bash
$ physpe -i example_chp  --raxml '-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1' --hcp
```

**--muscle**

  Set multiple sequence alignment parameters. The default is ``-maxiter 100``. More options about muslce please to see[MUSCLE Manual](http://www.drive5.com/muscle/manual/options.html)

The default option:

|  option   | description                                      |
|:----------|:-------------------------------------------------|
|  -maxiter | maximum number of iterations to run is set 100.  |


    

    
        

**--gblocks**

  Set Gblocks parameters. The default is ``-t=p -e=-gb1``. More options about Gblocks please to see [Gblocks documentation](http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_documentation.html).

The default option:

|  option | description                                                 |
|:--------|:------------------------------------------------------------|
|  -t     | Choice type of sequence. The physpe default set is protein. |
|  -e     | Eneric file extensionc. physep set default is -gbl1.        |

   
        

    
        

**--raxml**

  Set reconstruct phylogenetic tree arguments with RAxML. The default is ``-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1``. More options about RAxMl please to see [RAxML Manual](http://sco.h-its.org/exelixis/resource/download/NewManual.pdf).

The default option:

|  option | description                                                                                                                          |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------ |
|   -f    |  select algorithm. The physpe default set is ``a``, rapid Bootstrap analysis and search for best­scoring ML tree in one program run. |
|   -m    |  Model of Binary (Morphological), Nucleotide, Multi­State, or Amino Acid Substitution. The physpe default set is PROTGAMMAJTTX.      |
|   -p    |  Specify a random number seed for the parsimony inferences. The physep default set is 12345.                                         |
|   -x    |  Specify an integer number (random seed) and turn on rapid bootstrapping. The physpe default set is 12345.                           |
|   -N    |  The same with -# specify the number of alternative runs on distinct starting trees. The physpe default set is 100.                  |




## combine


User should prepare a combine tree file by Combine command to combine tree files.


In Linux you can easy combine more tree to a tree file, for example:

```bash
$ cat tree1.tree tree2.tree > combieTree.tree

```

Use **combine** in command line like this:


```bash
$ physpe -i organism_example_list.txt [options]*
```

### Combine options


| option  | Description  |
|---|---|
|  -h |  Print help message and exits. |
|  -i |  Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation. |
|  -o |  A directory contain combine tree file. The default output data name is combinetree. |


## iview

Annotating tree by iTol by iview module.


Use **iview** in command line like this:

```bash
$ physpe iview -i organism_example_list.txt -range phylum
```

### iview options

| option | Description                                                                                         |
|:-------|:----------------------------------------------------------------------------------------------------|
|  -h    |  Print help message and exits.                                                                      |
|  -i    |  Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation. |
|  -o    |  A directory contain range text file. The directory name is iview.                                  |


## check


Use check module  check input organisms match in kegg database or 16s database


```bash
$ physpe check -i organism_example_list.txt -out check --ehcp
```


### check options


| option | Description                                                                                         |
|:-------|:----------------------------------------------------------------------------------------------------|
|  -h    |  Print help message and exits.                                                                      |
|  -i    |  Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation. |
|  -o    |  A directory contain check result. The directory name is check.                                     |
| --echcp|  check input organisms prepare for extend autobuild tree module.                                  |

    
[1]: example/organism_example_list.txt
[2]: http://www.genome.jp/kegg/catalog/org_list.html

    