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
The main module as enter point and contain a main() function to invoke other
modules as pipeline.
"""

from physpetool.physpe import autobuild
from physpetool.physpe import check
from physpetool.physpe import combine
from physpetool.physpe import build
from physpetool.physpe import iview
from physpetool.version import version_infor
from physpetool.version import version
import argparse
import sys

# PhySpeTree version
physeptree_version = version

APP_DESC = (
    """
          -------------------------------------------------------------------------------------
                      PhySpeTree (%s) - Reconstruct Phylogenetic species Tree

          Citation:
                  PhySpeTree: automatically reconstructing phylogenetic species tree (submitted)

          --------------------------------------------------------------------------------------
          """ % (physeptree_version))


def main():
    start(sys.argv)


def start(input):
    if len(input) > 1:
        command = input[1]
        if command == "version":
            version_infor()
            return

    parser = argparse.ArgumentParser(description=APP_DESC,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    subparser = parser.add_subparsers(title="RCONSTRUCT PHYLOGENETIC TREE")

    # autobuild
    physpe_autobuid = subparser.add_parser("autobuild", help="Auto reconstruct phylogenetic tree")
    physpe_autobuid.set_defaults(func=autobuild.starting)
    autobuild.start_args(physpe_autobuid)

    # combine
    physpe_combine = subparser.add_parser("combine", help="Combine phylogenetic tree")
    physpe_combine.set_defaults(func=combine.starting)
    combine.start_args(physpe_combine)

    # iview
    physpe_iview = subparser.add_parser("iview", help="View tree by iTol")
    physpe_iview.set_defaults(func=iview.starting)
    iview.start_args(physpe_iview)

    # build
    physpe_build = subparser.add_parser("build", help="Extend phylogenetic tree with new species")
    physpe_build.set_defaults(func=build.starting)
    build.start_args(physpe_build)

    # check
    physpe_check = subparser.add_parser("check", help="Check organism database and prepare for extend tree files")
    physpe_check.set_defaults(func=check.starting)
    check.start_args(physpe_check)

    if len(input) == 1:
        print(APP_DESC)
        parser.print_usage()
        print('Please use program option for details')
        print('Example: \n$ PhySpeTree autobuild -h')
        return
    args = parser.parse_args(input[1:])
    # call subparser
    args.func(args)


if __name__ == '__main__':
    main()
    # start([......])
