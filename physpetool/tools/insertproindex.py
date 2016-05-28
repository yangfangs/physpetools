import sqlite3
from keggapi import getkolist
import time

def getdata(database, name):
    conn = sqlite3.connect(database)
    sqlselect = "select {0} from KOINDEX".format(name)
    conn.text_factory = str
    c = conn.cursor()
    c.execute(sqlselect)
    konum = c.fetchall()
    c.close()
    return konum


# insertdata('K02865','hsa','has:2525525')
def insertdata(konum, abbname, value):
    conn = sqlite3.connect('../database/proindex.db')
    conn.text_factory = str
    c = conn.cursor()
    sqlupdate = "UPDATE keggproindex SET {0}=? WHERE NAME=?".format(konum)
    c.execute(sqlupdate, (value, abbname))
    conn.commit()
    c.close()
#c.execute("UPDATE keggproindex SET KO2865='testdata' WHERE NAME='hsa'")
# c.execute("select NAME from keggproindex")
# col_name_list = [tuple[0] for tuple in cursor.description]
# print col_name_list
# for row in c.execute('SELECT * FROM keggproindex'):
#     print row

def kolinkinstert(konum):
    kolist = getkolist(konum[1])
    for ko in kolist:
        value = ko[1]
        abb = value.split(':')[0]
        insertdata(konum[0], abb, value)


if __name__ == '__main__':
    start = time.time()
    kodata = getdata('../database/koindex.db', 'EUKARYOTES,PROKARYOTES')
    # for line in kodata:
    #     ko = line[0]
    #     print ko
    #     kolinkinstert(ko)
    for line in kodata:
        print line[1]
        kolinkinstert(line)
    end = time.time()
    during = end - start
    print(during)