import os

from physpetool.database.dbpath import getlocaldbpath
from physpetool.phylotree.log import getLogging

dbpath = getlocaldbpath()
logchecking = getLogging('Checking organisms')


def checkKeggOrganism(input):
    """
Check input organisms list with KEGG database
    :param input: a open file list
    :return: a list contain organisms can be use construct phy tree
    """
    originaList = []
    for line in input:
        st = line.strip()
        originaList.append(st)
    originaList = removeEmptyStr(originaList)
    inputlist = []
    mislist = []
    spelist = os.path.join(dbpath, "organism_kegg_to_tax.txt")
    for line in originaList:
        abb = line.strip()
        for spename in open(spelist):
            spe_name_list = spename.strip().split('\t')
            spe_name = spe_name_list[0]
            if spe_name == abb:
                inputlist.append(abb)
                break
            else:
                pass
    # Get can't match list
    for che in inputlist:
        originaList.remove(che)
        mislist = originaList
    if not mislist:
        for misabb in mislist:
            logchecking.info("The organism: {0}".format(misabb))
    logchecking.warning("There organisms can't match in KEGG database so removed and reconstruct phylogenetic tree")
    return inputlist


def checkSilvaOrganism(input):
    """
Check input organisms list with SILVA database
    :param input: a open file list
    :return: a list contain organisms can be use construct phy tree
    """
    originaList = []
    for line in input:
        st = line.strip()
        originaList.append(st)
    originaList = removeEmptyStr(originaList)
    inputlist = []
    mislist = []
    spelist = os.path.join(dbpath, "kegg_to_silva_id.txt")
    for line in originaList:
        abb = line.strip()
        for spename in open(spelist):
            spe_name_list = spename.strip().split('\t')
            spe_name = spe_name_list[0]
            if spe_name == abb:
                inputlist.append(abb)
                break
            else:
                pass
    for che in inputlist:
        originaList.remove(che)
        mislist = originaList
    if not mislist:
        for misabb in mislist:
            logchecking.info("The organism: {0}".format(misabb))
    logchecking.warning("There organisms can't match in SILVA database so removed and reconstruct phylogenetic tree")

    return inputlist


def removeEmptyStr(all):
    newList = []
    for var in all:
        if var:
            newList.append(var)
    return newList


def checkFile(filepath):
    if os.path.isfile(filepath):
        return filepath
    else:
        print("Please input a exact file")
        exit(0)
