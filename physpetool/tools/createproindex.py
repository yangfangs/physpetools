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
Create highly conserved proteins database index database.

"""

import sqlite3

conn = sqlite3.connect('../database/koindex.db')
conn.text_factory = str
c = conn.cursor()
for row in c.execute('SELECT NAME,EUKARYOTES FROM KOINDEX'):
    print row

listko = []
with open('../database/protein_ko.txt') as ko:
    for line in ko:
        str = line.strip().split(',')
        listko.append(str[1])

text = ' TEXT, '.join(listko)


createlist = ["create table if not exists keggproindex", "(id integer primary key autoincrement, NAME TEXT, ", text, " TEXT)"]
createsql = ''.join(createlist)

proindex = sqlite3.connect('../database/proindex.db')
proindex.text_factory = str
cursor = proindex.cursor()
cursor.execute(createsql)

orgs = []
with open('../database/organism.txt') as org:
    for line in org:
        str = line.strip().split('\t')
        orgs.append((str[1],))

cursor.executemany("INSERT INTO keggproindex (NAME)\
    VALUES (?)", orgs)
proindex.commit()
cursor.close()


#cursor.execute('DROP TABLE keggproindex')


# check the name
# cursor.execute("select NAME from keggproindex")
# col_name_list = [tuple[0] for tuple in cursor.description]
# print col_name_list









