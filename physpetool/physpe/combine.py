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
The arguments parse module for combine module.

"""

import os
from physpetool.phylotree.consensustree import docontree

APP_DESC = ""


def start_args(input):
    """
Arguments parse
    :param input:  Arguments
    """
    combine_args = input.add_argument_group("COMBINE OPTIONS")
    combine_args.add_argument('-i', action='store', dest="inputfile",
                              help='iInput a tree file (PHYLIP format), which contain multiple tree.')
    combine_args.add_argument('-o', action='store', dest="outputfile",
                              default='combinetree', help='A directory contain combined tree file. \
                              The default is combineTree.')
    combine_args.add_argument('--mr', action='store_true', dest="mr",
                              default=True, help='Compute majority rule consensus tree. default.')
    combine_args.add_argument('--mre', action='store_true', dest="mre",
                              default=False, help='Compute extended majority rule consensus tree.')
    combine_args.add_argument('--strict', action='store_true', dest="strict",
                              default=False, help='Compute strict consensus tree.')

def starting(args):
    """
Staring run combine
    :param args: arguments
    """
    pwd = os.getcwd()

    out_put = os.path.join(pwd, args.outputfile)

    # get the consensus tree method
    if args.mre:
        rule = "MRE"
    elif args.strict:
        rule = "STRICT"
    elif args.mr:
        rule = "MR"

    # merge tree
    docontree(args.inputfile, out_put, rule)
