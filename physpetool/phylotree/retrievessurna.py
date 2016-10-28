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
The module retrieve and download SSU rRNA sequence from SILVA Database
"""

import ftplib
import os
import time
from physpetool.phylotree.log import getLogging

log_retrieve = getLogging('SSU rRNA DB')


def retrieve16srna(spenamelist, outpath):
    """
retrieve 16s rna form bioinfor.scu.edu.cn
    :param spenamelist: a list contain species names
    :param outpath: output data path
    :return: download file path
    """
    # pares and cheak species names lsit
    # spelist = []
    # for line in spenamelist:
    #     st = line.strip()
    #     spelist.append(st)
    spelist = spenamelist
    log_retrieve.info('Read organisms names success')
    # makdir tmep directory
    timeformat = '%Y%m%d%H%M%S'
    timeinfo = str(time.strftime(timeformat))
    subdir = 'temp/rna_sequence' + timeinfo
    dirname = os.path.dirname(outpath)
    dirname = os.path.join(dirname, subdir)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    # connect database
    connect = ftplib.FTP("bioinfor.scu.edu.cn")
    connect.login('anonymous')
    connect.cwd('/pub/database16s')
    # connect.dir()
    for abb in spelist:
        retrievename = abb + '.fasta'
        downloadfilname = 'rna_sequence' + '.fasta'
        downloadfilnamepath = os.path.join(dirname, downloadfilname)
        fw = open(downloadfilnamepath, 'ab')
        remoteFileName = 'RETR ' + os.path.basename(retrievename)
        connect.retrbinary(remoteFileName, fw.write, 1024)
        fw.write('\n')
        fw.close()
        log_retrieve.info("Retrieve and download of organism '{0}' SSU rRNA sequence was successful".format(abb))
    connect.quit()

    return dirname
