# Physpe Tutorial 

## Auto bulid Tree of life



### Auto build Tree of life by highly conserved protein

None


### Auto build Tree of life by 16s SSU RNA

1.  prepare organism names list, 191 organisms names list [download][1]  

```bash
$ cat 191speciesnames.txt 
neq
pai
ape
sto
ssoa
tvo
tac
afu
.....
```

2.  Reconstruct phylogenetic tree by 16s SSU RNA  

```bash
$ physpe autobuild -i 191speciesnames.txt -o 191_rna --srna
Loading organisms names success.....

The result are store in:191_rna

Now loading data and constructing species phylogenetic tree......
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: neq
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: ape
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: tac
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: mmp
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: gla
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: tps
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: cho
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: ddi
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: spo
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: aga
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: tru
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: mpu
2016-09-05 19:48:03,824 Checking organisms INFO: The organism: lin
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: ban
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: bce
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: ljo
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: san
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: spg
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: ges
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: lis
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: sco
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: cdi
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: mle
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: wsu
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: rpr
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: bpe
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: bpa
2016-09-05 19:48:03,825 Checking organisms INFO: The organism: ppr
2016-09-05 19:48:03,825 Checking organisms WARNING: There organisms can't match in SILVA database so removed and reconstruct phylogenetic tree
2016-09-05 19:48:03,825 16s DB INFO: Read organisms names success
2016-09-05 19:48:14,354 16s DB INFO: Retrieve organism 'pai' 16s SSU RNA sequences data success
2016-09-05 19:48:17,703 16s DB INFO: Retrieve organism 'sto' 16s SSU RNA sequences data success
2016-09-05 19:48:20,674 16s DB INFO: Retrieve organism 'ssoa' 16s SSU RNA sequences data success
2016-09-05 19:48:23,031 16s DB INFO: Retrieve organism 'tvo' 16s SSU RNA sequences data success
2016-09-05 19:48:26,510 16s DB INFO: Retrieve organism 'afu' 16s SSU RNA sequences data success
2016-09-05 19:48:28,766 16s DB INFO: Retrieve organism 'hal' 16s SSU RNA sequences data success
2016-09-05 19:48:31,148 16s DB INFO: Retrieve organism 'mac' 16s SSU RNA sequences data success
2016-09-05 19:48:33,579 16s DB INFO: Retrieve organism 'mma' 16s SSU RNA sequences data success
2016-09-05 19:48:35,856 16s DB INFO: Retrieve organism 'pfu' 16s SSU RNA sequences data success
2016-09-05 19:48:38,194 16s DB INFO: Retrieve organism 'pho' 16s SSU RNA sequences data success
......
```

3.  Get the tree file  

![191_species_rna](img/191_species_rna.png)







[1]: example/191speciesnames.txt