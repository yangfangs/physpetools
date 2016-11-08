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
from physpetool.view.annotatingtree import colorRange, colorLabel
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
                                 help="Input a TXT file contain species names (abbreviated names) are same \
                                with KEGG species abbreviation.")

    annotation_args.add_argument('-o', action='store', dest="outputfile",
                                 default='iview', help="A directory contain the generate configure files. \
                               The directory name is iview")

    annotation_args.add_argument('-r', '--range', action='store_true', dest="colorrange", default=False,
                                 help="Annotating labels with ranges by %s. The default is phylum." % (taxon))

    annotation_args.add_argument('-c', '--color', action='store_true', dest="colorlabel", default=False,
                                 help="Annotating labels without ranges by %s. The default is phylum." % (taxon))

    annotation_args.add_argument('-a', action='store', dest="assign", choices=taxonomy, default='phylum',
                                 help="Colored ranges by user choice form [%s]." % (taxon))

    annotation_args.add_argument('-l', '--labels', action='store_true', dest="labels", default=False,
                                 help="Change species labels from abbreviated names to full names.")


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
    elif args.colorlabel:
        colorLabel(args.inputfile, out_put, args.assign)