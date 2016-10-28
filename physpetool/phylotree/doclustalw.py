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
Module to call clustalw2 to do alignment

"""

# clustalw2 -INFILE=p1.fasta -TYPE=PROTEIN -OUTPUT=FASTA -ALIGN -OUTFILE=test/clustalw_p2.fasta
import os
import subprocess
from physpetool.phylotree.log import getLogging
from physpetool.softwares.path import getlocalpath
from physpetool.utils.outdirforamt import timeformat

logdoclustalw = getLogging('clutalw2')


def doclustalw(indata, outdata, clustalwpara):
    """
    Call clustalw software to do align
    :param indata: a director contain a fasta format file or a fasta format file
    :param outdata: the out is abs path with a file name
    :return: outdata path
    """
    logdoclustalw.debug("clustalw input data:{0}".format(indata))
    type = "-TYPE=DNA"
    if clustalwpara is None:
        clustalwparas = type
    else:
        clustalwparas = type + " " + clustalwpara.lstrip()
    clu_path = getlocalpath()
    out_path = os.path.dirname(outdata)
    doclu_subdir = str(timeformat('temp/rna_sequence'))
    clustalw_dir = os.path.join(out_path, doclu_subdir)
    # check indata type is dir or files?
    if os.path.isdir(indata):
        pro_name = os.listdir(indata)
        if not os.path.exists(clustalw_dir):
            os.makedirs(clustalw_dir)
        out_file = "-OUTFILE=" + os.path.join(clustalw_dir, pro_name[0])
        infile = os.path.join(indata,pro_name[0])
        cmd = clu_path + "/clustalw2 " + "-INFILE=" + infile + " -OUTPUT=FASTA -ALIGN " + out_file + " " + clustalwparas
        subprocess.call(cmd, shell=True)
        logdoclustalw.info("Multiple sequence alignment  by Clustalw2 was completed.")
        out_alg = os.path.join(clustalw_dir, pro_name[0])
        return out_alg
    # indata is a file
    elif os.path.isfile(indata):
        pro_name = indata
        if not os.path.exists(clustalw_dir):
            os.makedirs(clustalw_dir)
        out_file = "-OUTFILE=" + os.path.join(clustalw_dir, pro_name)
        cmd = clu_path + "/clustalw2 " + "-INFILE=" + pro_name + " -OUTPUT=FASTA -ALIGN " + out_file + " " + clustalwparas
        subprocess.call(cmd, shell=True)
        logdoclustalw.info("Multiple sequence alignment  by Clustalw2 was completed.")
        out_alg = os.path.join(clustalw_dir, pro_name)
        return out_alg


def doclustalw_file(indata_files, outdata, clustalwpara):
    """
Call clustalw software to do align
    :param indata_files: a directory contain more than one file
    :param outdata: out file after alignment
    :return: path
    """
    type = "-TYPE=PROTEIN"
    if clustalwpara is None:
        clustalwparas = type
    else:
        clustalwparas = type + " " + clustalwpara.lstrip()

    clu_path = getlocalpath()
    out_path = os.path.dirname(outdata)
    doclu_subdir = str(timeformat('temp/hcp_alignment'))
    clustalw_dir = os.path.join(out_path, doclu_subdir)
    pro_name = os.listdir(indata_files)
    if not os.path.exists(clustalw_dir):
        os.makedirs(clustalw_dir)
    for i in pro_name:
        each_pro = os.path.join(indata_files, i)
        out_file = "-OUTFILE=" + os.path.join(clustalw_dir, i)
        cmd = clu_path + "/clustalw2 " + "-INFILE=" + each_pro + " -OUTPUT=FASTA -ALIGN " + out_file + " " + clustalwparas
        subprocess.call(cmd, shell=True)
    logdoclustalw.info("Multiple sequence alignment by Clustalw2 was completed.")
    return clustalw_dir


if __name__ == '__main__':
    # doclustalw_file("/home/yangfang/physpetools_data/test_clustalw2/input",
    #                 "/home/yangfang/physpetools_data/test_clustalw2/test", "")
    doclustalw("/home/yangfang/physpetools_data/test_clustalw2/16srandata.fasta",
               "/home/yangfang/physpetools_data/test_clustalw2/test", '')
