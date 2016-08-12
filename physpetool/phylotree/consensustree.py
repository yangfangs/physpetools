import subprocess

from physpetool.softwares.path import getlocalpath


def docontree(input, output):
    raxmlpath = getlocalpath()

    consensuseCmd = raxmlpath + "/raxmlHPC-PTHREADS-AVX " + " -J MR -m GTRCAT -z " + input + " -w " + output + " -n T1"
    subprocess.call(consensuseCmd, shell=True)
