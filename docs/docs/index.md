
**One command line auto reconstruct phylogenetic tree**


# Introduction

In some filed combine species phylogenetic tree do some prediction are very important for instance,
protein-protein interactions and gene pathway members prediction. In this predicted construct a exact species phylogenetic tree
is necessary, but the process of constructing the tree species is very tedious.

We developing a command line software **Physpe**, which only one command line to construct species phylogenetic tree. User need to provide a txt files, witch contain species names only.
(the species names must be a abbreviation same with **KEGG database** organisms abbreviation), the **Physpe** auto reconstruct species phylogenetic tree.




# physpetools module:

* [autobuild](): Auto reconstruct phylogenetic tree

```bash
physpe autobuild -i species_name_list.txt -o Output
```


* [build](): Reconstruct phylogenetic tree

```bash
physpe build -i species.fasta -o Output
```

* [combine](): Combine multiple best phylogenetic tree 

```bash
physpe combine -i multiple_tree.tree -o Output
```


* [iview](): view phylogenetic tree by iTol

```bash
physpe iview -i species_name_list.txt -o ivew -range phylum 
```
