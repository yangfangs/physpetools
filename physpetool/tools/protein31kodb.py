# ########################## Copyrights and License ############################
#                                                                              #
# Copyright 2016 Yang Fang <yangfangscu@gmail.com>                             #
#                                                                              #
# This file is part of Physpe.                                                 #
# https://xiaofeiyangyang.github.io/physpetools/                               #
#                                                                              #
# Physpe is free software: you can redistribute it and/or modify it under      #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# Physpe is distributed in the hope that it will be useful, but WITHOUT ANY    #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with Physpe. If not, see <http://www.gnu.org/licenses/>.               #
#                                                                              #
# ##############################################################################

"""
The KEGG KO index database.

"""


import sqlite3
import os

print os.getcwd()
# name,eukaryotes,prokaryotes
listko = []

with open('../database/protein_ko.txt') as ko:
    i = 1
    for line in ko:
        str = line.strip().split(',')
        str.insert(0, i)
        i = i + 1
        listko.append(tuple(str))
print listko
conn = sqlite3.connect('../database/koindex.db')
conn.text_factory =str
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS KOINDEX
        (ID INT PRIMARY KEY NOT NULL,
        NAME          TEXT NOT NULL,
        EUKARYOTES     TEXT NOT NULL,
        PROKARYOTES    TEXT NOT NULL);''')
c.executemany("INSERT INTO KOINDEX (ID,NAME,EUKARYOTES,PROKARYOTES)\
              VALUES (?,?,?,?)", listko)
conn.commit()
c.close()
