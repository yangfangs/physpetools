import subprocess
import os
import os.path

"""
function to call muscle to do alignment

"""


# muscle -in process_L1.txt -out process_L1.afa -maxiters 100
def domuscle(indata, outdata):
    """
    call muscle software to do alignment
    :param indata: only one file must fasta format
    :param outdata: the out is abs path with a file name
    :return: outdata path
    """
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


def domuscle_file(indata_files, outdata):
    """
call muscle software to do alignment
    :param indata_files: a directory contain more than one file
    :param outdata: out file after alignment
    :return: path
    """
    out_path = os.path.dirname(outdata)
    muscle_dir = os.path.join(out_path, 'muscle_alignment_pro')
    # muscle_dir = os.path.join(indata_files, 'muscle_alignment')
    pro_name = os.listdir(indata_files)
    if os.path.exists(muscle_dir):
        pass
    else:
        os.mkdir(muscle_dir)
    for i in pro_name:
        out_alg = os.path.join(muscle_dir, i.split('.')[0])
        each_pro = os.path.join(indata_files, i)
        cmd = "muscle -in " + each_pro + " -out " + out_alg
        subprocess.call(cmd, shell=True)
    return muscle_dir