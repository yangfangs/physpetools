import os
import sqlite3

from physpetool.phylotree.log import getLogging
from physpetool.tools.keggapi import getprotein

logretrieveprotein = getLogging('kegg DB')


def getspecies(name, colname):
    """
    Get species protein index for DB
    :param name: a list contain abbreviation species names
    :param colname: a list contain colname of DB
    :return: a list contain protein index can be retrieved
    """
    relist = []
    conn = sqlite3.connect('physpetool/database/proindex.db')
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
    conn = sqlite3.connect('physpetool/database/proindex.db')
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
    dirname = os.path.dirname(outpath)
    dirname = os.path.join(dirname, "temp/conserved_protein")
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
    logretrieveprotein.info("retrieve from Kegg DB " + str(p) + " highly conserved proteins")
    return dirname


def doretrieve(specieslistfile, outpath):
    spelist = []
    with open(specieslistfile, "r") as read:
        for line in read:
            st = line.strip()
            spelist.append(st)
    logretrieveprotein.info("read species successful")
    colname = getcolname()
    relist = getspecies(spelist, colname)
    dirpath = retrieveprotein(relist, outpath)
    return dirpath

def test():
    relpath = os.path.split(os.path.realpath(__file__))[0]
    print relpath


if __name__ == '__main__':
    # lst = ["hsa", "ptr", "pps", "ggo", "pon", "nle", "mcc", "mcf", "rro", "cjc"]
    # doretrieve(lst)
    relpath = os.path.split(os.path.realpath(__file__))[0]
    print relpath

