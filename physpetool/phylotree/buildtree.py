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
Build tree module: use build tree user should provide the organism highly conserved proteins
or 16s SSU rRNA.
"""

from physpetool.convert.concatenate import cocat_path
from physpetool.convert.fasta2phy import fasta2phy
from physpetool.phylotree.doclustalw import doclustalw_file, doclustalw
from physpetool.phylotree.dofasttree import doFastTree
from physpetool.phylotree.dogblocks import dogblocks
from physpetool.phylotree.domuscle import domuscle_file, domuscle
from physpetool.phylotree.doraxml import doraxml

# default arguments
raxmlpara_pro = "-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1"
raxmlpara_dna = "-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1"
musclepara = "-maxiters 100"
gblockspara_pro = "-t=p -e=-gb1"
gblockspara_dna = "-t=d -e=-gb1"
clustalwpara = None


def build_hcp(in_put, out_put, args_muscle, args_muscle_p, args_clustalw, args_clustalw_p,
              args_gblocks, args_raxml, args_raxml_p, args_fasttree, args_fasttree_p, args_thread):
    '''reconstruct phylogenetic tree by hcp method'''
    out_retrieve = in_put
    # set default aligned by muscle if not specify clustalw
    if args_clustalw:
        out_alg = doclustalw_file(out_retrieve, out_put, args_clustalw_p)
    elif args_muscle:
        out_alg = domuscle_file(out_retrieve, out_put, args_muscle_p)
    out_concat = cocat_path(out_alg)
    out_gblock = dogblocks(out_concat, args_gblocks)
    out_f2p = fasta2phy(out_gblock)
    # reconstruct tree
    if args_fasttree:
        doFastTree(out_f2p, out_put, args_fasttree_p, args_thread)
    elif args_raxml:
        doraxml(out_f2p, out_put, args_raxml_p, args_thread)


def build_srna(in_put, out_put, args_muscle, args_muscle_p, args_clustalw, args_clustalw_p,
               args_gblocks, args_raxml, args_raxml_p, args_fasttree, args_fasttree_p, args_thread):
    '''reconstruct phylogenetic tree by ssu rna method'''
    out_retrieve = in_put
    # set default aligned by muscle if not specify clustalw
    if args_clustalw:
        out_alg = doclustalw(out_retrieve, out_put, args_clustalw_p)
    elif args_muscle:
        out_alg = domuscle(out_retrieve, out_put, args_muscle_p)

    if args_gblocks == gblockspara_pro:
        args_gblocks = gblockspara_dna
    out_gblock = dogblocks(out_alg, args_gblocks)
    out_f2p = fasta2phy(out_gblock)
    # reconstruct tree
    if args_fasttree:
        args_fasttree_p_add = "-nt " + args_fasttree_p.lstrip()
        doFastTree(out_f2p, out_put, args_fasttree_p_add, args_thread)
    elif args_raxml:
        if args_raxml_p == raxmlpara_pro:
            args_raxml_p = raxmlpara_dna
            doraxml(out_f2p, out_put, args_raxml_p, args_thread)
