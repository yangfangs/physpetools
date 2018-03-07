# Usage and Examples

## autobuild

The input of `autobuild` module is a TXT file containing [KEGG][2] abbreviated species names, for example [organism_example_list][1].

```bash
$ PhySpeTree -i autobuild organism_example_list.txt [options]*
```

### options

| option |  Description                                                                                                                            |
|:------- |:---------------------------------------------------------------------------------------------------------------------------------------|
|  -h     |  Print help message and exits.                                                                                                         |
|  -i     |  Input a TXT file containing abbreviated species names.                                                                                                               |
|  -o     |  A directory to store outputs. The default is "Outdata".                                                                                 |
|  -t     |  Number of processing threads (CPUs). The default is 1.                                                     |
|  -e     |  FASTA format files to extend the tree with the --ehcp or --esrna option.                                                              |
|  --hcp  |  HCP (highly conserved protein) method (default).                                                                                        |
|  --ehcp |  HCP method with extended HCP sequences.                                                                                               |
|  --srna |  SSU method.                                                                       |
|  --esrna|  SSU rRNA method with extended SSU rRNA sequences.                                                                                                           |


### example

Download the example input file:

```bash
$ wget "https://yangfangs.github.io/physpetools/example/organism_example_list.txt"

--2016-10-29 19:41:53--  https://yangfangs.github.io/physpetools/example/organism_example_list.txt
Resolving yangfangs.github.io (yangfangs.github.io)... 151.101.24.133
Connecting to yangfangs.github.io (yangfangs.github.io)|151.101.24.133|:443... connected.
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

**Automatically reconstruct species trees by HCP**

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

Outputs:

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


* `log.log`: logs.
* `Outdata`: tree files. 
    
    - `RAxML_bestTree.T1`: best ML search tree built by RAxML. 
    - `RAxML_bipartitions.T1`: bipartition tree built by RAxML.
    - `RAxML_bipartitionsBranchLabels.T1`: bipartition tree by RAxML with branch length.
    - `RAxML_bootstrap.T1`: bootstrap result.
    - `RAxML_info.T1`: logs in running RAxML.
    
* `temp`: temporary data used to check the quality of outputs in each step.

    - `conserved_protein`: highly conserved proteins retrieved from the KEGG database.
    - `alignment`: aligned sequences.
    - `concatenate`: concatenated sequences and conserved blocks.
    
        + `concatenate.fasta`: concatenated HCP sequences.
        + `concatenate.fasta-gb1`: conserved blocks (by Gblocks).
        + `concatenate.fasta-gb1.htm`: conserved blocks displayed in html.
        + `concatenate.fasta-gb1.phy`: conserved blocks in the PHYLIP format.

**Automatically reconstruct species trees by SSU rRNA**

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

Outputs:

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

* `log.log`: logs.
* `Outdata`: tree files like the HCP method.
* `temp`: temporary data used to check the quality of outputs in each step.

    - `rna_sequence`: SSU rRNA sequences retrieved from the SILVA database.
    - `rna_alignment`: aligned sequences and conserved blocks.
    
        + rna_sequence.fasta: aligned SSU rRNA sequences.
        + rna_sequence.fasta-gb1: conserved blocks (by Gblocks).
        + rna_sequence.fasta-gb1.htm: conserved blocks displayed in html.
        + rna_sequence.fasta-gb1.phy: conserved blocks in the PHYLIP format.


### Advanced options

Advanced options of internal software called in PhySpeTree can be set. These options are ``enclosed in single quotes and start with a space``.

Here is an example of setting RAxML advanced options by `--raxml_p`:

```bash
$ PhySpeTree autobuild -i organism_example_list.txt -o test --srna --raxml --raxml_p ' -f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1'
```

**--muscle**

> Multiple sequence alignment by MUSCLE (default).

**--muscle_p**

> Set MUSCLE advanced parameters, please see <a href="http://www.drive5.com/muscle/manual/options.html">MUSCLE Manual</a>

The default option:

|  option   | description                                      |
|:----------|:-------------------------------------------------|
|  -maxiter | Maximum number of iterations to run. The default is 100. |

**--clustalw**

> Multiple sequence alignment by ClustalW2.

**--clustalw_p**

> Set ClustalW2 advanced parameters, please see [Clustalw Help](http://www.clustal.org/download/clustalw_help.txt).

**--mafft**

>Multiple sequence alignment by mafft.

**--mafft_p**

>Set mafft advance parameters. Here use mafft default parameters, please see [mafft algorithms](http://mafft.cbrc.jp/alignment/software/algorithms/algorithms.html)


**--gblocks**

>Trim by Gblocks.(default)

**--gblocks_p**

> Set Gblocks advanced parameters, please see [Gblocks documentation](http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_documentation.html).

The default option:

|  option | description                                                 |
|:--------|:------------------------------------------------------------|
|  -t     | Choice type of sequence (default).                                        |
|  -e     | Generic file extension. The default in PhySpeTree is "-gbl1".     |

**--trimal**

> Trim by trimal.

**--trimal_p**

> Set trimal advance parameters, please see[trimal command line](http://trimal.cgenomics.org/use_of_the_command_line_trimal_v1.2)

**--ranxml**

> Reconstruct species tree by RAxML (default).

**--raxml_p**

> Set RAxML advanced parameters, please see [RAxML Manual](http://sco.h-its.org/exelixis/resource/download/NewManual.pdf).

The default option:

|  option | description                                                                                                                          |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------ |
|   -f    |  select algorithm. The default in PhySpeTree is ``a``, rapid Bootstrap analysis and search for best­scoring ML tree in one program run.  |
|   -m    |  Model of binary (morphological), nucleotide, multi­State, or amino acid substitution. The PhySpeTree default set is PROTGAMMAJTTX.      |
|   -p    |  Specify a random number seed for the parsimony inferences. The default in PhySpeTree is 12345.                                |
|   -x    |  Specify an integer number (random seed) and turn on rapid bootstrapping. The default in PhySpeTree is 12345.                            |
|   -N    |  The same with -# specify the number of alternative runs on distinct starting trees. The default in PhySpeTree is 100.                   |

**--fasttree**

> Reconstruct species tree by FastTree.

**--fasttree_p**
    
> Set FastTree advanced parameters, please see [FastTree Helps](http://www.microbesonline.org/fasttree/).

## build

The `build` module is used to reconstruct species trees with manually prepared sequences. Advanced options are the same as `autobuild` module.

```bash
# multiple method
$ PhySpeTree build -i example_hcp -o output --multiple

