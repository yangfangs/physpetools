import os
import subprocess
import re
from physpetool.phylotree.log import getLogging
from physpetool.softwares.path import getlocalpath

"""
function call gblock block the anligment data forme muscle.
/home/yangfang/physpetools/testdata/muscle_alignment/protein.fastq.alg-gb1
"""

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
    loggblocks.debug('Gblocks indata:{0}'.format(indata))
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
    loggblocks.info('Gblocks was completed')
    loggblocks.debug('Gblocks path:{0}'.format(gblock_data))
    return gblock_data
