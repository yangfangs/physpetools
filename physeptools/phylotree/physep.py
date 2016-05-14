import argparse
import sys
sys.path.append("../")
from domuscle import domuscle
from dogblocks import dogblocks
from doraxml import doraxml
from convert.fasta2phy import fasta2phy

"""
the main module as enter point and contain a main() function to invoke other
script same as pipeline.
"""

APP_DESC = """
constructing phylogenetic trees now

"""
import argparse

parser = argparse.ArgumentParser(description=APP_DESC)

parser.add_argument('-in', action='store', dest='fastafile',
                    help='input file must be fasta format')
parser.add_argument('-out', action="store", dest="nwkfile",
                    help='out file name be String type')

args = parser.parse_args()
print "in put fasta file is:"
print args.fastafile
print "outfile is:"
print args.nwkfile + "\n"
print "now loading data and constructing species phylogenetic tree..."


# in_put = '/home/yangfang/physpetools/testdata/protein.fastq'
# out_put = '/home/yangfang/physpetools/testdata/phytree.nwk'
# physep.py -in /home/yangfang/physpetools/testdata/protein.fastq -out /home/yangfang/physpetools/testdata/phytree

def main():
    in_put = args.fastafile
    out_put = args.nwkfile
    out_alg = domuscle(in_put, out_put)
    print "alignment done"
    out_gblock = dogblocks(out_alg, "gb1")
    print "Gblocks done"
    out_f2p = fasta2phy(out_gblock)
    print "convert fasta to PHYLIP format done"
    doraxml(out_f2p, out_put)
    print "construct phy tree by RAxML done"
if __name__ == '__main__':
    main()
