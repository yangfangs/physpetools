import sys

from phylotree.domuscle import domuscle_file
from phylotree.dogblocks import dogblocks
from phylotree.doraxml import doraxml
from convert.fasta2phy import fasta2phy
from convert.concatenate import cocat_path
from physpetool.phylotree.log import getLogging, setlogdir
from physpetool.phylotree.retrieveprotein import doretrieve
import argparse

"""
the main module as enter point and contain a main() function to invoke other
script same as pipeline.
"""

APP_DESC = """
constructing phylogenetic trees now

"""


def version_info():
    VERSION_INFO = 'V0.0.8'
    MUSCLE_INFO = 'v3.8.31'
    GBLOCKS_INFO = '0.91b'
    RAXML_INFO = 'v8.2.3'
    AUTHOR_INFO = 'Author: Yang Fang'
    print 'physpe version: ', VERSION_INFO
    print AUTHOR_INFO
    print "call software INFO:"
    print 'muscle version: ', MUSCLE_INFO
    print 'RAxML version: ', RAXML_INFO
    print 'Gblocks version: ', GBLOCKS_INFO
parser = argparse.ArgumentParser(description=APP_DESC)

raxmlpara = "-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1"
musclepara = '-maxiters 100'
gblockspara = '-t=p -e=-gb1'
parser = argparse.ArgumentParser(description=APP_DESC)

parser.add_argument('-in', action='store', dest='fastafile',
                    help='input file must be contain the species names')
parser.add_argument('-out', action="store", dest="nwkfile",
                    help='out file name be String type')
parser.add_argument('-v', '--version', action='store_true',
                    default=False, help='Version information')
parser.add_argument('-t', action='store', dest='thread',
                    type=int, default=1, help='set the thread')
parser.add_argument('-muscle', action='store', dest='muscle',
                    default=musclepara, help='alignment by muscle')
parser.add_argument('-gblocks', action='store', dest='gblocks',
                    default=gblockspara, help='use gblock')
parser.add_argument('-raxml', action='store', dest='raxml',
                    default=raxmlpara, help='build by raxml')
args = parser.parse_args()
print parser.parse_args()
if args.version:
    version_info()
    sys.exit(0)

print "in put fasta file is:"
print args.fastafile
print "outfile is:"
print args.nwkfile + "\n"
print "now loading data and constructing species phylogenetic tree..."
print args.thread

# in_put = '/home/yangfang/physpetools/testdata/protein.fastq'
# out_put = '/home/yangfang/physpetools/testdata/phytree.nwk'
# physpe -in /home/yangfang/physpetools/testdata/speciesname.txt -out /home/yangfang/physpetools/testdata/phytree4

def main():
    in_put = args.fastafile
    out_put = args.nwkfile
    setlogdir(out_put)
    out_retrieve = doretrieve(in_put, out_put)
    out_alg = domuscle_file(out_retrieve, out_put, args.muscle)
    out_concat = cocat_path(out_alg)
    out_gblock = dogblocks(out_concat, args.gblocks)
    out_f2p = fasta2phy(out_gblock)
    doraxml(out_f2p, out_put, args.raxml, args.thread)


if __name__ == '__main__':
     main()
