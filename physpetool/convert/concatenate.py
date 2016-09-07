import os

import time

from physpetool.phylotree.log import getLogging

"""

concatenate the muscle alignment files to only one file.

"""
logconcat = getLogging('concatenate')


def read_fasta_co(fp):
    """read *.fasta file and parse
    :param fp: a fasta format file
    """
    seq_name, seq_pro = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if seq_name: yield (seq_name, ''.join(seq_pro))
            seq_name, seq_pro = line, []
        else:
            seq_pro.append(line.replace(" ", ""))
    if seq_name: yield (seq_name, ''.join(seq_pro))


def cocat(each_muscle_alg):
    """read each files retrun name and sequences append to two list
    :param each_muscle_alg: .fasta file alignment by muscle
    :return: sequence name and sequence
    """
    att_name = []
    each_seq = []
    fr = open(each_muscle_alg)
    with fr as seq:
        for seq_name, seq_pro in read_fasta_co(seq):
            att_name.append(seq_name)
            each_seq.append(seq_pro)
    return (att_name, each_seq)


def cocat_path(muscle_alg):
    """
    Function can be invoked do concatenate:
    :param muscle_alg: a path contain all .fasta files are already alignment by muscle
    :return: the path of .phy file location

    """
    result_dir = os.path.dirname(muscle_alg)
    result = 'concatenate.fasta'
    timeformat = '%Y%m%d%H%M%S'
    timeinfo = str(time.strftime(timeformat))
    subdir = 'concatenate' + timeinfo
    concat_dir = os.path.join(result_dir, subdir)
    # crate a directory to store .phy file
    if not os.path.exists(concat_dir):
        os.makedirs(concat_dir)
    # write concatenate result to file
    result_path = os.path.join(concat_dir, result)
    fw = open(result_path, 'w')
    alg_files = os.listdir(muscle_alg)
    dict = {}
    for eachpro in alg_files:
        path = os.path.join(muscle_alg, eachpro)
        each_k, each_v = cocat(path)
        dict[eachpro] = each_v
    num = len(dict.get(alg_files[0]))
    for i in range(num):
        concat = []
        for j in alg_files:
            concat.append(dict.get(j)[i])
        logconcat.debug('> {0} {1}'.format(each_k[i], ''.join(concat)))
        fw.write(each_k[i] + '\n')
        fw.write(''.join(concat) + '\n')
    logconcat.info("concatenate gene was completed")
    return result_path

if __name__ == '__main__':
    os.chdir("/home/yangfang/physpetools_data/plant/test/")
    cocat_path('test_pro')
