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
                              help='input files name')
    combine_args.add_argument('-o', action='store', dest="outputfile",
                              default='combinetree', help='output files name')


def starting(args):
    """
Staring run combine
    :param args: arguments
    """
    pwd = os.getcwd()

    out_put = os.path.join(pwd, args.outputfile)
    docontree(args.inputfile, out_put)
