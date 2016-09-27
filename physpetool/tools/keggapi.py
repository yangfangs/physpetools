# ########################## Copyrights and License #############################
#                                                                               #
# Copyright 2016 Yang Fang <yangfangscu@gmail.com>                              #
#                                                                               #
# This file is part of PhySpeTree.                                              #
# https://xiaofeiyangyang.github.io/physpetools/                                #
#                                                                               #
# PhySpeTree is free software: you can redistribute it and/or modify it under   #
# the terms of the GNU Lesser General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)     #
# any later version.                                                            #
#                                                                               #
# PhySpeTree is distributed in the hope that it will be useful, but WITHOUT ANY #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS     #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  #
# details.                                                                      #
#                                                                               #
# You should have received a copy of the GNU Lesser General Public License      #
# along with PhySpeTree. If not, see <http://www.gnu.org/licenses/>.            #
#                                                                               #
# ###############################################################################

"""
API for KEGG database.
"""

import urllib2
import re


# ('Ribosomal protein L1 ', 'K02865')
def getorganismlist():
    page = urllib2.urlopen('http://rest.kegg.jp/list/organism')
    html = page.read()
    return html


def getkolist(ko):
    """Get KO list"""
    listko = []
    url = "http://rest.kegg.jp/link/genes/" + ko
    page = urllib2.urlopen(url)
    for line in page:
        html = line.strip().split('\t')
        listko.append(html)
    return listko


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