# single method
$ PhySpeTree build -i example_16s_ssurna.fasta -o output --single
```

### build options

| option |  Description                                                                                                                            |
|:------- |:---------------------------------------------------------------------------------------------------------------------------------------|
|  -h     |  Print help message and exits.                                                                                                         |
|  -i     |  Input a TXT file containing abbreviated species names.                               |
|  -o     |  A directory to store outputs. The default is "Outdata".                                                   |
|  -t     |  Number of processing threads (CPUs). The default is 1.                                                                                                                                      |
|  --multiple  |  Specify concatenate highly conserved protein method to reconstruct phylogenetic tree.                                                                                |
|  --single |  Use SSU rRNA data to reconstruct phylogenetic tree.                                                                                     |


### example

**Build species trees by manually prepared HCP**

The HCP sequences belonging to the same class are prepared in one FASTA format file, and all FASTA format files are stored in the same folder. For example, the folder [example_build_hcp][3] contains 10 classes of HCP (p1~p10) corresponding to 10 different organisms. There is no limit number of HCP sequences. We recommend no less than 10 highly conserved proteins to ensure the accuracy of the reconstructed phylogenetic tree.

Download and decompress the example input file:

```bash

$ wget "https://yangfangs.github.io/physpetools/example/example_build_hcp.tar.gz"

--2016-10-29 20:40:41--  https://yangfangs.github.io/physpetools/example/example_build_hcp.tar.gz
Resolving yangfangs.github.io (yangfangs.github.io)... 151.101.48.133
Connecting to yangfangs.github.io (yangfangs.github.io)|151.101.48.133|:443... connected.
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

Check HCP:


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

 
Reconstruct species tree and store outputs in the `build_hcp_tree` folder:

```bash
PhySpeTree build -i example_build_hcp -o build_hcp_tree --multiple
```

**Build species trees by manually prepared SSU rRNA**

All SSU rRNA sequences are prepared in one FASTA format file, for example [example_build_srna][4].

Download and decompress the example input file:

