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

import os
import subprocess
import re
from physpetool.phylotree.log import getLogging
from physpetool.softwares.path import getlocalpath

loggtrimal = getLogging('trimal')


# trimal -in concatenate.fasta -out output2 -gt 1 -phylip3.2

def dotrimal(indata, trimalpara):
    """
    do trimal after muslce and concatenate
    :param indata: a fasta file input to do trimal
    :param outdata: append name after
    :return: a file path of trimal result
    """
    # Deal with outdata name
    trimalparas = trimalpara.lstrip()
    trimalpath = getlocalpath()
    out_path = os.path.dirname(indata)
    trimal_name = "trimal.phy"
    trimal_data = os.path.join(out_path, trimal_name)

    cmd = trimalpath + "/trimal " + " -in " + indata + " -out " + trimal_data + " " + trimalparas + " -phylip"

    subprocess.call(cmd, shell=True)
    # support fasttree software
    trimal_data2 = trimal_data.replace('.phy', '')
    cmd2 = trimalpath + "/trimal " + " -in " + indata + " -out " + trimal_data2 + " " + trimalparas + " -fasta"
    subprocess.call(cmd2, shell=True)

    loggtrimal.info('Select conserved blocks by trimal was completed')
    loggtrimal.debug('trimal path:{0}'.format(trimal_data))
    return trimal_data
