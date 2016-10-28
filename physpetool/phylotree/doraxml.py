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
function to call RAxML construct tree
"""

import os
import subprocess
from physpetool.phylotree.log import getLogging
from physpetool.softwares.path import getlocalpath

logdoraxml = getLogging('RAxML')


def doraxml(inputfile, outputfile, raxmlpara, thread):
    """
call RAxML method to construct species tree
    :param inputfile: abs path of .phy format files
    :param outputfile: a file contain RAxML result
    """
    raxmlparas = raxmlpara.lstrip()

    raxmlparalist = raxmlparas.split(" ")
    tpara = '-T'
    if tpara in raxmlparalist:
        index = raxmlparalist.index(tpara)
        raxmlparalist.remove(raxmlparalist[index])
        raxmlparalist.remove(raxmlparalist[index])
        raxmlpararet = ' '.join(raxmlparalist)
    else:
        raxmlpararet = raxmlpara
    threadtostr = str(thread)
    raxmlpath = getlocalpath()
    if not os.path.exists(outputfile):
        os.mkdir(outputfile)
    strs = raxmlpath + "/raxmlHPC-PTHREADS-AVX " + "-T " + threadtostr + " " + raxmlpararet
    # cmd command
    cmd = strs + " -s " + inputfile + " -w " + outputfile
    subprocess.call(cmd, shell=True)
    logdoraxml.info("Phylogenetic species tree reconstructed by RAxML was completed")
