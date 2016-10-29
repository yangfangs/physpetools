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
Module to call muscle to do alignment
"""

import subprocess
import os
import os.path
import time
from physpetool.phylotree.log import getLogging
from physpetool.softwares.path import getlocalpath

logdomuscle = getLogging('muscle')


# muscle -in process_L1.txt -out process_L1.afa -maxiters 100
def domuscle(indata, outdata, musclepara):
    """
    call muscle software to do align
    :param indata: a director contain a fasta format file or a fasta format file
    :param outdata: the out is abs path with a file name
    :return: outdata path
    """
    muscleparas = musclepara.lstrip()
    mupath = getlocalpath()
    out_path = os.path.dirname(outdata)
    timeformat = '%Y%m%d%H%M%S'
    timeinfo = str(time.strftime(timeformat))
    subdir = 'temp/rna_alignment' + timeinfo
    muscle_dir = os.path.join(out_path, subdir)
    # check indata type
    if os.path.isdir(indata):
        pro_name = os.listdir(indata)
        if not os.path.exists(muscle_dir):
            os.makedirs(muscle_dir)
        out_alg = os.path.join(muscle_dir, pro_name[0])
        each_pro = os.path.join(indata, pro_name[0])
        cmd = mupath + "/muscle -in " + each_pro + " -out " + out_alg + " " + muscleparas
        subprocess.call(cmd, shell=True)
        logdomuscle.debug('muscle result path:{0}'.format(out_alg))
        logdomuscle.info("Multiple sequence alignment by Muscle was completed.")
        return out_alg
    elif os.path.isfile(indata):
        pro_name = indata
        if not os.path.exists(muscle_dir):
            os.makedirs(muscle_dir)
        out_alg = os.path.join(muscle_dir, pro_name)
        each_pro = pro_name
        cmd = mupath + "/muscle -in " + each_pro + " -out " + out_alg + " " + muscleparas
        subprocess.call(cmd, shell=True)
        logdomuscle.debug('muscle result path:{0}'.format(out_alg))
        logdomuscle.info("Multiple sequence alignment by Muscle was completed.")
        return out_alg


def domuscle_file(indata_files, outdata, musclepara):
    """
call muscle software to do align
    :param indata_files: a directory contain more than one file
    :param outdata: out file after alignment
    :return: path
    """
    muscleparas = musclepara.lstrip()
    mupath = getlocalpath()
    out_path = os.path.dirname(outdata)
    timeformat = '%Y%m%d%H%M%S'
    timeinfo = str(time.strftime(timeformat))
    subdir = 'temp/alignment' + timeinfo
    muscle_dir = os.path.join(out_path, subdir)
    # muscle_dir = os.path.join(indata_files, 'muscle_alignment')
    pro_name = os.listdir(indata_files)
    if not os.path.exists(muscle_dir):
        os.makedirs(muscle_dir)
    for i in pro_name:
        out_alg = os.path.join(muscle_dir, i.split('.')[0])
        each_pro = os.path.join(indata_files, i)
        cmd = mupath + "/muscle -in " + each_pro + " -out " + out_alg + " " + muscleparas
        subprocess.call(cmd, shell=True)
    logdomuscle.info("Multiple sequence alignment by Muscle was completed.")
    return muscle_dir
