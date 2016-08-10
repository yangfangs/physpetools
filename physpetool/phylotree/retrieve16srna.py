import ftplib
import os

import time

from physpetool.phylotree.log import getLogging

logretrieve16srna = getLogging('16s DB')


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
    spelist =spenamelist
    logretrieve16srna.info('Read organisms names successful')
    # makdir tmep directory
    timeformat = '%Y%m%d%H%M%S'
    timeinfo = str(time.strftime(timeformat))
    subdir = 'temp/16srnadata' + timeinfo
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
        downloadfilname = '16srandata' + '.fasta'
        downloadfilnamepath = os.path.join(dirname, downloadfilname)
        fw = open(downloadfilnamepath, 'ab')
        remoteFileName = 'RETR ' + os.path.basename(retrievename)
        connect.retrbinary(remoteFileName, fw.write, 1024)
        fw.write('\n')
        fw.close()
    connect.quit()
    logretrieve16srna.debug(dirname)
    return dirname
