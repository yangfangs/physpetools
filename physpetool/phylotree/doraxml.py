import os
import subprocess
"""
function to call RAxML construct tree

"""

#raxmlHPC-PTHREADS-AVX -f a -T 6 -w /home/yangfang/test_raxml/test3
# -m PROTGAMMAJTTX -o aoe -p 12345 -x 12345 -#autoMRE
# -s /home/yangfang/test_raxml/protein_alignment.fasta-gb1.phy -n T1




def doraxml(inputfile,outputfile):
    """
call RAxML method to construct species tree
    :param inputfile: abs path of .phy format files
    :param outputfile: a file contain RAxML result
    """
    if os.path.exists(outputfile):
        pass
    else:
        os.mkdir(outputfile)
    str = "raxmlHPC-PTHREADS-AVX -f a -T 6 -m PROTGAMMAJTTX -o hsa -p 12345 -x 12345 -# 100 -n T1"
    cmd = str + " -s " + inputfile + " -w " + outputfile
    print cmd
    subprocess.call(cmd, shell=True)




