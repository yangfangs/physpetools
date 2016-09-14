# ########################## Copyrights and License ############################
#                                                                              #
# Copyright 2016 Yang Fang <yangfangscu@gmail.com>                             #
#                                                                              #
# This file is part of Physpe.                                                 #
# https://xiaofeiyangyang.github.io/physpetools/                               #
#                                                                              #
# Physpe is free software: you can redistribute it and/or modify it under      #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# Physpe is distributed in the hope that it will be useful, but WITHOUT ANY    #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with Physpe. If not, see <http://www.gnu.org/licenses/>.               #
#                                                                              #
# ##############################################################################


"""
The physpe version and call software in physpe  version and citation.

"""
version = '0.2.1'


VERSION_DESC = (
    """
          --------------------------------------------------------------------------------
                      Physpe (%s) - Reconstruct Phylogenetic Tree

          Citation: null

          --------------------------------------------------------------------------------
          """ % (version))


def version_infor():
    muscle_info = 'v3.8.31'
    gblocks_info = '0.91b'
    raxml_info = 'v8.2.3'
    author_info = 'Author: Yang Fang\n'
    print (VERSION_DESC)
    print (author_info)
    print ("Physpe call follow software if you use physpe please don't forget cite this:\n ")
    print ("============================CALL SOFTWARE INFO=============================================")
    print ('muscle version: '), (muscle_info + '\ncite:')
    print (citation['muscle'])
    print ('RAxML version: '), (raxml_info + '\ncite:')
    print (citation['RAxML'])
    print ('Gblocks version: '), (gblocks_info + '\ncite:')
    print (citation['Gblocks'])
    print ("===========================CALL SOFTWARE INFO==============================================")

citation = {
    'muscle': u"""Edgar R C. MUSCLE: multiple sequence alignment with high accuracy and
    high throughput[J]. Nucleic acids research, 2004, 32(5): 1792-1797.
    """,

    'RAxML': u"""Stamatakis A. RAxML version 8: a tool for phylogenetic analysis and
    post-analysis of large phylogenies[J]. Bioinformatics, 2014, 30(9): 1312-1313.
    """,

    'Gblocks': u"""Talavera G, Castresana J. Improvement of phylogenies after removing
    divergent and ambiguously aligned blocks from protein sequence alignments[J].
    Systematic biology, 2007, 56(4): 564-577.
    """
}

if __name__ == '__main__':
    version_infor()
