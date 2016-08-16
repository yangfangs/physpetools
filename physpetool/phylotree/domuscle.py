import subprocess
import os
import os.path

import time

from physpetool.phylotree.log import getLogging
from physpetool.softwares.path import getlocalpath

"""
function to call muscle to do alignment

"""

logdomuscle = getLogging('muscle')


# muscle -in process_L1.txt -out process_L1.afa -maxiters 100
def domuscle(indata, outdata, musclepara):
    """
    call muscle software to do alignment
    :param indata: a director contain a fasta format file or a fasta format file
    :param outdata: the out is abs path with a file name
    :return: outdata path
    """
    muscleparas = musclepara.lstrip()
    mupath = getlocalpath()
    out_path = os.path.dirname(outdata)
    timeformat = '%Y%m%d%H%M%S'
    timeinfo = str(time.strftime(timeformat))
    subdir = 'temp/16srna_alignment' + timeinfo
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
        return out_alg



def domuscle_file(indata_files, outdata, musclepara):
    """
call muscle software to do alignment
    :param indata_files: a directory contain more than one file
    :param outdata: out file after alignment
    :return: path
    """
    muscleparas = musclepara.lstrip()
    mupath = getlocalpath()
    out_path = os.path.dirname(outdata)
    timeformat = '%Y%m%d%H%M%S'
    timeinfo = str(time.strftime(timeformat))
    subdir = 'temp/hcp_alignment' + timeinfo
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
    logdomuscle.info("Multiple sequence alignment by Muscle was completed")
    return muscle_dir
