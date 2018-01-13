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
Create highly conserved proteins index databse.

"""

import sqlite3
from keggapi import getkolist
import time


def getdata(database, name):
    """
    get the data by db contain eukaryotes prokaryotes KO number
    :param database: the databath path
    :param name: database col name
    :return: the query data from database
    """
    conn = sqlite3.connect(database)
    sqlselect = "select {0} from KOINDEX".format(name)
    conn.text_factory = str
    c = conn.cursor()
    c.execute(sqlselect)
    konum = c.fetchall()
    c.close()
    return konum


def insertdata(konum, abbname, value):
    """
    Insert protein index to  database
    example: insertdata('K02865','hsa','has:2525525')
    :param konum: the protein KO number
    :param abbname: the species abbreviation by kegg
    :param value: protein id by keegg
    """
    conn = sqlite3.connect('../database/KEGG_DB_1.0.db')
    conn.text_factory = str
    c = conn.cursor()
    sqlupdate = "UPDATE proindex SET {0}=? WHERE NAME=?".format(konum)
    c.execute(sqlupdate, (value, abbname))
    conn.commit()
    c.close()


# c.execute("UPDATE keggproindex SET KO2865='testdata' WHERE NAME='hsa'")
# c.execute("select NAME from keggproindex")
# col_name_list = [tuple[0] for tuple in cursor.description]
# print col_name_list
# for row in c.execute('SELECT * FROM keggproindex'):
#     print row

def kolinkinsertprokar(konum):
    """get Kegg KO link about prokartotes"""
    kolist = getkolist(konum[1])
    for ko in kolist:
        value = ko[1]
        abb = value.split(':')[0]
        insertdata(konum[0], abb, value)


def kolinkinserteuk(konum):
    """get Kegg KO link about eukaryotes"""
    kolist = getkolist(konum)
    for ko in kolist:
        value = ko[1]
        abb = value.split(':')[0]
        insertdata(konum, abb, value)


def inserteuk():
    """insert eukaryotes data from kegg"""
    kodata = getdata('../database/koindex.db', 'EUKARYOTES,PROKARYOTES')
    for line in kodata:
        ko = line[0]
        print ko
        kolinkinserteuk(ko)


def insertprokar():
    """insert prokaryotes data form kegg"""
    kodata = getdata('../database/koindex.db', 'EUKARYOTES,PROKARYOTES')
    for line in kodata:
        print line[1]
        kolinkinsertprokar(line)


def countcol():
    """check the database the protein number index are already get
        and the none data
    """
    countlen = []
    countnone = []
    conn = sqlite3.connect('../database/proindex.db')
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute('SELECT * FROM keggproindex'):
        listrow = list(row)
        relistrow = [x for x in listrow if x is not None]
        lens = len(relistrow) - 2
        if lens is 0:
            countnone.append(row)
        countlen.append(lens)
    c.close()
    return countlen, countnone


def displaydb():
    """display de database the length, max, min, average et al. of species respectively"""
    countlen, countnone = countcol()
    print "Total organism in database:", len(countlen)
    print "Max of get protein number is:", max(countlen)
    print "Min of get protein number is:", min(countlen)
    print "Average of get protein number is:", sum(countlen) / len(countlen)
    print "Number of can't get any protein:", len(countnone)
    print "Nhe species are can't get any protein names is:"
    for abb in countnone:
        print abb[1] + ",",


def display_row(abb):
    conn = sqlite3.connect('../database/proindex.db')
    conn.text_factory = str
    c = conn.cursor()
    sqlupdate = "select * from keggproindex  where NAME='{0}'".format(abb)
    c.execute(sqlupdate)
    result = c.fetchall()
    print (result)
    conn.commit()
    c.close()


if __name__ == '__main__':
    # start = time.time()
    # displaydb()
    #
    # end = time.time()
    # during = end - start
    # print "\n"
    # print "the execute time is:"
    # print(during)

    insertdata(konum='K02925', abbname='zma', value='zma:101027258')
    display_row('zma')



# update id =151
# select * from keggproindex where id =151
# update keggproindex set K02925 = 'zma:101027258' where id =151
# commit
