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

The module retrieve highly conserved proteins and download from KEGG database


"""
import shutil
import glob
import ftplib
import os
import sqlite3
import time
from physpetool.database.dbpath import getlocaldbpath
from physpetool.phylotree.log import getLogging
from physpetool.tools.keggapi import getprotein

logretrieveprotein = getLogging('KEGG INDEX DB')
KEGGDB = "KEGG_DB_3.0.db"


def getspecies(spelist, colname):
    """
    Get species protein index for DB
    :param name: a list contain abbreviation species nam
    :param colname: a list contain colname of DB
    :return: a list contain protein index can be retrieved and a match ko list (is a ko id list)
    """
    dbpath = getlocaldbpath()
    db = os.path.join(dbpath, KEGGDB)
    relist = []
    match_ko_name = []
    conn = sqlite3.connect(db)
    conn.text_factory = str
    c = conn.cursor()
    if len(spelist) >= 1000:
        sp = splist(spelist,500)
    else:
        sp = [spelist]

    for ko in colname:
        tem_reslist = []
        tem_none = 0
        for line in sp:
            connect = "' OR NAME = '".join(line)
            query = "SELECT " + ko + " FROM proindex WHERE NAME = '" + connect + "'"
            c.execute(query)
            ids = list(c.fetchall())
            idslist = [str(x[0]) for x in ids]

            num_none = len([x for x in idslist if x == 'None'])
            tem_none += num_none

            tem_reslist.extend(idslist)

        if tem_none != len(tem_reslist):
            relist.append(tem_reslist)
            match_ko_name.append(ko)

    c.close()
    return relist, match_ko_name


def getcolname():
    """get BD colnames"""
    dbpath = getlocaldbpath()
    db = os.path.join(dbpath, KEGGDB)
    conn = sqlite3.connect(db)
    conn.text_factory = str
    c = conn.cursor()
    c.execute("SELECT * FROM proindex")
    col_name_list = [tuple[0] for tuple in c.description]
    c.close()
    return col_name_list[2:]


def splist(l, s):
    """split a list to sub list contain s"""
    return [l[i:i + s] for i in range(len(l)) if i % s == 0]



def retrieveprotein(proindexlist, outpath, matchlist, spelist, local_db):
    """
    Retrieve proteins form Kegg DB
    :param proindexlist: a list contain protein index
    :param outpath: user input outpath
    :return: retrieve protein path
    """
    timeformat = '%Y%m%d%H%M%S'
    timeinfo = str(time.strftime(timeformat))
    subdir = 'temp/conserved_protein' + timeinfo
    dirname = os.path.dirname(outpath)
    dirname = os.path.join(dirname, subdir)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    fasta = {}
    p = 1

    # get hcp proteins form ftp server
    if local_db == "":
        connect = ftplib.FTP("173.255.208.244")
        connect.login('anonymous')
        connect.cwd('/pub/databasehcp')

        for line in spelist:
            w_file = dirname + "/" + line + ".fa"
            fw_ = open(w_file, 'ab')
            retrievename = line + '.fasta'
            remoteFileName = 'RETR ' + os.path.basename(retrievename)
            connect.retrbinary(remoteFileName, fw_.write)
            fw_.write(b'\n')
            fw_.close()
            logretrieveprotein.info("Retrieve " + line + " highly conserved proteins completed")
            # read get sequences
            with open(w_file, 'r') as f:
                for line in f:
                    if line != "\n":
                        tem = line.strip()
                        if tem[0] == '>':
                            header = tem[1:]
                        else:
                            sequence = tem
                            fasta[header] = fasta.get(header, '') + sequence
        connect.quit()
    # get protein sequence from local
    else:
        for line in spelist:
            file_name = line +".fasta"
            file_name_new = line + ".fa"
            abb_data_path = os.path.join(local_db,file_name)
            abb_data_path_new = os.path.join(dirname,file_name_new)
            shutil.copyfile(abb_data_path,abb_data_path_new)
            logretrieveprotein.info("Retrieve " + line + " highly conserved proteins completed")
            # read get sequences
            with open(abb_data_path_new, 'r') as f:
                for line in f:
                    if line != "\n":
                        tem = line.strip()
                        if tem[0] == '>':
                            header = tem[1:]
                        else:
                            sequence = tem
                            fasta[header] = fasta.get(header, '') + sequence

    for index in proindexlist:
        have_none = False
        none_num = len([x for x in index if x == 'None'])
        app_spe = []
        if none_num != len(index):
            q_index = [var for var in index if var != 'None']
            have_spe = [x.split(":")[0] for x in q_index]
            app_spe = [x for x in spelist if x not in have_spe]
            have_none = True
        else:
            q_index = index

        hcp_pro_name = hcp_name(matchlist[p - 1])

        wfiles = "{0}/p{1}.fasta".format(dirname, p)
        fw = open(wfiles, 'a')

        for id in q_index:
            abb_name = id.strip().split(":")[0]
            if id in fasta.keys():
                fw.write(">"+abb_name+"\n"+fasta[id]+"\n")
            else:
                name_none = ">" + abb_name + "\n"
                fw.write(name_none + "M" + "\n")
        if have_none:
            for line in app_spe:
                name_none = ">" + line + "\n"
                fw.write(name_none + "M" + "\n")
        fw.close()

        logretrieveprotein.info(
            "Retrieve and download of highly conserved protein '{0}' was successful store in p{1}.fasta file".format(
                hcp_pro_name, str(p)))
        p += 1
    logretrieveprotein.info("Retrieve from KEGG database " + str(p - 1) + " highly conserved proteins")

    for infile in glob.glob(os.path.join(dirname, '*.fa')):
        os.remove(infile)
    return dirname


def doretrieve(specieslistfile, outpath,local_db):
    '''main to  retrieve protein from kegg db'''
    # spelist = []
    # for line in specieslistfile:
    #     st = line.strip()
    #     spelist.append(st)
    spelist = specieslistfile
    logretrieveprotein.info("Reading organisms's names success!")
    colname = getcolname()
    proindexlist, matchlist = getspecies(spelist, colname)
    dirpath = retrieveprotein(proindexlist, outpath, matchlist, spelist,local_db)
    return dirpath


def hcp_name(index):
    """get highly conserved protein names from ko list"""
    ko_path = getlocaldbpath()
    pro_ko = os.path.join(ko_path, "protein_ko.txt")
    with open(pro_ko) as ko:
        for line in ko:
            name = line.strip().split(',')
            if name[1] == index:
                return name[0]


if __name__ == '__main__':
    print(getcolname())
    print(getspecies(['swe'], ['K01409']))
    # for line in getcolname():
    #     if getspecies(['mdm'], [line])[0] != []:
    #         proid = getspecies(['mdm'], [line])[0][0][0]
    #         print("http://rest.kegg.jp/get/" + proid + "/aaseq")
    specieslistfile = ['zma', "ath", "eco"]
    outpath = "/home/yangfang/test/alg2/"
    doretrieve(specieslistfile, outpath,local_db="")
