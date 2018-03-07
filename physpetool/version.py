# coding=utf-8
# ########################## Copyrights and License #############################
#                                                                               #
# Copyright 2016 Yang Fang <yangfangscu@gmail.com>                              #
#                                                                               #
# This file is part of PhySpeTree.                                              #
# https://xiaofeiyangyang.github.io/physpetools/                                #
#                                                                               #
# PhySpeTree is free software: you can redistribute it and/or modify it under   #
# the terms of the GNU Lesser General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)     #
# any later version.                                                            #
#                                                                               #
# PhySpeTree is distributed in the hope that it will be useful, but WITHOUT ANY #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS     #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  #
# details.                                                                      #
#                                                                               #
# You should have received a copy of the GNU Lesser General Public License      #
# along with PhySpeTree. If not, see <http://www.gnu.org/licenses/>.            #
#                                                                               #
# ###############################################################################


"""
The physpe version and call software in physpe  version and citation.

"""
version = '0.3.1'

VERSION_DESC = (
    """
          -------------------------------------------------------------------------------------
                      PhySpeTree (%s) - Reconstruct Phylogenetic species Tree
          PhySpeTree document: https://yangfangs.github.io/physpetools/       
        
          Citation:
                  PhySpeTree: automatically reconstructing phylogenetic species tree (submitted)

          --------------------------------------------------------------------------------------
          """ % (version))


def version_infor():
    muscle_info = 'v3.8.31'
    clustalw2_info = '2.1'
    mafft_info = 'v7.310'
    trimal_info = '1.2rev59'
    gblocks_info = '0.91b'
    raxml_info = 'v8.2.3'
    fasttree_info = '2.1.9'
    author_info = 'Author: Yang Fang\n'
    print (VERSION_DESC)
    print (author_info)
    print ("PhySpeTree call follow software, if you use PhySpetree build tree please don't forget cite this:\n ")
    print ("============================CALL SOFTWARE INFO=============================================")
    print ('muscle version: '), (muscle_info + '\ncite:')
    print (citation['muscle'])
    print ('clustalw2 versin: '), (clustalw2_info + '\ncite:')
    print (citation['clustalw2'])
    print ('mafft versin: '), (mafft_info + '\ncite:')
    print (citation['mafft'])
    print ('RAxML version: '), (raxml_info + '\ncite:')
    print (citation['RAxML'])
    print ('FastTree version: '), (fasttree_info + '\ncite:')
    print (citation['FastTree'])
    print ('Gblocks version: '), (gblocks_info + '\ncite:')
    print (citation['Gblocks'])
    print ('trimal versin: '), (trimal_info + '\ncite:')
    print (citation['trimal'])
    print ("===========================CALL SOFTWARE INFO==============================================")


citation = {
    'muscle': u"""Edgar R C. MUSCLE: multiple sequence alignment with high accuracy and
    high throughput[J]. Nucleic acids research, 2004, 32(5): 1792-1797.
    """,

    'clustalw2': u"""Larkin M A, Blackshields G, Brown N P, et al. Clustal W and Clustal X
    version 2.0[J]. bioinformatics, 2007, 23(21): 2947-2948.
    """,

    'RAxML': u"""Stamatakis A. RAxML version 8: a tool for phylogenetic analysis and
    post-analysis of large phylogenies[J]. Bioinformatics, 2014, 30(9): 1312-1313.
    """,
    'FastTree': u"""Price M N, Dehal P S, Arkin A P. FastTree 2–approximately
    maximum-likelihood trees for large alignments[J]. PloS one, 2010, 5(3): e9490.""",

    'Gblocks': u"""Talavera G, Castresana J. Improvement of phylogenies after removing
    divergent and ambiguously aligned blocks from protein sequence alignments[J].
    Systematic biology, 2007, 56(4): 564-577.
    """,
    'trimal': u"""Capella-Gutiérrez S, Silla-Martínez J M, Gabaldón T. trimAl: a tool for
     automated alignment trimming in large-scale phylogenetic analyses[J]. Bioinformatics,
      2009, 25(15): 1972-1973.""",
    'mafft': u"""Katoh K, Standley D M. MAFFT multiple sequence alignment software version 7:
     improvements in performance and usability[J]. Molecular biology and evolution, 2013, 30(4):
      772-780."""
}

if __name__ == '__main__':
    version_infor()
