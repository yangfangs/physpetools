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
The main module as enter point and invoke other
script as pipeline.
"""
from physpetool.phylotree.doclustalw import doclustalw_file, doclustalw
from physpetool.phylotree.dofasttree import doFastTree
from physpetool.phylotree.domafft import domafft, domafft_file
from physpetool.phylotree.domuscle import domuscle_file, domuscle
from physpetool.phylotree.dogblocks import dogblocks
from physpetool.phylotree.doraxml import doraxml
from physpetool.convert.fasta2phy import fasta2phy
from physpetool.convert.concatenate import cocat_path
from physpetool.phylotree.dotrimal import dotrimal
from physpetool.phylotree.log import getLogging, setlogdir
from physpetool.phylotree.retrievessurna import retrieve16srna
from physpetool.phylotree.retrieveprotein import doretrieve
from physpetool.utils.checkinputfile import checkKeggOrganism, checkSilvaOrganism, checkFile
import argparse
import os

APP_DESC = "Reconstruct"

raxmlpara_pro = "-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1"
raxmlpara_dna = "-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1"
musclepara = '-maxiters 100'
gblockspara_pro = '-t=p -e=-gb1'
gblockspara_dna = '-t=d -e=-gb1'
clustalwpara = None
trimalpara = "-gt 1"
mafftpara = "--auto"


def start_args(input):
    """
Argument parse
    :param input: arguments
    """
    autobuild_args = input.add_argument_group("AUTOBUILD OPTIONS")
    advance_args = input.add_argument_group("ADVANCE OPTIONS")
    autobuild_args.add_argument('-i', nargs='?', dest='spenames', type=argparse.FileType('r'),
                                help='Input a TXT file contain the species names (abbreviated names) are same with KEGG \
                                species abbreviation.')
    autobuild_args.add_argument('-o', action='store', dest="outdata",
                                default='Outdata',
                                help="A directory include output data (tree files). The default name is \
                                Outdata.")
    autobuild_args.add_argument('-t', action='store', dest='thread',
                                type=int, default=1,
                                help="Specify the number of processing threads (CPUs) to reconstruct \
                                phylogenetic tree. The default is 1.")
    autobuild_args.add_argument('-e', action='store', dest="extenddata",
                                help="The extended data should be FASTA format to extend phylogenetic tree by \
                                     --ehcp or --esrna option.")
    autobuild_args.add_argument('--hcp', action='store_true', dest='HCP',
                                default=True,
                                help="Specify the hcp (highly conserved protein) method to reconstruct \
                                phylogenetic tree. The default method is hcp.")
    autobuild_args.add_argument('--ehcp', action='store_true', dest='EHCP',
                                default=False,
                                help="The ehcp mode is use highly conserved proteins with extend highly  \
                                     conserved protein (users provide) to reconstruct phylogenetic tree.")
    autobuild_args.add_argument('--srna', action='store_true', dest='ssurna',
                                default=False,
                                help="The srna (SSU rRNA) method is use SSU rRNA data to reconstruct \
                               phylogenetic tree.")
    autobuild_args.add_argument('--esrna', action='store_true', dest='essurna',
                                default=False,
                                help="The esrna mode is use SSU RNA sequence with extend SSU RNA sequence \
                                (users provide) to reconstruct phylogenetic tree. ")
    advance_args.add_argument('--muscle', action='store_true', dest='muscle',
                              default=True,
                              help="Multiple sequence alignment by muscle. The default multiple sequence \
                                   alignment software is Muscle.")
    advance_args.add_argument('--muscle_p', action='store', dest='muscle_parameter',
                              default=musclepara, help="Set Muscle advance parameters. The default is -maxiter 100.")
    advance_args.add_argument('--clustalw', action='store_true', dest='clustalw',
                              default=False, help="Multiple sequence alignment by clustalw2.")
    advance_args.add_argument('--clustalw_p', action='store', dest='clustalw_parameter',
                              help='Set clustalw2 advance parameters. Here use clustalw default parameters.')
    advance_args.add_argument('--mafft', action='store_true', dest='mafft',
                              default=False, help="Multiple sequence alignment by mafft.")
    advance_args.add_argument('--mafft_p', action='store', dest='mafft_parameter',
                              default=mafftpara,
                              help='Set mafft advance parameters. Here use mafft default parameters.')
    advance_args.add_argument('--gblocks', action='store_true', dest='gblocks',
                              default=True, help="Trim by Gblocks.")
    advance_args.add_argument('--gblocks_p', action='store', dest='gblocks_parameter',
                              default=gblockspara_pro, help="Set Gblocks advance parameters.")
    advance_args.add_argument('--trimal', action='store_true', dest='trimal',
                              default=False, help="Trim by trimal.")
    advance_args.add_argument('--trimal_p', action='store', dest='trimal_parameter',
                              default=trimalpara, help="Set trimal advance parameters.")
    advance_args.add_argument('--raxml', action='store_true', dest='raxml', default=True,
                              help="Reconstruct phylogenetic tree by RAxML. The default build tree software is RAxML.")
    advance_args.add_argument('--raxml_p', action='store', dest='raxml_parameter',
                              default=raxmlpara_pro, help='Set RAxML advance parameters. ')
    advance_args.add_argument('--fasttree', action='store_true', dest='fasttree',
                              default=False, help='Reconstruct phylogenetic tree by FastTree.')
    advance_args.add_argument('--fasttree_p', action='store', dest='fasttree_parameter',
                              default='', help='Set FastTree advance parameters. ')


def starting(args):
    """
