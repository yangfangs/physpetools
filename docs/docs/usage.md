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

#### **Auto build phylogenetic tree by highly conserved proteins:**

```bash
$ physpe autobuild -i organism_example_list.txt --hcp
Loading organisms names success.....

The result are store in:Outdata

now loading data and constructing species phylogenetic tree......
Now loading data and constructing species phylogenetic tree......
2016-08-18 15:32:06,770 kegg DB INFO: Read organisms names successful
2016-08-18 15:32:08,380 kegg DB INFO: Retrieve highly conserved protein 'Ribosomal protein L1' success and store in p1.fasta file
2016-08-18 15:32:09,702 kegg DB INFO: Retrieve highly conserved protein 'DNA-directed RNA polymerase subunit alpha' success and store in p2.fasta file
2016-08-18 15:32:11,352 kegg DB INFO: Retrieve highly conserved protein 'Leucyl-tRNA synthetase' success and store in p3.fasta file
2016-08-18 15:32:12,786 kegg DB INFO: Retrieve highly conserved protein 'Metal-dependent proteases with chaperone activity' success and store in p4.fasta file
2016-08-18 15:32:14,318 kegg DB INFO: Retrieve highly conserved protein 'Phenylalanine-tRNA synthethase alpha subunit' success and store in p5.fasta file
2016-08-18 15:32:15,854 kegg DB INFO: Retrieve highly conserved protein 'Predicted GTPase probable translation factor' success and store in p6.fasta file
2016-08-18 15:32:17,049 kegg DB INFO: Retrieve highly conserved protein 'Ribosomal protein L11' success and store in p7.fasta file
2016-08-18 15:32:18,316 kegg DB INFO: Retrieve highly conserved protein 'Ribosomal protein L13' success and store in p8.fasta file

```

When auto reconstruct phylogenetic tree by `hcp` method was completed, you will get file layout like this:

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
        + concatenate.fasta-gb1: Select conserved blocks result (by Gblocks).
        + concatenate.fasta-gb1.htm: Select conserved blocks result view by html format.
        + concatenate.fasta-gb1.phy: Convert FASTA format to PHYLIP format


####  **Auto build phylogenetic tree by 16s SSU RNA:**


```bash
$ physpe autobuild -i organism_example_list.txt --srna
Loading organisms names success.....

The result are store in:Outdata

Now loading data and constructing species phylogenetic tree......
2016-08-18 15:29:31,528 16s DB INFO: Read organisms names success
2016-08-18 15:29:38,166 16s DB INFO: Retrieve organism 'aca' 16s SSU RNA sequences data success
2016-08-18 15:29:40,236 16s DB INFO: Retrieve organism 'ace' 16s SSU RNA sequences data success
2016-08-18 15:29:42,356 16s DB INFO: Retrieve organism 'acl' 16s SSU RNA sequences data success
2016-08-18 15:29:44,615 16s DB INFO: Retrieve organism 'acn' 16s SSU RNA sequences data success
2016-08-18 15:29:46,868 16s DB INFO: Retrieve organism 'aco' 16s SSU RNA sequences data success
2016-08-18 15:29:49,119 16s DB INFO: Retrieve organism 'acp' 16s SSU RNA sequences data success
2016-08-18 15:29:51,392 16s DB INFO: Retrieve organism 'adg' 16s SSU RNA sequences data success

```


When auto reconstruct phylogenetic tree by `srna` method was completed, you will get file layout like this:

```
log.log
Outdata/
        RAxML_bestTree.T1
        RAxML_bipartitions.T1
        RAxML_bipartitionsBranchLabels.T1
        RAxML_bootstrap.T1
        RAxML_info.T1
   temp/
        16srnadata20160818145209/
                                 16srandata.fasta

        16srna_alignment20160818145236/
                                  16srandata.fasta
                                  16srandata.fasta-gb1
                                  16srandata.fasta-gb1.htm
                                  16srandata.fasta-gb1.phy
```

