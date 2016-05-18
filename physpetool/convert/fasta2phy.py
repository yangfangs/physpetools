import os

from physpetool.phylotree.log import getLogging

"""
convert fasta format to PHYLIP(.phy) format

"""

logfasta2phy = getLogging('convert')
# function to read fasta file
def read_fasta(fp):
    """
    read *.fasta file and parse
    :param fp: a fasta format file
    """
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
    """
    convert fasta format file to PHYLIP format
    :param inputfile: *.fasta file
    :return: output data path
    """
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
            logfasta2phy.debug("sequence name is {0} sequence is {1}".format(seq_name, seq_pro))
            fw.write("%s %s\n" % (seq_name, seq_pro))
    logfasta2phy.info("Fasta format converted to PHYLIP format was completed")
    return fwfile