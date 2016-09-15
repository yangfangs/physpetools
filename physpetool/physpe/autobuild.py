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
The main module as enter point and invoke other
script as pipeline.
"""
from physpetool.phylotree.doclustalw import doclustalw_file, doclustalw
from physpetool.phylotree.domuscle import domuscle_file, domuscle
from physpetool.phylotree.dogblocks import dogblocks
from physpetool.phylotree.doraxml import doraxml
from physpetool.convert.fasta2phy import fasta2phy
from physpetool.convert.concatenate import cocat_path
from physpetool.phylotree.log import getLogging, setlogdir
from physpetool.phylotree.retrieve16srna import retrieve16srna
from physpetool.phylotree.retrieveprotein import doretrieve
from physpetool.utils.checkinputfile import checkKeggOrganism, checkSilvaOrganism, checkFile
import argparse
import os

APP_DESC = "reconstruct"

raxmlpara_pro = "-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1"
raxmlpara_dna = "-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1"
musclepara = '-maxiters 100'
gblockspara_pro = '-t=p -e=-gb1'
gblockspara_dna = '-t=d -e=-gb1'
clustalwpara = None


def start_args(input):
    """
Argument parse
    :param input: arguments
    """
    autobuild_args = input.add_argument_group("AUTOBUILD OPTIONS")
    advance_args = input.add_argument_group("ADVANCE OPTIONS")
    autobuild_args.add_argument('-i', nargs='?', dest='spenames', type=argparse.FileType('r'),
                                help='	Input a txt file contain the a abbreviation species names are same with KEGG species abbreviation.')
    autobuild_args.add_argument('-o', action='store', dest="outdata",
                                default='Outdata',
                                help="A directory include output data (reconstruct tree files). The default output data name is Outdata.")
    autobuild_args.add_argument('-t', action='store', dest='thread',
                                type=int, default=1,
                                help="Specify the number of processing threads (CPUs) to use for Physpe to reconstruct phylogenetic tree. The default is 1.")
    autobuild_args.add_argument('-e', action='store', dest="extenddata",
                                help="The extended data should be FASTA format to extend phylogenetic tree by --ehcp or --esrna option.")
    autobuild_args.add_argument('--hcp', action='store_true', dest='HCP',
                                default=False,
                                help="The hcp (highly conserved protein) mode is use highly conserved proteins to reconstruct phylogenetic tree. The default mode is hcp.")
    autobuild_args.add_argument('--ehcp', action='store_true', dest='EHCP',
                                default=False,
                                help="The ehcp (extend highly conserved protein) mode is use highly conserved proteins and extend highly protein (user provide) to reconstruct phylogenetic tree.")
    autobuild_args.add_argument('--srna', action='store_true', dest='ssurna',
                                default=False,
                                help="The srna (16s SSU RNA) mode is use 16s SSU RNA data to reconstruct phylogenetic tree.")
    autobuild_args.add_argument('--esrna', action='store_true', dest='essurna',
                                default=False,
                                help="The esrna (extend 16s SSU RNA) mode is use 16s SSU RNA data and extend 16s SSU RNA (user provide) to reconstruct phylogenetic tree.")
    advance_args.add_argument('--muscle', action='store_true', dest='muscle',
                              default=True,
                              help='Multiple sequence alignment by muscle. The default aligned software is Muscle.')
    advance_args.add_argument('--muscle_p', action='store', dest='muscle_parameter',
                              default=musclepara, help='Set more detail muscle parameter.')
    advance_args.add_argument('--clustalw', action='store_true', dest='clustalw',
                              default=False, help='multiple sequense alignment by clustalw2.')
    advance_args.add_argument('--clustalw_p', action='store', dest='clustalw_parameter',
                              help='Set more detail clustalw2 parameter.')
    advance_args.add_argument('--gblocks', action='store', dest='gblocks',
                              default=gblockspara_pro, help='Use gblock.')
    advance_args.add_argument('--raxml', action='store', dest='raxml',
                              default=raxmlpara_pro, help='Build by raxml.')


def starting(args):
    """
