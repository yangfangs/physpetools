import subprocess
import os

"""
function call gblock block the anligment data forme muscle.
/home/yangfang/physpetools/testdata/muscle_alignment/protein.fastq.alg-gb1
"""


# Gblocks protein_alignment.fasta -t=p -e=-gb1 -b4=5 -d=y

def dogblocks(indata, outdata):
    alg_name = os.path.basename(indata)
    out_path = os.path.dirname(indata)
    gblock_name = alg_name + '-' + outdata
    gblock_data = os.path.join(out_path, gblock_name)

    cmd = "Gblocks " + indata + " -t=p" + " -e=-" + outdata
    subprocess.call(cmd, shell=True)
    return gblock_data