```
$ wget "https://yangfangs.github.io/physpetools/example/example_build_srna.fasta"

--2016-10-29 20:56:31--  https://yangfangs.github.io/physpetools/example/example_build_srna.fasta
Resolving yangfangs.github.io (yangfangs.github.io)... 151.101.48.133
Connecting to yangfangs.github.io (yangfangs.github.io)|151.101.48.133|:443... connected.
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

Reconstruct species tree and store outputs in the `build_srna_tree` folder:

```bash
PhySpeTree build -i example_build_srna.fasta -o build_srna_tree --single --fasttree
```

## combine

The **combine** module is used to combine trees generated from different methods. It contains two steps, at first merge different tree files into the same file. You can use `cat` bash command in the Linux system, for example:

```bash
$ cat tree1.tree tree2.tree > combineTree.tree
```

Then, use **combine**:

```bash
$ PhySpeTree combine -i combineTree.tree [options]*
```

### combine options


| option  | Description  |
|---|---------------------------------|
|  -h |  Print help message and exits. |
|  -i |  Input PHYLIP format file containing multiple trees.                                                                                  |
|  -o |  Output directory. The default is "combineTree".                                                                                                                   |
|  --mr |  Majority rule trees.                   |
|  --mre |  Extended majority rule trees.                   |
| --strict |  Strict consensus trees.         |

### example

[example_combine_tree.tar.gz][5] contains `tree1.tree` and `tree2.tree` reconstructed by the HCP and SSU rRNA method, respectively.

Download and decompress the example input file:

```bash

$ wget "https://yangfangs.github.io/physpetools/example/example_combine_tree.tar.gz"

--2016-10-30 13:32:06--  https://yangfangs.github.io/physpetools/example/example_combine_tree.tar.gz
Resolving yangfangs.github.io (yangfangs.github.io)... 151.101.48.133
Connecting to yangfangs.github.io (yangfangs.github.io)|151.101.48.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 661 [application/octet-stream]
Saving to: ‘example_combine_tree.tar.gz’

example_combine_tree.tar.gz  100%[==============================================>]     661  --.-KB/s    in 0s      
                                                                                                                    
2016-10-30 13:32:07 (380 MB/s) - ‘example_combine_tree.tar.gz’ saved [661/661] 


$ tar -zxvf example_combine_tree.tar.gz 
example_combine_tree/
example_combine_tree/tree2.tree
example_combine_tree/tree1.tree
```

Merge `tree1.tree` and `tree2.tree`:

```bash
$ cd example_combine_tree/
$ cat tree1.tree tree2.tree > combine.tree
```
Combine trees:

```bash
PhySpeTree combine -i combine.tree -o combineTree
```

Outputs:
update PhySpeTree work follow fig
```
combine/
        RAxML_info.T1
        RAxML_MajorityRuleConsensusTree.T1
```

* `RAxML_info.T1`: logs in running RAxML.
* `RAxML_MajorityRuleConsensusTree.T1`: the majority rule consensus tree.

## iview

PhySpeTree provides the `iview` module to annotate taxonomic information (kingdom, phylum, class, or order) of output trees and to generate configure files linked to [iTol](http://itol.embl.de/).

```bash
$ PhySpeTree iview -i organism_example_list.txt --range
```

### iview options

| option | Description                                                                                         |
|:-------|:----------------------------------------------------------------------------------------------------|
|  -h    |  Print help message and exits.                                                                      |
|  -i    |  Input a TXT file containing abbreviated species names.  |
|  -o    |  A directory to store outputs. The default is "iview".                                            |
|  -a    |  Colored ranges \[kingdom, phylum, class or order\].           |
| -r/--range   | Annotating labels with ranges by kingdom, phylum, class or order. The default is phylum.                  |
|-c/--color|Annotating labels without ranges by kingdom, phylum, class or order. The default is phylum.|
| -l/--labels  | Change species labels from abbreviated names to full names.                                   |


### example

Download the example file:

```bash
$ wget "https://yangfangs.github.io/physpetools/example/organism_example_list.txt"

--2016-10-30 13:40:48--  https://yangfangs.github.io/physpetools/example/organism_example_list.txt
Resolving yangfangs.github.io (yangfangs.github.io)... 151.101.48.133
Connecting to yangfangs.github.io (yangfangs.github.io)|151.101.48.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 39 [text/plain]
Saving to: ‘organism_example_list.txt’

organism_example_list.txt    100%[==============================================>]      39  --.-KB/s    in 0s      

