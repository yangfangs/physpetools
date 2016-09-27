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
Deal with SILVA database data for create 16s SSU rRNA database.

"""

import os


def convert_ncbi_id(read, write):
    """
convert taxmap_emble file to accession silva id
    :param read: taxmap emble file
    :param write: write file user rename
    """
    fw = open(write, 'w')
    with open(read) as read:
        for line in read:
            tem = line.strip().split('\t')
            col1 = '{0}.{1}.{2}'.format(tem[0], tem[1], tem[2])
            col2 = tem[-1]
            fw.write(col1 + '\t' + col2 + '\n')
    fw.close()


def convert_ncbi_silva(ncbilist, silvalist):
    """
convert ncbi id to silva accession
    :param ncbilist: a txt file contain ncbi id list
    :param silvalist: a txt file contain silva id list
    """
    fw = open('ncbi_to_silva_id.txt', 'a')
    with open(ncbilist) as read:
        for line in read:
            nid = line.strip().split('\t')
            nid1 = nid[1].strip()
            for silvaid in open(silvalist):
                sid = silvaid.strip().split('\t')
                sid1 =sid[1].strip()
                if nid1 == sid1:
                    print nid1
                    fw.write(nid[0] + '\t' + nid[1] + '\t' + sid[0] + '\n')
                    break
                else:
                    pass
    fw.close()


os.chdir('/home/yangfang/physpetools_data/16sRNA')
# convert_ncbi_id('taxmap_embl_ssu_ref_123.1.txt', 'silva_map_ncbi_ref.txt')
convert_ncbi_silva('organism_convert_to_tax.txt', 'silva_map_ncbi_NR.txt')
