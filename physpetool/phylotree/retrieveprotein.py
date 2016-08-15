import os
import sqlite3
import time
from physpetool.database.dbpath import getlocaldbpath
from physpetool.phylotree.log import getLogging
from physpetool.tools.keggapi import getprotein

logretrieveprotein = getLogging('kegg DB')


def getspecies(name, colname):
    """
    Get species protein index for DB
    :param name: a list contain abbreviation species nam
    :param colname: a list contain colname of DB
    :return: a list contain protein index can be retrieved
    """
    dbpath = getlocaldbpath()
    db = os.path.join(dbpath, "proindex.db")
    relist = []
    conn = sqlite3.connect(db)
    conn.text_factory = str
    c = conn.cursor()
    connect = "' OR NAME = '".join(name)
    for ko in colname:

        query = "SELECT " + ko + " FROM keggproindex WHERE NAME = '" + connect + "'"
        c.execute(query)
        ids = list(c.fetchall())
        idslist = [str(x[0]) for x in ids]
        if 'None' not in idslist:
            relist.append(idslist)
        else:
            pass
    c.close()
    return relist


def getcolname():
    """get BD colnames"""
    dbpath = getlocaldbpath()
    db = os.path.join(dbpath, "proindex.db")
    relist = []
    conn = sqlite3.connect(db)
    conn.text_factory = str
    c = conn.cursor()
    c.execute("SELECT * FROM keggproindex")
    col_name_list = [tuple[0] for tuple in c.description]
    c.close()
    return col_name_list[2:]


def splist(l, s):
    """split a list to sub list contain s"""
    return [l[i:i + s] for i in range(len(l)) if i % s == 0]


def retrieveprotein(proindexlist, outpath):
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
        logretrieveprotein.info("retrieve " + "Conserved protein p" + str(p) + " success")
        p += 1
    logretrieveprotein.info("retrieve from Kegg DB " + str(p-1) + " highly conserved proteins")
    return dirname


def doretrieve(specieslistfile, outpath):
    '''main to  retrieve protein from kegg db'''
    # spelist = []
    # for line in specieslistfile:
    #     st = line.strip()
    #     spelist.append(st)
    spelist = specieslistfile
    logretrieveprotein.info("Read organisms names successful")
    colname = getcolname()
    relist = getspecies(spelist, colname)
    dirpath = retrieveprotein(relist, outpath)
    return dirpath

def hcp_name(index):
    ko_path = getlocaldbpath()
    pro_ko = os.path.join(ko_path, "protein_ko.txt")
    with open(pro_ko) as ko:
        for line in ko:
            name = line.strip().split(',')
            if name[1] == index:
                return name[0]