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

import os
import sqlite3
import time
from physpetool.database.dbpath import getlocaldbpath
from physpetool.phylotree.log import getLogging
from physpetool.tools.keggapi import getprotein

logretrieveprotein = getLogging('KEGG INDEX DB')


def getspecies(name, colname):
    """
    Get species protein index for DB
    :param name: a list contain abbreviation species nam
    :param colname: a list contain colname of DB
    :return: a list contain protein index can be retrieved and a match ko list (is a ko id list)
    """
    dbpath = getlocaldbpath()
    db = os.path.join(dbpath, "KEGG_DB_1.0.db")
    relist = []
    match_ko_name = []
    conn = sqlite3.connect(db)
    conn.text_factory = str
    c = conn.cursor()
    connect = "' OR NAME = '".join(name)
    for ko in colname:

        query = "SELECT " + ko + " FROM proindex WHERE NAME = '" + connect + "'"
        c.execute(query)
        ids = list(c.fetchall())
        idslist = [str(x[0]) for x in ids]
        if 'None' not in idslist:
            relist.append(idslist)
            match_ko_name.append(ko)
        else:
            pass
    c.close()
    return relist, match_ko_name


def getcolname():
    """get BD colnames"""
    dbpath = getlocaldbpath()
    db = os.path.join(dbpath, "KEGG_DB_1.0.db")
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


def retrieveprotein(proindexlist, outpath, matchlist):
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
    p = 1
    for index in proindexlist:
        hcp_pro_name = hcp_name(matchlist[p - 1])

        wfiles = "{0}/p{1}.fasta".format(dirname, p)
        f = open(wfiles, "a")
        spprolist = splist(index, 10)
        for id in spprolist:
            query = "+".join(id)
            protein = getprotein(query)
            protein = protein.readlines()
            for i in protein:
                if i.startswith(">"):
                    abbname = i.split(":")[0] + "\n"
                    f.write(abbname)
                else:
                    f.write(i)
        f.close()
        logretrieveprotein.info(
            "Retrieve and download of highly conserved protein '{0}' was successful store in p{1}.fasta file".format(hcp_pro_name, str(p)))
        p += 1
    logretrieveprotein.info("Retrieve from KEGG database " + str(p - 1) + " highly conserved proteins")
    return dirname


def doretrieve(specieslistfile, outpath):
    '''main to  retrieve protein from kegg db'''
    # spelist = []
    # for line in specieslistfile:
    #     st = line.strip()
    #     spelist.append(st)
    spelist = specieslistfile
    logretrieveprotein.info("Read organisms names success")
    colname = getcolname()
    relist, matchlist = getspecies(spelist, colname)
    dirpath = retrieveprotein(relist, outpath, matchlist)
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
    print getcolname()
    print getspecies(['zma'], ['K02925'])
