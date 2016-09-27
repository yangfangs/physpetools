# ########################## Copyrights and License #############################
#                                                                               #
# Copyright 2016 Yang Fang <yangfangscu@gmail.com>                              #
#                                                                               #
# This file is part of PhySpeTree.                                              #
# https://xiaofeiyangyang.github.io/physpetools/                                #
#                                                                               #
# PhySpeTree is free software: you can redistribute it and/or modify it under   #
# the terms of the GNU Lesser General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)     #
# any later version.                                                            #
#                                                                               #
# PhySpeTree is distributed in the hope that it will be useful, but WITHOUT ANY #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS     #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  #
# details.                                                                      #
#                                                                               #
# You should have received a copy of the GNU Lesser General Public License      #
# along with PhySpeTree. If not, see <http://www.gnu.org/licenses/>.            #
#                                                                               #
# ###############################################################################

import os
import time
from physpetool.phylotree.log import getLogging

"""

Concatenate the muscle alignment files to one file.

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
    dict_abb = {}
    for eachpro in alg_files:
        path = os.path.join(muscle_alg, eachpro)
        each_k, each_v = cocat(path)
        dict_abb[eachpro] = each_k
        dict[eachpro] = each_v
    # Get all abb names
    all_abb = dict_abb.get(alg_files[0])
    # Concatenate
    for i in all_abb:
        concat = []
        for j in alg_files:
            index_abb = dict_abb.get(j).index(i)
            concat.append(dict.get(j)[index_abb])
        fw.write(i + '\n')
        fw.write(''.join(concat) + '\n')

    logconcat.info("Concatenate highly conserved proteins was completed")
    return result_path
