import subprocess
import os
import os.path

"""
function to call muscle to do alignment

"""


# muscle -in process_L1.txt -out process_L1.afa -maxiters 100
def domuscle(indata, outdata):
    out_path = os.path.dirname(outdata)
    fa_name = os.path.basename(indata)
    muscle_dir = os.path.join(out_path, 'muscle_alignment')

    if os.path.exists(muscle_dir):
        pass
    else:
        os.mkdir(muscle_dir)
    muscle_file = fa_name + '.alg'

    out_alg = os.path.join(muscle_dir, muscle_file)


    cmd = "muscle -in " + indata + " -out " + out_alg

    subprocess.call(cmd, shell=True)
    return out_alg