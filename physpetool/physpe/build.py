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
The arguments parse module for build module.

"""

import os
from physpetool.phylotree.buildtree import build_hcp, build_srna
from physpetool.phylotree.log import setlogdir

APP_DESC = ""

raxmlpara_pro = "-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1"
raxmlpara_dna = "-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1"
musclepara = "-maxiters 100"
gblockspara_pro = "-t=p -e=-gb1"
gblockspara_dna = "-t=d -e=-gb1"
clustalwpara = None


def start_args(input):
    """
Arguments parse
    :param input:  Arguments
    """
    build_args = input.add_argument_group("BUILD OPTIONS")
    advance_args = input.add_argument_group("ADVANCE OPTIONS")
    build_args.add_argument('-i', action='store', dest='input',
                            help="Input file FASTA format for '--sran' method or a directory contain conserved\
                                proteins for '--hcp' method.")
    build_args.add_argument('-o', action='store', dest="outdata",
                            default='Outdata',
                            help="A directory include output data (tree files). The default name is \
                                Outdata.")
    build_args.add_argument('-t', action='store', dest='thread',
                            type=int, default=1,
                            help="Specify the number of processing threads (CPUs) to reconstruct \
                                phylogenetic tree. The default is 1.")
    build_args.add_argument('--hcp', action='store_true', dest='HCP',
                            default=False,
                            help="Specify the hcp (highly conserved protein) method to reconstruct \
                                phylogenetic tree. The default method is hcp.")
    build_args.add_argument('--srna', action='store_true', dest='ssurna',
                            default=False,
                            help="The srna (SSU rRNA) method is use SSU rRNA data to reconstruct \
                               phylogenetic tree.")
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
    advance_args.add_argument('--gblocks', action='store', dest='gblocks_parameter',
                              default=gblockspara_pro, help="Set Gblocks advance parameters.")
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
Staring run build
    :param args: arguments
    """

    pwd = os.getcwd()

    out_put = os.path.join(pwd, args.outdata)
    if args.input:
        if os.path.isfile(args.input):
            args_input = args.input
        elif os.path.isdir(args.input):
            args_input = os.path.join(pwd, args.input)

    if args.HCP:
        setlogdir(out_put)
        build_hcp(args_input, out_put, args.muscle, args.muscle_parameter, args.clustalw, args.clustalw_parameter,
                  args.gblocks_parameter, args.raxml, args.raxml_parameter, args.fasttree, args.fasttree_parameter,
                  args.thread)
    # reconstruct phylogenetic tree by ssu RNA
    elif args.ssurna:
        setlogdir(out_put)
        build_srna(args_input, out_put, args.muscle, args.muscle_parameter, args.clustalw, args.clustalw_parameter,
                   args.gblocks_parameter, args.raxml, args.raxml_parameter, args.fasttree, args.fasttree_parameter,
                   args.thread)
