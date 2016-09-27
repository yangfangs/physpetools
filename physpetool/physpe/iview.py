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
The arguments parse module for iview module.

"""

import os
from physpetool.view.annotatingtree import colorRange
from physpetool.view.changelabels import annotatingLabels

APP_DESC = ""


def start_args(input):
    """
Arguments parse
    :param input:  Arguments
    """
    taxonomy = ['kingdom', 'phylum', 'class', 'order']
    taxon = ', '.join(taxonomy)
    annotation_args = input.add_argument_group("ANNOTATION OPTIONS")
    annotation_args.add_argument('-i', action='store', dest="inputfile",
                                 help="Input organisms names file, which used reconstructed \
                              phylogenetic tree.")
    annotation_args.add_argument('-o', action='store', dest="outputfile",
                                 default='iview', help="It's a directory name contain iview convert files to \
                               view tree by use iTol v3 web applications. default output directory is iview.")

    annotation_args.add_argument('-r', '--range', action='store_true', dest="colorrange", default=False,
                                 help="Colored ranges by %s, you can choice one. The default is phylum." % (taxon))

    annotation_args.add_argument('-a', action='store', dest="assign", choices=taxonomy, default='phylum',
                                 help="Colored ranges by user, choice form [%s]." % (taxon))

    annotation_args.add_argument('-l', '--labels', action='store_true', dest="labels", default=False,
                                 help="Change labels from abbreviation names to full names.")


def starting(args):
    """
Staring run combine
    :param args: arguments
    """
    pwd = os.getcwd()
    out_put = os.path.join(pwd, args.outputfile)
    if args.colorrange:
        colorRange(args.inputfile, out_put, args.assign)
    elif args.labels:
        annotatingLabels(args.inputfile, args.outputfile)
