# Usage and Examples




## autobuild

Users should prepare a TXT file contain the species names (abbreviated names), such as [organism_example_list.txt][1]

Use **autobuild** in command line like this:

```bash
$ PhySpeTree -i organism_example_list.txt [options]*
```

### Autobuild options

| option |  Description                                                                                                                            |
|:------- |:---------------------------------------------------------------------------------------------------------------------------------------|
|  -h     |  Print help message and exits.                                                                                                         |
|  -i     |  Input a TXT file contain the species names (abbreviated names) are same with KEGG species abbreviation.                               |
|  -o     |  A directory include output data (tree files). The default output data name is Outdata.                                                |
|  -t     |  Specify the number of processing threads (CPUs) to reconstruct phylogenetic tree. The default is 1.                                   |
|  -e     |  The extended data should be FASTA format to extend phylogenetic tree by --ehcp or --esrna option.                                     |
|  --hcp  |  Specify the hcp (highly conserved protein) method to reconstruct phylogenetic tree. The default method is hcp.                        |
|  --ehcp |  The ehcp mode is use highly conserved proteins with extend highly conserved protein (users provide) to reconstruct phylogenetic tree. |
|  --srna |  The srna (SSU rRNA) method is use SSU rRNA data to reconstruct phylogenetic tree.                                                     |
|  --esrna|  The esrna mode is use SSU RNA sequence with extend SSU RNA sequence (users provide) to reconstruct phylogenetic tree.                 |


### example

When use `autobuild` command to build species tree, users should prepare a organism list with species names (abbreviated names) are same with [KEGG organism list][2].

The format of the list is as follows or download [organism_example_list.txt][1].

```bash
$ wget "https://xiaofeiyangyang.github.io/physpetools/example/organism_example_list.txt"

--2016-10-29 19:41:53--  https://xiaofeiyangyang.github.io/physpetools/example/organism_example_list.txt
Resolving xiaofeiyangyang.github.io (xiaofeiyangyang.github.io)... 151.101.24.133
Connecting to xiaofeiyangyang.github.io (xiaofeiyangyang.github.io)|151.101.24.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 39 [text/plain]
Saving to: ‘organism_example_list.txt’

organism_example_list.txt     100%[==============================================>]      39  --.-KB/s    in 0s      

2016-10-29 19:41:54 (19.0 MB/s) - ‘organism_example_list.txt’ saved [39/39]

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

#### **Auto build phylogenetic tree by highly conserved proteins method:**

```bash
$ PhySpeTree autobuild -i organism_example_list.txt --hcp
Loading organisms names success.....

The result are store in:Outdata

Now loading data and constructing phylogenetic tree......
2016-10-29 19:44:11,660 KEGG INDEX DB INFO: Read organisms names success
2016-10-29 19:44:17,296 KEGG INDEX DB INFO: Retrieve and download of highly conserved protein 'Ribosomal protein L1' was successful store in p1.fasta file
2016-10-29 19:44:17,919 KEGG INDEX DB INFO: Retrieve and download of highly conserved protein 'DNA-directed RNA polymerase subunit alpha' was successful store in p2.fasta file
2016-10-29 19:44:18,369 KEGG INDEX DB INFO: Retrieve and download of highly conserved protein 'Leucyl-tRNA synthetase' was successful store in p3.fasta file
2016-10-29 19:44:18,943 KEGG INDEX DB INFO: Retrieve and download of highly conserved protein 'Metal-dependent proteases with chaperone activity' was successful store in p4.fasta file
2016-10-29 19:44:19,660 KEGG INDEX DB INFO: Retrieve and download of highly conserved protein 'Phenylalanine-tRNA synthethase alpha subunit' was successful store in p5.fasta file
2016-10-29 19:44:20,114 KEGG INDEX DB INFO: Retrieve and download of highly conserved protein 'Predicted GTPase probable translation factor' was successful store in p6.fasta file
2016-10-29 19:44:20,505 KEGG INDEX DB INFO: Retrieve and download of highly conserved protein 'Ribosomal protein L11' was successful store in p7.fasta file
2016-10-29 19:44:20,917 KEGG INDEX DB INFO: Retrieve and download of highly conserved protein 'Ribosomal protein L13' was successful store in p8.fasta file
2016-10-29 19:44:21,333 KEGG INDEX DB INFO: Retrieve and download of highly conserved protein 'Ribosomal protein L14' was successful store in p9.fasta file
......
```

When building a phylogenetic tree using the HCP method, you will get files layout like this:

```
log.log
Outdata/
        RAxML_bestTree.T1
        RAxML_bipartitions.T1
        RAxML_bipartitionsBranchLabels.T1
        RAxML_bootstrap.T1
        RAxML_info.T1
   temp/
        conserved_protein20161029194411/
                                       　p1.fasta
                                       　p2.fasta
                                       　p3.fasta
                                       　......
        alignment20161029194429/
                                    p1.fasta
                                    p2.fasta
                                    p2.fasta
                                    ......
        concatenate20161029194432/
                                  concatenate.fasta
                                  concatenate.fasta-gb1
                                  concatenate.fasta-gb1.htm
                                  concatenate.fasta-gb1.phy
