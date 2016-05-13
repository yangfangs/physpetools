"""
function call gblock block the anligment data forme muscle.

"""

# Gblocks protein_alignment.fasta -t=p -e=-gb1 -b4=5 -d=y
import subprocess


def dogblocks(indata, outdata):
    cmd = "Gblocks " + indata + " -t=p" + " -e=-" + outdata
    subprocess.call(cmd, shell=True)
    # pro = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    # pro.communicate()
    print cmd

dogblocks("/home/yangfang/physpetools/tests/protein_alignment.fasta","gb1")
