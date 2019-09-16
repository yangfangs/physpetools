import sqlite3
import os
from Bio import SeqIO

db ="/home/yangfang/PhySpeTree/physpetools/physpetool/database/KEGG_DB_3.0.db"
conn = sqlite3.connect(db)
conn.text_factory = str
c = conn.cursor()
c.execute("select * from proindex")
x = c.fetchall()


def read_seq(seq_path):
    seq_db = {}

    reads = SeqIO.parse(seq_path, 'fasta')
    for read in reads:
        seq = str(read.seq)
        seq_name = str(read.name)
        tem = seq_name.strip().split("|")
        if len(tem) > 1:
            seq_name = tem[1]
        seq_db[seq_name] = seq
    return seq_db


total = []
not_have = []

HCP_db = "/home/yangfang/PhySpeTree/revision/HCPDB/hcpdb/"
db_path = "/home/yangfang/PhySpeTree/revision/HCPDB/abb_seqs1000/"
all_ = len(x)
idx =1
for line in x:
    tem = [var for var in line if var != None]
    spe_name = tem[1]
    seq_name = tem[2:]
    read_path = db_path + spe_name + ".fasta"
    if os.path.isfile(read_path):
        seqs = read_seq(read_path)
        for each in seq_name:
            if each in seqs.keys():
                w_path = HCP_db + each + ".fasta"
                # print(w_path)
                f_w = open(w_path,'w')
                f_w.write(">" + each +"\n" + seqs[each])
                f_w.close()
            else:
                not_have.append(each)
    else:
        not_have.extend(seq_name)
    idx +=1
    print(idx/all_)


with open("/home/yangfang/PhySpeTree/revision/HCPDB/hcp_code.txt",'w') as f:
    for each in not_have:
        f.write(each +"\n")