* log.log: The log information of physpe.
* Outdata: Contain phylogenetic tree output result. 
    
    - RAxML_bestTree.T1: Reconstruct phylogenetic tree by RAxML, it's best ML search tree. 
    - RAxML_bipartitions.T1: Bipartition tree by RAxML.
    - RAxML_bipartitionsBranchLabels.T1: Bipartition tree by constructed by RAxML with branch length lables.
    - RAxML_bootstrap.T1: Bootstrap result by RAxML
    - RAxML_info.T1: The info of run RAxMl.
    
* temp: The temp data by physpe, `it's very important to user to check the key steps`.

    - 16srnadata: Contain 16s SSU RNA data retrieved form SILVA database.
    
        + 16srnadata.fasta: FASTA format data contain input organism 16s SSU RNA data.
         
    - 16srna_alignment: Contain the concatenate highly conserved proteins result and select conserved blocks data.
    
        + 16srandata.fasta: Contain 16s SSU RNA data with multiple sequence alignment already.
        + 16srandata.fasta-gb1: Select conserved blocks result (by Gblocks).
        + 16srandata.fasta-gb1.htm: Select conserved blocks result view by html format.
        + 16srandata.fasta-gb1.phy: Convert FASTA format to PHYLIP format


### Advance options

User enable choice more detail options with Physpe call software, detail advance options input
``must be enclosed in single quotes``.

The follow is to use RAxML advance options example:

```bash
$ physpe -i organism_example_list.txt --raxml '-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1'
```

**--muscle**

  Set multiple sequence alignment parameters. The default is ``-maxiter 100``. More options about muslce please to see [MUSCLE Manual](http://www.drive5.com/muscle/manual/options.html)

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




##  build

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


### example


#### **Build phylogenetic tree by highly conserved proteins**


When use build to reconstruct phylogenetic tree you should prepare a directory contain highly conserved proteins such as [example_build_hcp][3]. In this example
contain ten highly conserved proteins p1~p10, in each highly conserved proteins contain 10 organism.

Download [example_build_hcp][3] you can use the tar command to unpack:

```bash
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

 
Reconstruct phylogenetic tree ues example are by follow command:

```bash
physpe build -i example_build_hcp -o build_hcp_tree --hcp
```


Few seconds reconstruct phylogenetic tree completed and tree file are store in `build_hcp_tree` directory

`NOTE`:

* Prepare how many highly proteins which user decide, we recommend not less than 10 highly conserved proteins.
* Each protein must have the same organisms.


#### **Build phylogenetic tree by 16s RNA**

Use build command to construct phylogenetic tree by 16s RNA sequence, user should prepare a FASTA format file
contain each organisms 16s RNA sequence as [example_build_srna][4]. In this example contain ten organism 16s SSU RNA sequence.


Download [example_build_srna][4] and check the organisms names:

```bash
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

Reconstruct phylogenetic tree ues example are by follow command:

```bash
physpe build -i example_build_srna.fasta -o build_srna_tree --srna
```

Few seconds reconstruct phylogenetic tree completed and tree file are store in `build_srn_tree` directory


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


### example

User can use combine command to combine tree from different method method, in our example combine tree from two way reconstruct
The `tree1.tree` reconstruct by highly conserved proteins, the `tree2.tree` reconstruct by 16s SSU RNA data, exapmel data
[example_combine_tree.tar.gz][4]

Download [example_combine_tree.tar.gz][4] and unpack:


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
physpe combine -i combine.tree -o combineTree
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

Annotating tree by iTol use iview module. User can use iview command to color tree range by kingdom, phylum, class or order.
the range annotation files can used in [iTol](http://itol.embl.de/), iTol is a very popular online tool for the display, 
annotation and management of phylogenetic trees. More detail with of iTol in [iTol help](http://itol.embl.de/help.cgi) 


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
|  -r/--range    |Annotating ranges by kingdom, phylum, class or order. The default is phylum.                 |


### example

iview Annotating tree by kingdom, phylum, class or order example, download example [organism_example_list.txt][1]


#### Annotating tree by kingdom

```bash
$ physpe iview -i organism_example_list.txt --range kingdom
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
$ physpe iview -i organism_example_list.txt --range phylum
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
$ physpe iview -i organism_example_list.txt --range class
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
$ physpe iview -i organism_example_list.txt --range order
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
[3]: example/example_build_hcp.tar.gz
[3]: example/example_build_srna.fasta
[4]: example/example_combine_tree.tar.gz