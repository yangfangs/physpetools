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
function to call iqtree and iqtree reconstruct tree.
"""
import os

import subprocess

from physpetool.phylotree.log import getLogging
from physpetool.softwares.path import getlocalpath

logdoiqtree = getLogging('iqtree')


def doiqtree(inputfile, outputfile, iqtreepara, thread):
    # Use FASTA format build tree
    # input_fasta = inputfile.replace('.phy', '')
    iqtreePath = getlocalpath()
    thread_to_str = str(thread)
    out_tree_name = os.path.join(outputfile, "iqtree.tree")
    if not os.path.exists(outputfile):
        os.mkdir(outputfile)
    if thread_to_str is '1':
        cmd = iqtreePath + "/iqtree " + "-s " + inputfile + " -pre " + out_tree_name + iqtreepara
        subprocess.call(cmd, shell=True)
    else:
        # set the threads
        cmd = iqtreePath + "/iqtree " + "-s " + inputfile + " -pre " + out_tree_name + " -nt " + thread_to_str + iqtreepara
        subprocess.call(cmd, shell=True)
    logdoiqtree.info("Phylogenetic species tree reconstructed by iqtree was completed")


if __name__ == '__main__':
    doiqtree("/home/yangfang/PhySpeTree/iqtree-1.6.9-Linux/example.phy",
               "/home/yangfang/PhySpeTree/iqtree-1.6.9-Linux/test/",
               " -m MF", "1"
               )