```


* log.log: The log information of PhySpeTree.
* Outdata: Contain PhySpeTree output result (Tree Files). 
    
    - RAxML_bestTree.T1: Reconstruct phylogenetic tree by RAxML, it's best ML search tree. 
    - RAxML_bipartitions.T1: Bipartition tree by RAxML.
    - RAxML_bipartitionsBranchLabels.T1: Bipartition tree by RAxML constructed with branch length labels.
    - RAxML_bootstrap.T1: Bootstrap result by RAxML
    - RAxML_info.T1: The info of run RAxMl.
    
* temp: The temp data by PhySpeTree, `it's very important for users to check the key steps`.

    - conserved_protein: Contain highly conserved proteins retrieved and downloaded form KEGG database.
    - alignment: Contain highly conserved proteins with multiple sequence alignment by muscle.
    - concatenate: Contain the concatenate highly conserved proteins result and select conserved blocks data.
    
        + concatenate.fasta: Concatenated highly conserved proteins data.
        + concatenate.fasta-gb1: Selected conserved blocks data (by Gblocks).
        + concatenate.fasta-gb1.htm: Selected conserved blocks result and display by html format.
        + concatenate.fasta-gb1.phy: Convert FASTA format to PHYLIP format.


####  **Auto build phylogenetic tree by SSU rRNA method:**


```bash
$ PhySpeTree autobuild -i organism_example_list.txt --srna
Loading organisms names success.....

The result are store in:Outdata

Now loading data and constructing phylogenetic tree......
2016-10-29 20:12:49,353 SSU rRNA DB INFO: Read organisms names success
2016-10-29 20:12:54,582 SSU rRNA DB INFO: Retrieve and download of organism 'aca' SSU rRNA sequence was successful
2016-10-29 20:12:56,831 SSU rRNA DB INFO: Retrieve and download of organism 'ace' SSU rRNA sequence was successful
2016-10-29 20:12:59,182 SSU rRNA DB INFO: Retrieve and download of organism 'acl' SSU rRNA sequence was successful
2016-10-29 20:13:01,545 SSU rRNA DB INFO: Retrieve and download of organism 'acn' SSU rRNA sequence was successful
2016-10-29 20:13:04,096 SSU rRNA DB INFO: Retrieve and download of organism 'aco' SSU rRNA sequence was successful
2016-10-29 20:13:06,972 SSU rRNA DB INFO: Retrieve and download of organism 'acp' SSU rRNA sequence was successful
2016-10-29 20:13:09,943 SSU rRNA DB INFO: Retrieve and download of organism 'adg' SSU rRNA sequence was successful
2016-10-29 20:13:12,707 SSU rRNA DB INFO: Retrieve and download of organism 'adk' SSU rRNA sequence was successful
2016-10-29 20:13:16,015 SSU rRNA DB INFO: Retrieve and download of organism 'aeh' SSU rRNA sequence was successful
2016-10-29 20:13:18,969 SSU rRNA DB INFO: Retrieve and download of organism 'aeq' SSU rRNA sequence was successful

```


When building a phylogenetic tree using the SSU rRNA method, you will get files layout like this:

```
log.log
Outdata/
        RAxML_bestTree.T1
        RAxML_bipartitions.T1
        RAxML_bipartitionsBranchLabels.T1
        RAxML_bootstrap.T1
        RAxML_info.T1
   temp/
        rna_sequence20161029201249/
                                 rna_sequence.fasta

        rna_alignment20161029201319/
                                  rna_sequence.fasta
                                  rna_sequence.fasta-gb1
                                  rna_sequence.fasta-gb1.htm
                                  rna_sequence.fasta-gb1.phy
```

* log.log: The log information of PhySpeTree.
* Outdata: Contain PhySpeTree output result (Tree Files). 
    
    - RAxML_bestTree.T1: Reconstruct phylogenetic tree by RAxML, it's best ML search tree. 
    - RAxML_bipartitions.T1: Bipartition tree by RAxML.
    - RAxML_bipartitionsBranchLabels.T1: Bipartition tree by RAxML constructed with branch length labels.
    - RAxML_bootstrap.T1: Bootstrap result by RAxML
    - RAxML_info.T1: The info of run RAxMl.
    
