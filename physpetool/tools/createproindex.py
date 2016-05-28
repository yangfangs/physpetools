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









