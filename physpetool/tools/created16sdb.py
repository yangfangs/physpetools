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

"""
Create 16s SSU rRNA database.

"""



import os

def read_fasta_parse(fp):
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


os.chdir('/home/yangfang/physpetools_data/16sRNA')
seq_name = []
seq_pro = []


def parsefastafile(parsefilepath, idfilepath, wdir):
    if not os.path.exists(wdir):
        os.makedirs(wdir)
    ncbi_acc = read_ncbi_id(idfilepath)
    with open(parsefilepath) as read:
        for seq_name, seq_pro in read_fasta_parse(read):
            acc = seq_name.strip().split(' ')[0].replace('>', '')
            ncbi_acc_re = []
            for num in ncbi_acc:
                if num[1] == acc:
                    faname = num[0] + '.fasta'
                    fapath = os.path.join(wdir, faname)
                    fw = open(fapath, 'w')
                    fw.write('>' + num[0] + '\n')
                    fw.write(seq_pro)
                    fw.close()
                    ncbi_acc_re.append(num)
                else:
                    pass
            for line in ncbi_acc_re:
                ncbi_acc.remove(line)

def read_ncbi_id(idfilepath):
    ncbi_acc = []
    with open(idfilepath) as readid:
        for line in readid:
            lin = line.strip().split('\t')
            ncbi_acc.append([lin[0], lin[2]])
    return ncbi_acc


parsefastafile('SILVA_123.1_SSURef_Nr99_tax_silva_trunc.fasta','ncbi_to_silva_id.txt','ftpfiles')


# parsefastafile('silva_test.fasta', 'ncbi_test2.txt', 'testreslult2')


# ncbi_acc = read_ncbi_id('ncbi_to_silva_id.txt')
# print ncbi_acc




# with open('test.fasta') as read:
#     for seq_name, seq_pro in read_fasta_parse(read):
#         acc = seq_name.strip().split(' ')[0].replace('>', '')
#         print acc
