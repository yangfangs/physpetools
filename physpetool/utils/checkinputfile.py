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
Check input file is right.

"""

from physpetool.database.dbpath import getlocaldbpath
from physpetool.phylotree.log import getLogging
import os

dbpath = getlocaldbpath()
logchecking = getLogging('Checking organisms')


def check_organism(input, db_list):
    """
    check input organism
    :param input: a list contain species name
    :param db_list: a list file contain organism in corresponding database
    :return: inputlist: match in database mislist: can't match in database
    """
    originaList = []
    for line in input:
        st = line.strip()
        originaList.append(st)
    originaList = removeEmptyStr(originaList)
    inputlist = []
    mislist = []
    spelist = os.path.join(dbpath, db_list)
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
    return inputlist, mislist


def checkKeggOrganism(input):
    """
Check input organisms list with KEGG database
    :param input: a open file list
    :return: a list contain organisms can be use construct phy tree
    """
    inputlist, mislist = check_organism(input, "organism_kegg_to_tax.txt")
    if mislist:
        for misabb in mislist:
            logchecking.info("The species: {0} can't match in KEGG protein index database".format(misabb))
        logchecking.warning(
            "These species can't match in KEGG protein index database so removed and reconstruct phylogenetic tree.")
    return inputlist


def checkSilvaOrganism(input):
    """
Check input organisms list with SILVA database
    :param input: a open file list
    :return: a list contain organisms can be use construct phy tree
    """
    inputlist, mislist = check_organism(input, "kegg_to_silva_id.txt")
    if mislist:
        for misabb in mislist:
            logchecking.info("The organism: {0} can't match in SSU rRNA database".format(misabb))
        logchecking.warning(
            "These species can't match in SSU rRNA database so removing and reconstructing phylogenetic tree.")

    return inputlist


def removeEmptyStr(all):
    """
Remove empty string
    :param all: input a list
    :return: a new list
    """
    newList = []
    for var in all:
        if var:
            newList.append(var)
    return newList


def checkFile(filepath):
    """
check input files
    :param filepath: input files
    :return: input files
    """
    if os.path.isfile(filepath):
        return filepath
    else:
        print("Please input a exact file")
        exit(0)


def readIputFile(inputfile):
    """
    prepare and check input file list
    :param inputfile:
    :return: inputfile by check list
    """
    org_name = []
    with open(inputfile) as f:
        for name in f:
            each_name = name.strip()
            org_name.append(each_name)

    org_name_check = removeEmptyStr(org_name)
    return org_name_check
