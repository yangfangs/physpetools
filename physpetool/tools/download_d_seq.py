import os
from urllib import request
import time
def splist(l, s):
    """split a list to sub list contain s"""
    return [l[i:i + s] for i in range(len(l)) if i % s == 0]

def getprotein(proid):
    # http://rest.kegg.jp/get/hsa:10458+ece:Z5100+pon:100172290
    url = "http://rest.kegg.jp/get/" + proid + "/aaseq"

    page = request.urlopen(url,timeout=60)
    time.sleep(5)
    return page


d_seq = []

with open("/home/yangfang/PhySpeTree/revision/HCPDB/hcp_code.txt") as f:
    for line in f:
        d_seq.append(line.strip())

all_file_path = '/home/yangfang/PhySpeTree/revision/HCPDB/hcp_append/'
all_files = list(filter(lambda f: not f.startswith('.'), os.listdir(all_file_path)))

for line in all_files:
    name = line.split('.')[0]
    if ( name in d_seq):
        d_seq.remove(name)

spprolist = splist(d_seq, 10)

idx =1
all_ = len(spprolist)

for id in spprolist:
    print(idx / all_)
    res = {}
    get_abb = []
    id_abb = [">"+x.strip().split(" ")[0]for x in id]
    query = "+".join(id)
    protein = getprotein(query)
    protein = protein.readlines()
    protein = [x.decode('utf-8') for x in protein]
    for i in protein:
        if i.startswith(">"):

            abbname = i.strip().split(" ")[0]
            get_abb.append(abbname)

            print(abbname)
            res[abbname] = []
            # print(abbname)
        else:
            res[abbname].append(i)
    # if the abb protein code changed by KEGG DB
    if len(get_abb) != len(id_abb):
        loss_abb = [x for x in id_abb if x not in get_abb]
        for loss in loss_abb:
            res[loss] = "M\n"


    for k, v in res.items():
        w_file = all_file_path + k + ".fasta"
        w_path = open(w_file, "w")
        w_path.write(k+"\n" + "".join(v))
        w_path.close()
    idx +=1