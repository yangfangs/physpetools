import argparse
# import sys
# sys.path.append("../")
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
# physpe -in /home/yangfang/physpetools/testdata/speciesname.txt -out /home/yangfang/physpetools/testdata/phytree4

def main():

    in_put = args.fastafile
    out_put = args.nwkfile
    setlogdir(out_put)
    out_retrieve = doretrieve(in_put, out_put)
    out_alg = domuscle_file(out_retrieve, out_put)
    out_concat = cocat_path(out_alg)
    out_gblock = dogblocks(out_concat, "gb1")
    out_f2p = fasta2phy(out_gblock)
    doraxml(out_f2p, out_put)

if __name__ == '__main__':
    main()
