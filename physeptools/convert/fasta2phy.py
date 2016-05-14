import os

"""
convert fasta format to PHYLIP(.phy) format

"""


# function to read fasta file
def read_fasta(fp):
    seq_name, seq_pro = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if seq_name: yield (seq_name, ''.join(seq_pro))
            seq_name, seq_pro = line.replace(">", ""), []
        else:
            seq_pro.append(line.replace(" ", ""))
    if seq_name: yield (seq_name, ''.join(seq_pro))


def fasta2phy(inputfile):
    fwfile = inputfile + '.phy'
    fw = open(fwfile, 'w')
    fr = open(inputfile)
    count = 0
    with fr as fp:
        for str in fp.readlines():
            if str.startswith(">"):
                count += 1
        fp.seek(0, 0)
        for seq_name, seq_pro in read_fasta(fp):
            seq_len = len(seq_pro)
        fw.write("%d %d\n" % (count, seq_len))
        fp.seek(0, 0)
        for seq_name, seq_pro in read_fasta(fp):
            print seq_name, seq_pro
            fw.write("%s %s\n" % (seq_name, seq_pro))
    return fwfile