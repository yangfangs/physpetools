# Frequently Asked Questions (FAQ)


## PhySpeTree input/output


### 1.What preparation of user should does for PhySpeTree?

The users should prepare a TXT file, which contain species name (abbreviated names are same with [KEGG database](http://www.genome.jp/kegg/catalog/org_list.html).
one line write one species name only. For example,[organism_example_list](https://gitlab.com/xiaoxiaoyang/physpetools/raw/master/examples/organism_example_list.txt).
You can retrieve the Abbreviation of species names by [KEGG API](http://rest.kegg.jp/list/organism)


### 2.What's PhySpeTree output data mean?

PhySpeTree output two data files, the one is a result file default names is `Outdata`, another is a `temp` file.

If you reconstruct phylogenetic tree by `--hcp` (highly conserved protein) method, the temp files include three directory: `conserved_protein`, `alignment` and `concatenate`.

  * conserved_protein: Store the FASTA format files, which was highly conserved proteins retrieved by KEGG database.
  * alignment: Store the sequence files has been aligned.
  * concatenate: Include concatenated highly conserved proteins data (FASTA format) and selected conserved blocks data (\*.fasta-gb1 format file).

If you reconstruct phylogenetic tree by `--srna` (SSU rRNA) method, the temp files include two directory: `rna_sequence` and `rna_alignment`.

  * rna_sequence: Store a file named rna_sequence.fasta, contain the SSU rRNA sequence retrieved from SILVA database.
  * rna_alignment: Store in the \*.fasta file is the sequence files has been aligned and the \*.fasta-gb1, \*fasta-gb1.html are select conserved blocks data (use Gblocks software),
  the \*.phy format file is converted from has been select conserved blocks data by PhySpeTree.

`NOTE`:

* *Users can check the quality of every aspect of data by the corresponding temp files.*


## PhySpeTree reconstruct phylogenetic tree database

### 1.what's the highly conserved proteins be used to reconstruct phylogenetic tree?

PhySpeTree use 31 highly conserved proteins to reconstruct phylogenetic tree. This highly conserved proteins exclusion Horizontal Gene Transfers (HGTs) already.

**cite:**

> Ciccarelli F D, Doerks T, Von Mering C, et al. Toward automatic reconstruction of a highly resolved tree of life[J]. science, 2006, 311(5765): 1283-1287.

The 31 highly conserved proteins and corresponding KEGG database KO number as follow table:



Protein Names                                       |  Eukaryotes KO     |Prokaryotes KO
--------------------------------------------------- | ------------------ | ---------------
DNA-directed RNA polymerase subunit alpha           |   K03040           |   K03040
Ribosomal protein L1                                |   K02865           |   K02863
Leucyl-tRNA synthetase                              |   K01869           |   K01869
Metal-dependent proteases with chaperone activity   |   K01409           |   K01409
Phenylalanine-tRNA synthethase alpha subunit        |   K01889           |   K01889
Predicted GTPase probable translation factor        |   K06942           |   K06942
Preprotein translocase subunit SecY                 |   K10956           |   K10956
Ribosomal protein L11                               |   K02868           |   K02867
Ribosomal protein L13                               |   K02873           |   K02871
Ribosomal protein L14                               |   K02875           |   K02874
Ribosomal protein L15                               |   K02877           |   K17437
Ribosomal protein L16/L10E                          |   K02866           |   K02872
Ribosomal protein L18                               |   K02883           |   K02882
Ribosomal protein L22                               |   K02891           |   K02890
Ribosomal protein L3                                |   K02925           |   K02906
Ribosomal protein L5                                |   K02932           |   K02931
Ribosomal protein L6P/L9E                           |   K02940           |   K02939
Ribosomal protein S11                               |   K02949           |   K02948
Ribosomal protein S15P/S13E                         |   K02958           |   K02956
Ribosomal protein S17                               |   K02962           |   K02961
Ribosomal protein S2                                |   K02981           |   K02967
Ribosomal protein S3                                |   K02985           |   K02982
Ribosomal protein S4                                |   K02987           |   K02986
Ribosomal protein S5                                |   K02989           |   K02988
Ribosomal protein S7                                |   K02993           |   K02992
Ribosomal protein S8                                |   K02995           |   K02994
Ribosomal protein S9                                |   K02997           |   K02996
Seryl-tRNA synthetase                               |   K01875           |   K01875
Arginyl-tRNA synthetase                             |   K01887           |   K01887
DNA-directed RNA polymerase beta subunit            |   K03043           |   K03043
Ribosomal protein S13                               |   K02953           |   K02952




### 2.How the SSU rRAN database was created?

The SSU rRAN database was created by [SILVA](<https://www.arb-silva.de/>) SSU rRNA database project (version: SILVA SSU 123.1 release).
In this data the sequences haven been truncated, which means that all nucleotides that have not been aligned were removed from the sequence.