starting run reconstruct tree
    :param args: arguments
    """
    print ("Loading organisms names success.....\n")
    print ("The result are store in:{0}\n".format(args.outdata))
    print ("Now loading data and constructing phylogenetic tree......")

    in_put = args.spenames

    pwd = os.getcwd()

    out_put = os.path.join(pwd, args.outdata)
    if args.extenddata:
        if os.path.isfile(args.extenddata):
            args_extend = args.extenddata
        elif os.path.isdir(args.extenddata):
            args_extend = os.path.join(pwd, args.extenddata)
    else:
        pass


    # Reconstruct phylogenetic tree by ssu RNA.
    if args.ssurna:
        setlogdir(out_put)
        starting_srna(in_put, out_put,
                      args.muscle, args.muscle_parameter,
                      args.clustalw, args.clustalw_parameter,
                      args.mafft, args.mafft_parameter,
                      args.gblocks, args.gblocks_parameter,
                      args.trimal, args.trimal_parameter,
                      args.raxml, args.raxml_parameter,
                      args.fasttree, args.fasttree_parameter,
                      args.thread)

    # Reconstruct phylogenetic tree by extend highly conserved proteins.
    elif args.EHCP:
        setlogdir(out_put)
        starting_ehcp(in_put, out_put,
                      args.muscle, args.muscle_parameter,
                      args.clustalw, args.clustalw_parameter,
                      args.mafft, args.mafft_parameter,
                      args.gblocks, args.gblocks_parameter,
                      args.trimal, args.trimal_parameter,
                      args.raxml, args.raxml_parameter,
                      args.fasttree, args.fasttree_parameter,
                      args.thread, args.extenddata)

    # Reconstruct phylogenetic tree by extend ssu rna method.
    elif args.essurna:
        setlogdir(out_put)
        starting_esrna(in_put, out_put,
                       args.muscle, args.muscle_parameter,
                       args.clustalw, args.clustalw_parameter,
                       args.mafft, args.mafft_parameter,
                       args.gblocks, args.gblocks_parameter,
                       args.trimal, args.trimal_parameter,
                       args.raxml, args.raxml_parameter,
                       args.fasttree, args.fasttree_parameter,
                       args.thread, args.extenddata)
    # Reconstruct phylogenetic tree by highly conserved proteins.
    elif args.HCP:
        setlogdir(out_put)
        starting_hcp(in_put, out_put,
                 args.muscle, args.muscle_parameter,
                 args.clustalw, args.clustalw_parameter,
                 args.mafft, args.mafft_parameter,
                 args.gblocks, args.gblocks_parameter,
                 args.trimal, args.trimal_parameter,
                 args.raxml, args.raxml_parameter,
                 args.fasttree, args.fasttree_parameter,
                 args.thread)

def starting_hcp(in_put, out_put,
                 args_muscle, args_muscle_p,
                 args_clustalw, args_clustalw_p,
                 args_mafft, args_mafft_p,
                 args_gblocks, args_gblocks_p,
                 args_trimal, args_trimal_p,
                 args_raxml, args_raxml_p,
                 args_fasttree, args_fasttree_p,
                 args_thread):
    '''reconstruct phylogenetic tree by hcp method'''
    hcp_input = checkKeggOrganism(in_put)
    out_retrieve = doretrieve(hcp_input, out_put)

    # set default aligned by muscle if not specify clustalw
    if args_clustalw:
        out_alg = doclustalw_file(out_retrieve, out_put, args_clustalw_p)
    elif args_mafft:
        out_alg = domafft_file(out_retrieve, out_put, args_mafft_p)
    elif args_muscle:
        out_alg = domuscle_file(out_retrieve, out_put, args_muscle_p)

    out_concat = cocat_path(out_alg)

    # set default trim by gblocks if not specify trimal
    if args_trimal:
        out_f2p = dotrimal(out_concat, args_trimal_p)
    elif args_gblocks:
        out_gblock = dogblocks(out_concat, args_gblocks_p)
        out_f2p = fasta2phy(out_gblock)

    # reconstruct tree
    if args_fasttree:
        doFastTree(out_f2p, out_put, args_fasttree_p, args_thread)
    elif args_raxml:
        doraxml(out_f2p, out_put, args_raxml_p, args_thread)


def starting_srna(in_put, out_put,
                  args_muscle, args_muscle_p,
                  args_clustalw, args_clustalw_p,
                  args_mafft, args_mafft_p,
                  args_gblocks, args_gblocks_p,
                  args_trimal, args_trimal_p,
                  args_raxml, args_raxml_p,
                  args_fasttree, args_fasttree_p,
                  args_thread):
    '''reconstruct phylogenetic tree by ssu rna method'''
    ssu_input = checkSilvaOrganism(in_put)
    out_retrieve = retrieve16srna(ssu_input, out_put)
    # set default aligned by muscle if not specify clustalw or mafft
    if args_clustalw:
        out_alg = doclustalw(out_retrieve, out_put, args_clustalw_p)
    elif args_mafft:
        out_alg = domafft(out_retrieve, out_put, args_mafft_p)
    elif args_muscle:
        out_alg = domuscle(out_retrieve, out_put, args_muscle_p)

    # set default trim by gblocks if not specify trimal
    if args_trimal:
        out_f2p = dotrimal(out_alg, args_trimal_p)
    elif args_gblocks:
        if args_gblocks_p is gblockspara_pro:
            args_gblocks_p = gblockspara_dna
            out_gblock = dogblocks(out_alg, args_gblocks_p)
        out_f2p = fasta2phy(out_gblock)

    # reconstruct tree
    if args_fasttree:
        args_fasttree_p_add = "-nt " + args_fasttree_p.lstrip()
        doFastTree(out_f2p, out_put, args_fasttree_p_add, args_thread)
    elif args_raxml:
        if args_raxml_p is raxmlpara_pro:
            args_raxml_p = raxmlpara_dna
            doraxml(out_f2p, out_put, args_raxml_p, args_thread)


def starting_ehcp(in_put, out_put,
                  args_muscle, args_muscle_p,
                  args_clustalw, args_clustalw_p,
                  args_mafft, args_mafft_p,
                  args_gblocks, args_gblocks_p,
                  args_trimal, args_trimal_p,
                  args_raxml, args_raxml_p,
                  args_fasttree, args_fasttree_p,
                  args_thread, args_extenddata):
    '''reconstruct phylogenetic tree by ehcp method'''
    hcp_input = checkKeggOrganism(in_put)
    out_retrieve = doretrieve(hcp_input, out_put)
    retrieve_pro = os.listdir(out_retrieve)
    for reline in retrieve_pro:
        fw_name = os.path.join(out_retrieve, reline)
        fr_name = os.path.join(args_extenddata, reline)
        fw = open(fw_name, 'ab')
        with open(fr_name) as fr:
            for line in fr:
                fw.write(line)
        fw.close()

    # set default aligned by muscle if not specify clustalw or mafft
    if args_clustalw:
        out_alg = doclustalw_file(out_retrieve, out_put, args_clustalw_p)
    elif args_mafft:
        out_alg = domafft_file(out_retrieve, out_put, args_mafft_p)
    elif args_muscle:
        out_alg = domuscle_file(out_retrieve, out_put, args_muscle_p)

    out_concat = cocat_path(out_alg)

    # set default trim by gblocks if not specify trimal
    if args_trimal:
        out_f2p = dotrimal(out_concat, args_trimal_p)
    elif args_gblocks:
        out_gblock = dogblocks(out_concat, args_gblocks_p)
        out_f2p = fasta2phy(out_gblock)
    # reconstruct tree
    if args_fasttree:
        doFastTree(out_f2p, out_put, args_fasttree_p, args_thread)
    elif args_raxml:
        doraxml(out_f2p, out_put, args_raxml_p, args_thread)


def starting_esrna(in_put, out_put,
                   args_muscle, args_muscle_p,
                   args_clustalw, args_clustalw_p,
                   args_mafft, args_mafft_p,
                   args_gblocks, args_gblocks_p,
                   args_trimal, args_trimal_p,
                   args_raxml, args_raxml_p,
                   args_fasttree, args_fasttree_p,
                   args_thread, args_extenddata):
    '''reconstruct phylogenetic tree by ssu rna extend method'''
    extend_check = checkFile(args_extenddata)
    ssu_input = checkSilvaOrganism(in_put)
    out_retrieve = retrieve16srna(ssu_input, out_put)
    retrieve_srna_path = os.path.join(out_retrieve, 'rna_sequence.fasta')

    fw = open(retrieve_srna_path, 'ab')
    with open(extend_check) as read:
        for line in read:
            fw.write(line)
    fw.close()

    # set default aligned by muscle if not specify clustalw
    if args_clustalw:
        out_alg = doclustalw(out_retrieve, out_put, args_clustalw_p)
    elif args_mafft:
        out_alg = domafft(out_retrieve, out_put, args_mafft_p)
    elif args_muscle:
        out_alg = domuscle(out_retrieve, out_put, args_muscle_p)

    # set default trim by gblocks if not specify trimal
    if args_trimal:
        out_f2p = dotrimal(out_alg, args_trimal_p)
    elif args_gblocks:
        if args_gblocks_p is gblockspara_pro:
            args_gblocks_p = gblockspara_dna
            out_gblock = dogblocks(out_alg, args_gblocks_p)
        out_f2p = fasta2phy(out_gblock)
    # reconstruct tree
    if args_fasttree:
        args_fasttree_p_add = "-nt " + args_fasttree_p.lstrip()
        doFastTree(out_f2p, out_put, args_fasttree_p_add, args_thread)
    elif args_raxml:
        if args_raxml_p is raxmlpara_pro:
            args_raxml_p = raxmlpara_dna
            doraxml(out_f2p, out_put, args_raxml_p, args_thread)
