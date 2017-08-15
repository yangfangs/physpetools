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
Module to call mafft to do alignment
"""

import subprocess
import os
import os.path
import time
from physpetool.phylotree.log import getLogging
from physpetool.softwares.path import getlocalpath

logmafft = getLogging('mafft')


# mafft --auto p1.fasta > output
def domafft(indata, outdata, mafftparas):
    """
    call mafft software to do align
    :param indata: a director contain a fasta format file or a fasta format file
    :param outdata: the out is abs path with a file name
    :return: outdata path
    """
    mafftparas = mafftparas.lstrip()
    mapath = getlocalpath()
    out_path = os.path.dirname(outdata)
    timeformat = '%Y%m%d%H%M%S'
    timeinfo = str(time.strftime(timeformat))
    subdir = 'temp/rna_alignment' + timeinfo
    mafft_dir = os.path.join(out_path, subdir)
    # check indata type
    if os.path.isdir(indata):
        pro_name = os.listdir(indata)
        if not os.path.exists(mafft_dir):
            os.makedirs(mafft_dir)
        out_alg = os.path.join(mafft_dir, pro_name[0])
        each_pro = os.path.join(indata, pro_name[0])
        cmd = mapath + "/mafft " + mafftparas + " " + each_pro + " > " + out_alg
        subprocess.call(cmd, shell=True)
        logmafft.debug('mafft result path:{0}'.format(out_alg))
        logmafft.info("Multiple sequence alignment by mafft was completed.")
        return out_alg
    elif os.path.isfile(indata):
        pro_name = indata
        if not os.path.exists(mafft_dir):
            os.makedirs(mafft_dir)
        out_alg = os.path.join(mafft_dir, pro_name)
        each_pro = pro_name
        cmd = mapath + "/mafft " + mafftparas + " " + each_pro + " > " + out_alg
        subprocess.call(cmd, shell=True)
        logmafft.debug('mafft result path:{0}'.format(out_alg))
        logmafft.info("Multiple sequence alignment by mafft was completed.")
        return out_alg


def domafft_file(indata_files, outdata, mafftparas):
    """
call mafft software to do align
    :param indata_files: a directory contain more than one file
    :param outdata: out file after alignment
    :return: path
    """
    mafftparas = mafftparas.lstrip()
    mapath = getlocalpath()
    out_path = os.path.dirname(outdata)
    timeformat = '%Y%m%d%H%M%S'
    timeinfo = str(time.strftime(timeformat))
    subdir = 'temp/alignment' + timeinfo
    mafft_dir = os.path.join(out_path, subdir)
    # mafft_dir = os.path.join(indata_files, 'muscle_alignment')
    pro_name = os.listdir(indata_files)
    if not os.path.exists(mafft_dir):
        os.makedirs(mafft_dir)
    for i in pro_name:
        out_alg = os.path.join(mafft_dir, i.split('.')[0])
        each_pro = os.path.join(indata_files, i)
        cmd = mapath + "/mafft " + mafftparas + " " + each_pro + " > " + out_alg
        subprocess.call(cmd, shell=True)
    logmafft.info("Multiple sequence alignment by mafft was completed.")
    return mafft_dir