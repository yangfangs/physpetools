# ('Ribosomal protein L1 ', 'K02865')
import urllib2


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
    return listko