starting run reconstruct tree
    :param args: arguments
    """
    print ("Loading organisms names success.....\n")
    print ("The result are store in:{0}\n".format(args.outdata))
    print ("Now loading data and constructing species phylogenetic tree......")

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
    # Reconstruct phylogenetic tree by highly conserved proteins.
    if args.HCP:
        setlogdir(out_put)
        starting_hcp(in_put, out_put, args.muscle, args.muscle_parameter, args.clustalw, args.clustalw_parameter,
                     args.gblocks, args.raxml, args.thread)
    # Reconstruct phylogenetic tree by ssu RNA.
    elif args.ssurna:
        setlogdir(out_put)
        starting_srna(in_put, out_put, args.muscle, args.muscle_parameter, args.clustalw, args.clustalw_parameter,
                      args.gblocks, args.raxml, args.thread)

    # Reconstruct phylogenetic tree by extend highly conserved proteins.
    elif args.EHCP:
        setlogdir(out_put)
        starting_ehcp(in_put, out_put, args.muscle, args.muscle_parameter, args.clustalw, args.clustalw_parameter,
                      args.gblocks, args.raxml, args.thread, args_extend)

    # Reconstruct phylogenetic tree by extend ssu rna method.
    elif args.essurna:
        setlogdir(out_put)
        starting_esrna(in_put, out_put, args.muscle, args.muscle_parameter, args.clustalw, args.clustalw_parameter,
                       args.gblocks, args.raxml, args.thread, args_extend)


def starting_hcp(in_put, out_put, args_muscle, args_muscle_p, args_clustalw, args_clustalw_p,
                 args_gblocks, args_raxml, args_thread):
    '''reconstruct phylogenetic tree by hcp method'''
    hcp_input = checkKeggOrganism(in_put)
    out_retrieve = doretrieve(hcp_input, out_put)

    # set default aligned by muscle if not specify clustalw
    if args_clustalw:
        out_alg = doclustalw_file(out_retrieve, out_put, args_clustalw_p)
    elif args_muscle:
        out_alg = domuscle_file(out_retrieve, out_put, args_muscle_p)

    out_concat = cocat_path(out_alg)
    out_gblock = dogblocks(out_concat, args_gblocks)
    out_f2p = fasta2phy(out_gblock)
    doraxml(out_f2p, out_put, args_raxml, args_thread)


def starting_srna(in_put, out_put, args_muscle, args_muscle_p, args_clustalw, args_clustalw_p,
                  args_gblocks, args_raxml, args_thread):
    '''reconstruct phylogenetic tree by ssu rna method'''
    ssu_input = checkSilvaOrganism(in_put)
    out_retrieve = retrieve16srna(ssu_input, out_put)
    # set default aligned by muscle if not specify clustalw
    if args_clustalw:
        out_alg = doclustalw(out_retrieve, out_put, args_clustalw_p)
    elif args_muscle:
        out_alg = domuscle(out_retrieve, out_put, args_muscle_p)
    if args_gblocks is gblockspara_pro:
        args_gblocks = gblockspara_dna
        out_gblock = dogblocks(out_alg, args_gblocks)
    out_f2p = fasta2phy(out_gblock)
    if args_raxml is raxmlpara_pro:
        args_raxml = raxmlpara_dna
        doraxml(out_f2p, out_put, args_raxml, args_thread)


def starting_ehcp(in_put, out_put, args_muscle, args_muscle_p, args_clustalw, args_clustalw_p,
                  args_gblocks, args_raxml, args_thread, args_exteddata):
    '''reconstruct phylogenetic tree by ehcp method'''
    hcp_input = checkKeggOrganism(in_put)
    out_retrieve = doretrieve(hcp_input, out_put)
    retrieve_pro = os.listdir(out_retrieve)
    for reline in retrieve_pro:
        fw_name = os.path.join(out_retrieve, reline)
        fr_name = os.path.join(args_exteddata, reline)
        fw = open(fw_name, 'ab')
        with open(fr_name) as fr:
            for line in fr:
                fw.write(line)
        fw.close()

    # set default aligned by muscle if not specify clustalw
    if args_clustalw:
        out_alg = doclustalw_file(out_retrieve, out_put, args_clustalw_p)
    elif args_muscle:
        out_alg = domuscle_file(out_retrieve, out_put, args_muscle_p)

    out_concat = cocat_path(out_alg)
    out_gblock = dogblocks(out_concat, args_gblocks)
    out_f2p = fasta2phy(out_gblock)
    doraxml(out_f2p, out_put, args_raxml, args_thread)


def starting_esrna(in_put, out_put, args_muscle, args_muscle_p, args_clustalw, args_clustalw_p,
                   args_gblocks, args_raxml, args_thread, args_extenddata):
    '''reconstruct phylogenetic tree by ssu rna extend method'''
    extend_check = checkFile(args_extenddata)
    ssu_input = checkSilvaOrganism(in_put)
    out_retrieve = retrieve16srna(ssu_input, out_put)
    retrieve_srna_path = os.path.join(out_retrieve, '16srandata.fasta')

    fw = open(retrieve_srna_path, 'ab')
    with open(extend_check) as read:
        for line in read:
            fw.write(line)
    fw.close()

    # set default aligned by muscle if not specify clustalw
    if args_clustalw:
        out_alg = doclustalw(out_retrieve, out_put, args_clustalw_p)
    elif args_muscle:
        out_alg = domuscle(out_retrieve, out_put, args_muscle_p)

    if args_gblocks is gblockspara_pro:
        args_gblocks = gblockspara_dna
    out_gblock = dogblocks(out_alg, args_gblocks)
    out_f2p = fasta2phy(out_gblock)
    if args_raxml is raxmlpara_pro:
        args_raxml = raxmlpara_dna
    doraxml(out_f2p, out_put, args_raxml, args_thread)
