# ('Ribosomal protein L1 ', 'K02865')
import urllib2
import re


def getorganismlist():
    page = urllib2.urlopen('http://rest.kegg.jp/list/organism')
    html = page.read()
    return html


def getkolist(ko):
    listko = []
    url = "http://rest.kegg.jp/link/genes/" + ko
    page = urllib2.urlopen(url)
    for line in page:
        html = line.strip().split('\t')
        listko.append(html)
        # return listko


# \nORGANISM    hsa  Homo sapiens (human)\nPATHWAY
# PDB: 3RNJ 4JS0 2YKT 1Y2O 1WDZ\nAASEQ       552\n            MSLSRS
# HGDGSARTLAGR\nNTSEQ
def parsegetpro(propage):
    spename, speseq = None, []
    apipage = propage.read()
    apipagelist = apipage.split("///")
    for line in apipagelist:
        regname = r"(?<=\nORGANISM).*?(?=\nPATHWAY)"
        regseq = r"(?<=\nAASEQ).*?(?=\nNTSEQ)"
        namecomp = re.compile(regname)
        seqcomp = re.compile(regseq)
        name = re.findall(namecomp, line)
        seq = re.findall(seqcomp, line)


def getprotein(proid):
    # http://rest.kegg.jp/get/hsa:10458+ece:Z5100+pon:100172290
    url = "http://rest.kegg.jp/get/" + proid + "/aaseq"
    page = urllib2.urlopen(url)
    return page
