
**One command line auto reconstruct phylogenetic tree**


# Introduction

In some filed combine species phylogenetic tree do some prediction are very important for instance,
protein-protein interactions and gene pathway members prediction. In this predicted construct a exact species phylogenetic tree
is necessary, but the process of constructing the tree species is very tedious.

We developing a command line software **Physpe**, which only one command line to construct species phylogenetic tree. User need to provide a txt files, witch contain species names only.
(the species names must be a abbreviation same with **KEGG database** organisms abbreviation), the **Physpe** auto reconstruct species phylogenetic tree.


# Physpe workflow


![workflow](img/physpe2.png)


Physpe workflow includes the following steps:

1. Prepare organisms names to reconstruct phylogenetic tree as [example](https://raw.githubusercontent.com/xiaofeiyangyang/physpetools/master/examples/organism_example_list.txt)

2. Choice the way to reconstruct phylogenetic tree, use 16s RNA or Highly conversion proteins.

3. Query database and parse retrieve fasta format files.

4. Do multiple sequence alignment by call Muscle.

5. Concatenate conserved proteins by Physpe.

6. Select conserved blocks by Call Gblosks.

7. Reconstructing phylogenetic tree by Call RAxML.

8. Output reconstruct phylogenetic tree files.



# Features

- Easy to use (one command line auto construct phylogenetic tree).

- Multi-selection (selection construct phylogenetic tree by highly conversion protein or 16s RNA).

- Adjustable parameters (user can choice any enable parameters by own).

- User need provide a species list (reconstruct phylogenetic tree organisms) only.

- combine best phylogenetic tree (combine multiple tree to a consensus tree)

- view tree by iTol (easy use iview module to view tree)


# physpetools module:

* [autobuild](usage.md#autobuild): Auto reconstruct phylogenetic tree

```bash
physpe autobuild -i species_name_list.txt -o Output
```


* [build](usage.md#build): Reconstruct phylogenetic tree

```bash
physpe build -i species.fasta -o Output
```

* [combine](usage.md#combine): Combine multiple best phylogenetic tree 

```bash
physpe combine -i multiple_tree.tree -o Output
```


* [iview](usage.md#iview): view phylogenetic tree by iTol

```bash
physpe iview -i species_name_list.txt -o ivew -range phylum 
```
