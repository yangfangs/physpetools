import os

from physpetool.database.dbpath import getlocaldbpath
from physpetool.phylotree.log import getLogging

dbpath = getlocaldbpath()
logchecking = getLogging('Checking organisms')


def checkKeggOrganism(input):
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
    for che in inputlist:
        originaList.remove(che)
        mislist = originaList
    if not mislist:
        for misabb in mislist:
            logchecking.info(misabb)
    logchecking.warning("There organisms can't match in KEGG database so removed and reconstruct phylogenetic tree")
    print mislist
    return inputlist


def checkSilvaOrganism(input):
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
            logchecking.info(misabb)
    logchecking.warning("There organisms can't match in SILVA database so removed and reconstruct phylogenetic tree")
    print mislist
    return inputlist


def removeEmptyStr(all):
    newList = []
    for var in all:
        if var:
            newList.append(var)
    return newList


