"""
function to call muscle to do alignment

"""

# muscle -in process_L1.txt -out process_L1.afa -maxiters 100
import subprocess


def domuscle(indata, outdata):
    cmd = "muscle -in " + indata + " -out " + outdata
    subprocess.call(cmd, shell=True)
    # pro = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    # pro.communicate()

domuscle("/home/yangfang/physpetools/tests/protein.fastq", "/home/yangfang/physpetools/tests/protein_alignment.fasta")