2016-10-30 13:40:50 (21.5 MB/s) - ‘organism_example_list.txt’ saved [39/39]
```

**Annotate the tree by kingdom**

```bash
$ PhySpeTree iview -i organism_example_list.txt --range -a kingdom
Color range by kingdom was complete.
```

The color range file is store in the `iview` folder:

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

**Annotate the tree by phylum**

```bash
$ PhySpeTree iview -i organism_example_list.txt --range -a phylum
Color range by phylum was complete.
```

The color range file is store in the `iview` folder:

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

**Annotate the tree by class**

```bash
$ PhySpeTree iview -i organism_example_list.txt --range -a class
Color range by class was complete.
```

The color range file is store in the `iview` folder:

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

**Annotate the tree by order**

```bash
$ PhySpeTree iview -i organism_example_list.txt --range -a order
Color range by order was complete.
```

The color range file is store in the `iview` folder:

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

The `check` module is used to check whether input organisms are in pre-built databases.

```bash
$ PhySpeTree check -i organism_example_list.txt --ehcp
```

### check options

| option | Description                                                                                         |
|:-------|:----------------------------------------------------------------------------------------------------|
|  -h    |  Print help message and exits.                                                                      |
|  -i    |  Input a TXT file containing abbreviated species names. |
|  -o    |  A directory to store outputs. The default is "check".                                      |
| --hcp  |  Check whether organisms are supported in the KEGG database.                                        |
| --ehcp |  Check input organisms prepare for extend autobuild tree module.                                    |
| --srna |  Check whether organisms are supported in the SILVA database.                                       |

### example

**Check extended organisms in `autobuild`**

Determine proteins to be prepared in the `autobuild` module with the `--ehcp` option, for example, [organism_example_list.txt][1]

Download the example file:

```bash
$ wget "https://yangfangs.github.io/physpetools/example/organism_example_list.txt"

--2016-10-30 13:40:48--  https://yangfangs.github.io/physpetools/example/organism_example_list.txt
Resolving yangfangs.github.io (yangfangs.github.io)... 151.101.48.133
Connecting to yangfangs.github.io (yangfangs.github.io)|151.101.48.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 39 [text/plain]
Saving to: ‘organism_example_list.txt’

organism_example_list.txt    100%[==============================================>]      39  --.-KB/s    in 0s      

2016-10-30 13:40:50 (21.5 MB/s) - ‘organism_example_list.txt’ saved [39/39]
```

Check: 

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

The check result is stored in the `check` folder. In `physpe_echp_extend.txt` file indicates class of HCP and their corresponding names, which will be used to prepare extended HCP sequences.

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

**Check whether input organisms are supported in PhySpeTree**

Check whether input species are supported by the KEGG database when using the `--hcp` method, for example [example download][6].

Download the example file:

```bash
$ wget "https://yangfangs.github.io/physpetools/example/191speciesnames.txt"

--2016-10-30 14:48:21--  https://yangfangs.github.io/physpetools/example/191speciesnames.txt
Resolving yangfangs.github.io (yangfangs.github.io)... 151.101.48.133
Connecting to yangfangs.github.io (yangfangs.github.io)|151.101.48.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 773 [text/plain]
Saving to: ‘191speciesnames.txt’

191speciesnames.txt          100%[==============================================>]     773  --.-KB/s    in 0s      

2016-10-30 14:48:22 (322 MB/s) - ‘191speciesnames.txt’ saved [773/773]
```

The check results show one organism named 'ges' is not supported in PhySpeTree:

```bash
$ PhySpeTree check -i 191speciesnames.txt --hcp
WARNING: The following species are not supported by KEGG DATABASE:
ges
Checked  whether the input species names in KEGG DATABASE completed.
```

Check whether input species are supported by SILVA database when using the `--srna` metho, for example [example download][6]
 
Download the example file:

```bash
$ wget "https://yangfangs.github.io/physpetools/example/191speciesnames.txt"

--2016-10-30 14:48:21--  https://yangfangs.github.io/physpetools/example/191speciesnames.txt
Resolving yangfangs.github.io (yangfangs.github.io)... 151.101.48.133
Connecting to yangfangs.github.io (yangfangs.github.io)|151.101.48.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 773 [text/plain]
Saving to: ‘191speciesnames.txt’

191speciesnames.txt          100%[==============================================>]     773  --.-KB/s    in 0s      

2016-10-30 14:48:22 (322 MB/s) - ‘191speciesnames.txt’ saved [773/773]
```

The check results show 28 organisms are not supported in PhySpeTree:

```bash

(progect) [yangfang@localhost test_check] $ PhySpeTree check -i 191speciesnames.txt --srna
WARNING: The following species are not supported by SILVA DATABASE:
neq
ape
tac
mmp
gla
tps
cho
ddi
spo
aga
tru
mpu
lin
ban
bce
ljo
san
spg
ges
lis
sco
cdi
mle
wsu
rpr
bpe
bpa
ppr
Checked  whether the input species names in SILVA DATABASE completed.
```

For organisms not in the pre-built list, PhySpeTree provides extend options (`--echp` or `--esrna`) to insert manually prepared sequences.


[1]: example/organism_example_list.txt
[2]: http://www.genome.jp/kegg/catalog/org_list.html
[3]: example/example_build_hcp.tar.gz
[4]: example/example_build_srna.fasta
[5]: example/example_combine_tree.tar.gz
[6]: example/191speciesnames.txt
