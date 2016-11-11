### 1. What is the input of PhySpeTree?

Users only need to prepare a TXT file containing [KEGG](http://www.genome.jp/kegg/catalog/org_list.html) abbreviated species names. For example, [organism_example_list](https://gitlab.com/xiaoxiaoyang/physpetools/raw/master/examples/organism_example_list.txt).

### 2. How to explain PhySpeTree outputs?

PhySpeTree returns two folders, `Outdata` contains the output species tree and `temp` includes temporary data. Files in `temp` can be used to check the quality of outputs in each step. If HCP method (`--hcp`) is selected, the `temp` folder includes:

  * `conserved_protein`: highly conserved proteins retrieved from the KEGG database.
  * `alignment`: aligned sequences.
  * `concatenate`: concatenated sequences and conserved blocks.

If SSU rRNA method (`--srna`) is selected, the `temp` folder includes:

  * `rna_sequence`: SSU rRNA sequences retrieved from the SILVA database.
  * `rna_alignment`: aligned sequences and conserved blocks.

### 3. What classes of HCP are selected?

PhySpeTree uses 31 HCP without horizontal transferred genes according to Ciccarelli *et al.*.

**cite:**

> Ciccarelli FD, Doerks T, Von Mering C, et al. Toward automatic reconstruction of a highly resolved tree of life[J]. science, 2006, 311(5765): 1283-1287.

The 31 HCP and corresponding KEGG KO number are shown in the following table:

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


### 4. How are SSU rRAN created?

The SSU rRAN sequences are created from the [SILVA](<https://www.arb-silva.de/>) database (123.1 release). Sequences haven been truncated, which means unaligned nucleotides are removed.

