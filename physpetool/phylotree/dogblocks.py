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
Gblocks module: do gblocks before aligned sequences.

"""
import os
import subprocess
import re
from physpetool.phylotree.log import getLogging
from physpetool.softwares.path import getlocalpath

loggblocks = getLogging('Gblocks')


# Gblocks protein_alignment.fasta -t=p -e=-gb1 -b4=5 -d=y

def dogblocks(indata, gblockpara):
    """
    do gblocks after muslce and concatenate
    :param indata: a fasta file input after gblock
    :param outdata: append name after gblocks
    :return: a file path of gblocks result
    """
    # Deal with outdata name
    gblockparas = gblockpara.lstrip()
    gblockparalist = gblockparas.split(" ")
    regex = '-e='
    for i in range(0, len(gblockparalist)):
        if re.search(regex, gblockparalist[i]):
            index = i
            break
    outnamepara = gblockparalist[index]
    outdata = outnamepara.split('=')[1]
    gblockpath = getlocalpath()
    alg_name = os.path.basename(indata)
    out_path = os.path.dirname(indata)
    gblock_name = alg_name + outdata
    gblock_data = os.path.join(out_path, gblock_name)

    cmd = gblockpath + "/Gblocks " + indata + " " + gblockparas
    subprocess.call(cmd, shell=True)
    loggblocks.info('Select conserved blocks by Gblocks was completed')
    loggblocks.debug('Gblocks path:{0}'.format(gblock_data))
    return gblock_data
