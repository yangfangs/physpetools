# ########################## Copyrights and License ############################
#                                                                              #
# Copyright 2016 Yang Fang <yangfangscu@gmail.com>                             #
#                                                                              #
# This file is part of Physpe.                                                 #
# https://xiaofeiyangyang.github.io/physpetools/                               #
#                                                                              #
# Physpe is free software: you can redistribute it and/or modify it under      #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# Physpe is distributed in the hope that it will be useful, but WITHOUT ANY    #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with Physpe. If not, see <http://www.gnu.org/licenses/>.               #
#                                                                              #
# ##############################################################################

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
    clustalwpara = "-TYPE=DNA"
    clustalwparas = clustalwpara.lstrip()
    clu_path = getlocalpath()
    out_path = os.path.dirname(outdata)
    doclu_subdir = str(timeformat('temp/hcp_alignment'))
    clustalw_dir = os.path.join(out_path, doclu_subdir)
    if not os.path.exists(clustalw_dir):
        os.makedirs(clustalw_dir)
    out_file = "-OUTFILE=" + os.path.join(clustalw_dir, indata)
    cmd = clu_path + "/clustalw2 " + "-INFILE=" + indata + " -OUTPUT=FASTA -ALIGN " + out_file + " " + clustalwpara
    subprocess.call(cmd, shell=True)
    logdoclustalw.info("Multiple sequence alignment  by Clustalw2 was completed.")
    return clustalw_dir


def doclustalw_file(indata_files, outdata, clustalwpara):
    clustalwpara = "-TYPE=PROTEIN"
    clustalwparas = clustalwpara.lstrip()
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
        cmd = clu_path + "/clustalw2 " + "-INFILE=" + each_pro + " -OUTPUT=FASTA -ALIGN " + out_file + " " + clustalwpara
        subprocess.call(cmd, shell=True)
    logdoclustalw.info("Multiple sequence alignment  by Clustalw2 was completed.")
    return clustalw_dir


if __name__ == '__main__':
    # doclustalw_file("/home/yangfang/physpetools_data/test_clustalw2/input",
    #                 "/home/yangfang/physpetools_data/test_clustalw2/test", "")
    doclustalw("/home/yangfang/physpetools_data/test_clustalw2/16srandata.fasta",
               "/home/yangfang/physpetools_data/test_clustalw2/test",'')