* temp: The temp data by PhySpeTree, `it's very important to users to check the key steps`.

    - rna_sequence: Contain SSU rRNA data retrieved and downloaded form SILVA database.
    
        + rna_sequence.fasta: A FASTA format file, which contain input organism SSU rRNA sequence.
         
    - rna_alignment: Contain the concatenated highly conserved proteins result and selected conserved blocks data.
    
        + rna_sequence.fasta: Contain SSU rRNA data with multiple sequence alignment already.
        + rna_sequence.fasta-gb1: Selected conserved blocks result (by Gblocks).
        + rna_sequence.fasta-gb1.htm: Selected conserved blocks result and display html format.
        + rna_sequence.fasta-gb1.phy: Convert FASTA format to PHYLIP format.


### Advance options

Users enable choice more detail options with PhySpeTree call software, detail advance options input
``must be enclosed in single quotes and start with space``.

The following is an example of using RAxML advanced options:

```bash
$ PhySpeTree -i organism_example_list.txt --raxml ' -f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1'
```

**--muscle**

  Multiple sequence alignment by muscle. The default multiple sequence alignment software is Muscle.


**--muscle_p**

  Set Muscle advance parameters. The default is ``-maxiter 100``. More options about Muscle please to see [MUSCLE Manual](http://www.drive5.com/muscle/manual/options.html)

The default option:

|  option   | description                                      |
|:----------|:-------------------------------------------------|
|  -maxiter | maximum number of iterations to run is set 100.  |


**--clustalw**

    Multiple sequence alignment by clustalw2.

**--clustalw_p**

  Set clustalw2 advance parameters. Here use clustalw2 default parameters. More options about clustalw2 please to see [Clustalw Help](http://www.clustal.org/download/clustalw_help.txt).


**--gblocks**

  Set Gblocks advance parameters. The default is ``-t=p -e=-gb1``. More options about Gblocks please to see [Gblocks documentation](http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_documentation.html).

The default option:

|  option | description                                                 |
|:--------|:------------------------------------------------------------|
|  -t     | Choice type of sequence. The PhySpeTree default set is protein. |
|  -e     | Eneric file extensionc. PhySpeTree set default is -gbl1.        |


**--ranxml**

    Reconstruct phylogenetic tree by RAxML. The default build tree software is RAxML.



**--raxml_p**

  Set reconstruct phylogenetic tree arguments with RAxML. The default is `` -f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1``. More options about RAxMl please to see [RAxML Manual](http://sco.h-its.org/exelixis/resource/download/NewManual.pdf).

The default option:

|  option | description                                                                                                                          |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------ |
|   -f    |  select algorithm. The PhySpeTree default set is ``a``, rapid Bootstrap analysis and search for best­scoring ML tree in one program run. |
|   -m    |  Model of Binary (Morphological), Nucleotide, Multi­State, or Amino Acid Substitution. The PhySpeTree default set is PROTGAMMAJTTX.      |
|   -p    |  Specify a random number seed for the parsimony inferences. The physep default set is 12345.                                         |
|   -x    |  Specify an integer number (random seed) and turn on rapid bootstrapping. The PhySpeTree default set is 12345.                           |
|   -N    |  The same with -# specify the number of alternative runs on distinct starting trees. The PhySpeTree default set is 100.                  |




**--fasttree**
    
  Reconstruct phylogenetic tree by FastTree.

**--fasttree_p**
    
  Set more FastTree advance parameters. More options about clustalw2 please to see [FastTree](http://www.microbesonline.org/fasttree/).


## build

Users can reconstruct phylogenetic tree use `build` module by manually prepared files. such as, SSU rRNA sequence or highly conserved proteins.

Use **build** module in command line to reconstruct phylogenetic tree:

* build phylogenetic tree by highly conserved proteins method:


```bash
$ PhySpeTree build -i example_hcp -o output --hcp
```

* build phylogenetic tree by SSU rRNA sequence method:


```bash
$ PhySpeTree build -i example_16s_ssurna.fasta -o output --sran
```



### build options

| option |  Description                                                                                                                            |
|:------- |:---------------------------------------------------------------------------------------------------------------------------------------|
|  -h     |  Print help message and exits.                                                                                                         |
|  -i     |  Input a TXT file contain the species names (abbreviated names) are same with KEGG species abbreviation.                               |
|  -o     |  A directory include output data (tree files). The default output data name is Outdata.                                                |
|  -t     |  Specify the number of processing threads (CPUs) to reconstruct phylogenetic tree. The default is 1.                                   |
|  -e     |  The extended data should be FASTA format to extend phylogenetic tree by --ehcp or --esrna option.                                     |
|  --hcp  |  Specify the hcp (highly conserved protein) method to reconstruct phylogenetic tree. The default method is hcp.                        |
|  --srna |  The srna (SSU rRNA) method is use SSU rRNA data to reconstruct phylogenetic tree.                                                     |


### example


#### **Build phylogenetic tree by highly conserved proteins**


When use build to reconstruct phylogenetic tree, you should prepare a directory contain highly conserved proteins such as [example_build_hcp][3]. In this example
contain ten highly conserved proteins p1~p10, in each highly conserved proteins contain 10 organisms.

Downloading [example_build_hcp][3] and then you can use the tar command to unpack in command line:

```bash

$ wget "https://xiaofeiyangyang.github.io/physpetools/example/example_build_hcp.tar.gz"

--2016-10-29 20:40:41--  https://xiaofeiyangyang.github.io/physpetools/example/example_build_hcp.tar.gz
Resolving xiaofeiyangyang.github.io (xiaofeiyangyang.github.io)... 151.101.48.133
Connecting to xiaofeiyangyang.github.io (xiaofeiyangyang.github.io)|151.101.48.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17419 (17K) [application/octet-stream]
Saving to: ‘example_build_hcp.tar.gz’

example_build_hcp.tar.gz     100%[==============================================>]  17.01K  --.-KB/s    in 0.009s  

2016-10-29 20:40:42 (1.92 MB/s) - ‘example_build_hcp.tar.gz’ saved [17419/17419]


$ tar -zxvf example_build_hcp.tar.gz

example_build_hcp/                                                                                                   
example_build_hcp/p1.fasta
example_build_hcp/p2.fasta
example_build_hcp/p3.fasta
example_build_hcp/p4.fasta
example_build_hcp/p5.fasta
example_build_hcp/p6.fasta
example_build_hcp/p7.fasta
example_build_hcp/p8.fasta
example_build_hcp/p9.fasta
example_build_hcp/p10.fasta
```

Check each highly conserved proteins in each files:


```bash
$ cd  example_build_hcp/
$ cat p1.fasta 
>aeh
MARLTKRQKAIREKIDPAQQYPVAEALGLLRELPGAKFTESVEVAVNLGVDPRKSDQIVR
GSTVLPNGTGKTVRVAVFAQGDAAEAAKEAGADIVGMDDLAEQVKGGNLDFDVVVAAPDA
MGVVGRLGPILGPRGLMPNPKVGTVTPDVAGAVKNAKAGQVRYRTDKGGIIHCAIGKVDF
EVEALQQNLQALITDLQKLKPANSKGVYLKKVAVSTTMGPGLAVDLASLET
>adk
MAKLTKKQKAQQGKVDSTKLYPFAEAVALVKEAATAKFDESIDVAVQLGVDAKKSDQVVR
GAVVLPNGTGKTTRVAVFAQGAKAEEAKAAGADVVGMDDLAAQVKAGDMPFDVVIAAPDA
MRVVGTLGQILGPRGLMPNPKVGTVTPDVATAVKNAKAGQVQFRVDKAGIVHTTIGRRSF
ADDKLQGNLAALIEALNKAKPATSKGVYLRKVAVSSTMGVGVRVDTQSIAA
>acp
MAHVAKKYKAAAEKVDRTKRYKLDEAMSLVKQTATKKFDETVDASINLGVDPKHADQVVR
GAVVLPHGMGKTVRLAVFAKGDKAKEAQEAGADIVGAEDLAEKIQGGFMDFDKLIATPDM
MGVVGRLGKILGPRGLMPNPKVGTVTMDLARAVKEQKAGKVEFRVEKAGIVHVPFGKASF
DPDKLKANFSAIMEVIYKAKPQTAKGVYVKNVTLSTTMGPGIKVDLAELAAQHA
>acn
MSGDGSSYSAEEGIRELLQSAKAKFRESVDVAIKLSVADSKSGESVRGAVVLPKGLGREV
RVAVFAKGEHAKHASDAGADVVGDEELIEEIKKGRKLDVDWCIATPDFMPQISAIAKILG
PRGLMPNPKFGTVTLELAKMVGVIKSGQVKFKSDRYGIVHVKIGDVSFTPEDLLENFNAV
VVAVQNLKPATIKGSYVRGVFVNSTMGRSFRIAGIG
>adg
MPKHGKKYLEAKKQVDRTKLYDPYEALELVKRLASAKFDETVEVAVRLGVDPRHADQQVR
GAVVLPHGTGKTRRVLVFARGEKAKEAEAAGADYVGAEDLIARIQGGWLDFDVAIATPDM
MAMVGRIGRILGPRGLMPNPKTGTVTFDVAQAVAEAKAGRVEYRTDKAGIVHAPIGKVSF
EVEKLVENLKALVDALVRAKPPAAKGQYLRSITVSSTMGPGVKVNPAKLLAS
>acl
MKRGKKYLEAVKLYDKSVAYTGLEAVELAKKTSVAKFDATVEVAFRLNVDPRKADQNLRG
AISLPHGTGKTVRVVVIAKPEKAKEALAAGALEAGDVELIDKIGKGWFDFDVMVATPDMM
AQLGKLGRVLGPKGLMPNPKTGTVTLDVAKAVEEIKAGKIEYRTDKVGNIHAPIGKVSFD
SNKLHENMLAIYNQLVRIKPATVKGTYIKKIALSTTMGPGIMVEENNIKK
>ace
MKRGKKYRAAAQLVDRTKLYSPLEAMRLAKQTNTMRVPATVEVAMRLGVDPRKADQMVRG
TVNLPHGTGKTPRVLVFATAERAEEARAAGADYVGADELIEQVANGFLDFDAVVATPDLM
GKVGRLGRILGPRGLMPNPKTGTVTNDVAKAVADIKSGKIEFRVDRQANLHLVIGKTDFT
EQQLVENYAAALDEVLRLKPPTAKGRYLKKVTISTTMGPGIPVDPNRVRNLLAEETAAA
>aeq
MTKHGKKYVEAEKQIPAEPVSPLAAMKLLKEISVANFDETVTGDFRLGIDTRQADQQLRG
TVSLPNGSGKTVRVAVFAEGAAAQAAEEAGADIVGTDELMQQIQAGEFNFDAAVATPDQM
GKVGRLGKILGPRGLMPNPKLGTVTNDVAKAIKELKGGRVEYRADRYGIAHVVLGKVSFT
PEQLAENYGAVYDEILRMKPAAAKGKYVKSITVSGTMTPGVSVDSSVTRAYTESAE
>aca
MSKKVSKNVAKARAAVEPRPYTLQDAVPLLQQVKFAKFDETVDLTMRLGVDPRHADQMVR
GTVVLPHGLGKTKKVAVITTGDRQKEAEAAGAEIVGGEELVEKIQKESWTDFDALIATPD
MMRSVGRLGKVLGPRGLMPNPKTGTVTNDVAAAVKEIKAGKIEYRTDKTALVHVPVGKLS
FPAEKLIDNAMTVITSVVRAKPSAAKGKYIKGITLSSTMGPGIPLDGSVADAAAKA
>aco
MAKKSKRYSEIAAKVDSTKLYGLREAVDLYKEVATAKFDESLEVHIRLGVDPRHADQQVR
GTIVLPHGTGITKRVLVLAVGEKVKEAEDAGADIVGGDDLIQKISTGWLDFDAVIATPDM
MKSVGRLGKILGPRGLMPSAKAGTVTFDVADAIKEIKAGRVEFRVDKTAIIHNMVGKKSF
EAEKLFENLKVLYRAILKARPASAKGTYVRSFYIAPTMGVGIKIDPVAASKEVAEA
```

 
Reconstruct phylogenetic tree by follow command:

```bash
PhySpeTree build -i example_build_hcp -o build_hcp_tree --hcp
```


Few seconds reconstruct phylogenetic tree completed and tree file were stored in `build_hcp_tree` directory.

`NOTE`:

* Prepare how many highly proteins which users decide, we recommend not less than 10 highly conserved proteins.
* Each proteins files must have the same organisms sequence.


#### **Build phylogenetic tree by SSU rRNA**

Use `build` command to construct phylogenetic tree by SSU rRNA sequence, users should prepare a FASTA format file
contain each species SSU rRNA sequence as [example_build_srna][4]. In this example contain ten species SSU rRNA sequence.


Download [example_build_srna][4] and check the organisms names:

```
$ wget "https://xiaofeiyangyang.github.io/physpetools/example/example_build_srna.fasta"
--2016-10-29 20:56:31--  https://xiaofeiyangyang.github.io/physpetools/example/example_build_srna.fasta
Resolving xiaofeiyangyang.github.io (xiaofeiyangyang.github.io)... 151.101.48.133
Connecting to xiaofeiyangyang.github.io (xiaofeiyangyang.github.io)|151.101.48.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 14982 (15K) [application/octet-stream]
Saving to: ‘example_build_srna.fasta’

example_build_srna.fasta     100%[==============================================>]  14.63K  --.-KB/s    in 0.005s  

2016-10-29 20:56:33 (3.14 MB/s) - ‘example_build_srna.fasta’ saved [14982/14982]

$ grep '>' example_build_srna.fasta 
>aca
>ace
>acl
>acn
>aco
>acp
>adg
>adk
>aeh
>aeq
```

Reconstruct phylogenetic tree  by follow command:

```bash
PhySpeTree build -i example_build_srna.fasta -o build_srna_tree --srna
```

Few seconds reconstruct phylogenetic tree completed and tree files were stored in `build_srn_tree` directory


### Advance options

Users enable choice more detail options with PhySpeTree call software, detail advance options input
`must be enclosed in single quotes and Start with a space`.

The following is an example of using RAxML advanced options:

```bash
$ PhySpeTree -i organism_example_list.txt --raxml '-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1'
```

**--muscle**

  Multiple sequence alignment by muscle. The default multiple sequence alignment software is Muscle.


**--muscle_p**

  Set Muscle advance parameters. The default is ``-maxiter 100``. More options about muslce please to see [MUSCLE Manual](http://www.drive5.com/muscle/manual/options.html)

The default option:

|  option   | description                                      |
|:----------|:-------------------------------------------------|
|  -maxiter | maximum number of iterations to run is set 100.  |


**--clustalw**

    Multiple sequence alignment by clustalw2.

**--clustalw_p**

  Set clustalw2 advance parameters. Here use clustalw default parameters. More options about clustalw please to see [Clustalw Help](http://www.clustal.org/download/clustalw_help.txt).


**--gblocks**

  Set Gblocks advance parameters. The default is ``-t=p -e=-gb1``. More options about Gblocks please to see [Gblocks documentation](http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_documentation.html).

The default option:

|  option | description                                                 |
|:--------|:------------------------------------------------------------|
|  -t     | Choice type of sequence. The PhySpeTree default set is protein. |
|  -e     | Eneric file extensionc. PhySpeTree set default is -gbl1.        |


**--ranxml**

    Reconstruct phylogenetic tree by RAxML. The default build tree software is RAxML.



**--raxml_p**

  Set reconstruct phylogenetic tree arguments with RAxML. The default is ``-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1``. More options about RAxMl please to see [RAxML Manual](http://sco.h-its.org/exelixis/resource/download/NewManual.pdf).

The default option:

|  option | description                                                                                                                              |
|:--------|:---------------------------------------------------------------------------------------------------------------------------------------- |
|   -f    |  select algorithm. The PhySpeTree default set is ``a``, rapid Bootstrap analysis and search for best­scoring ML tree in one program run. |
|   -m    |  Model of Binary (Morphological), Nucleotide, Multi­State, or Amino Acid Substitution. The PhySpeTree default set is PROTGAMMAJTTX.      |
|   -p    |  Specify a random number seed for the parsimony inferences. The physep default set is 12345.                                             |
|   -x    |  Specify an integer number (random seed) and turn on rapid bootstrapping. The PhySpeTree default set is 12345.                           |
|   -N    |  The same with -# specify the number of alternative runs on distinct starting trees. The PhySpeTree default set is 100.                  |


**--fasttree**
    
  Reconstruct phylogenetic tree by FastTree.

**--fasttree_p**
    
  Set more FastTree advance parameters. More options about clustalw please to see [FastTree](http://www.microbesonline.org/fasttree/).


## combine


The **combine** module for the consensus tree construction.


In Linux you can easy combine more tree to a tree file, for example:

```bash
$ cat tree1.tree tree2.tree > combineTree.tree

```

Use **combine** in command line like this:


```bash
$ PhySpeTree combine -i combineTree.tree [options]*
```

### Combine options


| option  | Description  |
|---|---------------------------------|
|  -h |  Print help message and exits. |
|  -i |  Input a tree file (PHYLIP format), which contain multiple tree. |
|  -o |  A directory contain combine tree file. The default output data name is combineTree. |
|  --mr |  Compute majority rule consensus tree.  |
|  --mre |  Compute extended majority rule consensus tree.  |
| --strict |  Compute strict consensus tree.  |

### example

Users can use combine command to combine tree from different method method, in our example combine tree from two way reconstruct
The `tree1.tree` reconstruct by highly conserved proteins, the `tree2.tree` reconstructed by SSU rRNA data, exapmel data
[example_combine_tree.tar.gz][5]

Download [example_combine_tree.tar.gz][5] and unpack:


```bash
$ tar -zxvf example_combine_tree.tar.gz 
example_combine_tree/
example_combine_tree/tree2.tree
example_combine_tree/tree1.tree
```

Combine tree1.tree and tree2.tree to a tree file:


```bash
$ conbine tree1.tree tree2.tree > combine.tree
```



Combine tree command as like this:

```bash
PhySpeTree combine -i combine.tree -o combineTree
```


In the combineTree directory contain two files:

```
combine/
        RAxML_info.T1
        RAxML_MajorityRuleConsensusTree.T1
```

* RAxML_info.T1: The info of RAxML
* RAxML_MajorityRuleConsensusTree.T1: The combine tree by Majority Rule method.



## iview

PhySpeTree provide annotating tree by iTol use iview module. Users can use iview command to color tree range by kingdom, phylum, class or order.
the range annotated files can used in [iTol](http://itol.embl.de/), iTol is a very popular online tool for the display, 
annotation and management of phylogenetic trees. More detail with of iTol in [iTol help](http://itol.embl.de/help.cgi) 


Use **iview** in command line like this:

```bash
$ PhySpeTree iview -i organism_example_list.txt -range phylum
```

### iview options

| option | Description                                                                                         |
|:-------|:----------------------------------------------------------------------------------------------------|
|  -h    |  Print help message and exits.                                                                      |
|  -i    |  Input a TXT file contain species names (abbreviated names) are same with KEGG species abbreviation.|
|  -o    |  A directory contain range text file. The directory name is iview.                                  |
|  -a    |  Colored ranges by users assign, users can choice from \[kingdom, phylum, class and order\].        |
| -r/--range   | Annotating ranges by kingdom, phylum, class or order. The default is phylum.                  |
| -l/--labels  | Change species labels from abbreviated names to full names.                                   |


### example

iview Annotating tree by kingdom, phylum, class or order example, download example [organism_example_list.txt][1]


#### Annotating tree by kingdom

```bash
$ PhySpeTree iview -i organism_example_list.txt --range kingdom
Color range by kingdom was complete.
```

The color range type data are store in iview directory:

```bash
$ cd iview
$ cat range_color_by_kingdom.txt 
TREE_COLORS
SEPARATOR TAB
DATA
aca     range   #BEBF5A Prokaryotes
ace     range   #BEBF5A Prokaryotes
acl     range   #BEBF5A Prokaryotes
acn     range   #BEBF5A Prokaryotes
aco     range   #BEBF5A Prokaryotes
acp     range   #BEBF5A Prokaryotes
adg     range   #BEBF5A Prokaryotes
adk     range   #BEBF5A Prokaryotes
aeh     range   #BEBF5A Prokaryotes
aeq     range   #BEBF5A Prokaryotes
```

#### Annotating tree by phylum

```bash
$ PhySpeTree iview -i organism_example_list.txt --range phylum
Color range by phylum was complete.
```

The color range type data are store in iview directory:

```bash
$ cd iview
$ cat range_color_by_phylum.txt 
TREE_COLORS
SEPARATOR TAB
DATA
aca     range   #865142 Bacteria
ace     range   #865142 Bacteria
acl     range   #865142 Bacteria
acn     range   #865142 Bacteria
aco     range   #865142 Bacteria
acp     range   #865142 Bacteria
adg     range   #865142 Bacteria
adk     range   #865142 Bacteria
aeh     range   #865142 Bacteria
aeq     range   #865142 Bacteria
```

#### Annotating tree by class

```bash
$ PhySpeTree iview -i organism_example_list.txt --range class
Color range by class was complete.
```

The color range type data are store in iview directory:

```bash
$ cd iview
$ cat range_color_by_class.txt 
TREE_COLORS
SEPARATOR TAB
DATA
aca     range   #9AB7F3 Acidobacteria
ace     range   #99D1DB Actinobacteria
acl     range   #A5E58D Tenericutes
acn     range   #94F1C1 Alphaproteobacteria
aco     range   #D67A21 Synergistetes
acp     range   #DD9284 Deltaproteobacteria
adg     range   #3E70B8 Firmicutes - Clostridia
adk     range   #DDC8B7 Betaproteobacteria
aeh     range   #72E137 Gammaproteobacteria - Others
aeq     range   #99D1DB Actinobacteria
```

#### Annotating tree by order

```bash
$ PhySpeTree iview -i organism_example_list.txt --range order
Color range by order was complete.
```

The color range type data are store in iview directory:

```bash
$ cd iview
$ cat range_color_by_order.txt 
TREE_COLORS
SEPARATOR TAB
DATA
aca     range   #AA8761 Acidobacterium
ace     range   #8770BC Acidothermus
acl     range   #3BD26B Acholeplasma
acn     range   #D1B487 Anaplasma
aco     range   #D96D21 Aminobacterium
acp     range   #AC4E16 Anaeromyxobacter
adg     range   #287AD8 Ammonifex
adk     range   #C8184E Alicycliphilus
aeh     range   #57A569 Alkalilimnicola
aeq     range   #F1A2B7 Adlercreutzia
```


## check


The check module can check input organisms match in KEGG database or SSU rRNA database.


```bash
$ PhySpeTree check -i organism_example_list.txt -out check --ehcp
```


### check options


| option | Description                                                                                         |
|:-------|:----------------------------------------------------------------------------------------------------|
|  -h    |  Print help message and exits.                                                                      |
|  -i    |  Input a TXT file contain species names (abbreviated names) are same with KEGG species abbreviation.|
|  -o    |  A directory contain check result. The directory name is check.                                     |
| --hcp  |  Check organisms whether supported by KEGG database.                                                |
| --ehcp |  Check input organisms prepare for extend autobuild tree module.                                    |
| --srna |  Check organisms whether supported by SILVA database.                                               |

### example


#### check organism for extend autobuild

When users use autobuild to reconstruct phylogenetic tree with `--ehcp` method, you should prepare highly conserved proteins as extend proteins
for auto build tree. You can determine what proteins to be prepared by the check command. Download example for check [organism_example_list.txt][1]


Use check command like follow: 

```bash
$ PhySpeTree check -i organism_example_list.txt --ehcp

'Ribosomal protein L1' ----------------------------------> p1.fasta

'DNA-directed RNA polymerase subunit alpha' ----------------------------------> p2.fasta

'Leucyl-tRNA synthetase' ----------------------------------> p3.fasta

'Metal-dependent proteases with chaperone activity' ----------------------------------> p4.fasta

'Phenylalanine-tRNA synthethase alpha subunit' ----------------------------------> p5.fasta

'Predicted GTPase probable translation factor' ----------------------------------> p6.fasta

'Ribosomal protein L11' ----------------------------------> p7.fasta

'Ribosomal protein L13' ----------------------------------> p8.fasta

'Ribosomal protein L14' ----------------------------------> p9.fasta

'Ribosomal protein L22' ----------------------------------> p10.fasta

'Ribosomal protein L3' ----------------------------------> p11.fasta

'Ribosomal protein L5' ----------------------------------> p12.fasta

'Ribosomal protein S11' ----------------------------------> p13.fasta

'Ribosomal protein S17' ----------------------------------> p14.fasta

'Ribosomal protein S2' ----------------------------------> p15.fasta

'Ribosomal protein S3' ----------------------------------> p16.fasta

'Ribosomal protein S4' ----------------------------------> p17.fasta

'Ribosomal protein S5' ----------------------------------> p18.fasta

'Ribosomal protein S7' ----------------------------------> p19.fasta

'Ribosomal protein S8' ----------------------------------> p20.fasta

'Ribosomal protein S9' ----------------------------------> p21.fasta

'Seryl-tRNA synthetase' ----------------------------------> p22.fasta

'Arginyl-tRNA synthetase' ----------------------------------> p23.fasta

'DNA-directed RNA polymerase beta subunit' ----------------------------------> p24.fasta

'Ribosomal protein S13' ----------------------------------> p25.fasta

Check extend highly conserved protein is completed.

```

This check result write to default directory name is `check`

```bash
$ cd check
$ cat physpe_echp_extend.txt 
'Ribosomal protein L1' ----------------------------------> p1.fasta
'DNA-directed RNA polymerase subunit alpha' ----------------------------------> p2.fasta
'Leucyl-tRNA synthetase' ----------------------------------> p3.fasta
'Metal-dependent proteases with chaperone activity' ----------------------------------> p4.fasta
'Phenylalanine-tRNA synthethase alpha subunit' ----------------------------------> p5.fasta
'Predicted GTPase probable translation factor' ----------------------------------> p6.fasta
'Ribosomal protein L11' ----------------------------------> p7.fasta
'Ribosomal protein L13' ----------------------------------> p8.fasta
'Ribosomal protein L14' ----------------------------------> p9.fasta
'Ribosomal protein L22' ----------------------------------> p10.fasta
'Ribosomal protein L3' ----------------------------------> p11.fasta
'Ribosomal protein L5' ----------------------------------> p12.fasta
'Ribosomal protein S11' ----------------------------------> p13.fasta
'Ribosomal protein S17' ----------------------------------> p14.fasta
'Ribosomal protein S2' ----------------------------------> p15.fasta
'Ribosomal protein S3' ----------------------------------> p16.fasta
'Ribosomal protein S4' ----------------------------------> p17.fasta
'Ribosomal protein S5' ----------------------------------> p18.fasta
'Ribosomal protein S7' ----------------------------------> p19.fasta
'Ribosomal protein S8' ----------------------------------> p20.fasta
'Ribosomal protein S9' ----------------------------------> p21.fasta
'Seryl-tRNA synthetase' ----------------------------------> p22.fasta
'Arginyl-tRNA synthetase' ----------------------------------> p23.fasta
'DNA-directed RNA polymerase beta subunit' ----------------------------------> p24.fasta
'Ribosomal protein S13' ----------------------------------> p25.fasta
```

In `physpe_echp_extend.txt` file you can check the highly conserved protein, which you should prepare for extend hcp method to reconstruct phylogenetic tree.







[1]: example/organism_example_list.txt
[2]: http://www.genome.jp/kegg/catalog/org_list.html
[3]: example/example_build_hcp.tar.gz
[4]: example/example_build_srna.fasta
[5]: example/example_combine_tree.tar.gz