import os
import subprocess

from physpetool.phylotree.log import getLogging
from physpetool.softwares.path import getlocalpath

logdoraxml = getLogging('RAxML')
"""
function to call RAxML construct tree

"""


# raxmlHPC-PTHREADS-AVX -f a -T 6 -w /home/yangfang/test_raxml/test3
# -m PROTGAMMAJTTX -o aoe -p 12345 -x 12345 -#autoMRE
# -s /home/yangfang/test_raxml/protein_alignment.fasta-gb1.phy -n T1


def doraxml(inputfile, outputfile, raxmlpara, thread):
    """
call RAxML method to construct species tree
    :param inputfile: abs path of .phy format files
    :param outputfile: a file contain RAxML result
    """
    raxmlparalist = raxmlpara.split(" ")
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
    cmd = strs + " -s " + inputfile + " -w " + outputfile
    subprocess.call(cmd, shell=True)
    logdoraxml.info("species phylogenetic constructed by RAxML was completed")
