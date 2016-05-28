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
