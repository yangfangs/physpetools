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
function to call FastTree and FastTree reconstruct tree.
"""
import os

import subprocess

from physpetool.phylotree.log import getLogging
from physpetool.softwares.path import getlocalpath

logdofasttree = getLogging('FastTree')


def doFastTree(inputfile, outputfile, FastTreepara, thread):
    # Use FASTA format build tree
    input_fasta = inputfile.replace('.phy', '')
    FastTreePath = getlocalpath()
    thread_to_str = str(thread)
    out_tree_name = os.path.join(outputfile, "FastTree.tree")
    if not os.path.exists(outputfile):
        os.mkdir(outputfile)
    if thread_to_str is '1':
        cmd = FastTreePath + "/FastTree " + FastTreepara + input_fasta + " >" + out_tree_name
        subprocess.call(cmd, shell=True)
    else:
        # set the threads
        os.environ["OMP_NUM_THREADS"] = thread_to_str
        cmd = FastTreePath + "/FastTreeMP " + FastTreepara + input_fasta + " >" + out_tree_name
        subprocess.call(cmd, shell=True)
    logdofasttree.info("Phylogenetic species tree reconstructed by FastTree was completed")


if __name__ == '__main__':
    doFastTree("/home/yangfang/physpetools/testdata/temp/concatenate20160916155942/concatenate.fasta-gb1",
               "/home/yangfang/physpetools_data/test_fasttree/",
               "", "4"
               )
