import os
import subprocess
import sys

from phylotree.domuscle import domuscle_file, domuscle
from phylotree.dogblocks import dogblocks
from phylotree.doraxml import doraxml
from convert.fasta2phy import fasta2phy
from convert.concatenate import cocat_path
from physpetool.phylotree.log import getLogging, setlogdir
from physpetool.phylotree.retrieve16srna import retrieve16srna
from physpetool.phylotree.retrieveprotein import doretrieve
import argparse

from physpetool.utils.checkinputfile import checkKeggOrganism, checkSilvaOrganism

"""
the main module as enter point and contain a main() function to invoke other
script same as pipeline.
"""

APP_DESC = """
        PHYSPE v0.1.2:
Reconstruct phylogenetic tree
"""


def version_info():
    version_info = 'V0.1.2'
    muscle_info = 'v3.8.31'
    gblocks_info = '0.91b'
    raxml_info = 'v8.2.3'
    author_info = 'Author: Yang Fang'
    print 'physpe version: ', version_info
    print author_info
    print "call software INFO:"
    print 'muscle version: ', muscle_info
    print 'RAxML version: ', raxml_info
    print 'Gblocks version: ', gblocks_info


parser = argparse.ArgumentParser(description=APP_DESC)

raxmlpara_pro = "-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1"
raxmlpara_dna = "-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1"
musclepara = '-maxiters 100'
gblockspara_pro = '-t=p -e=-gb1'
gblockspara_dna = '-t=d -e=-gb1'
parser = argparse.ArgumentParser(description=APP_DESC)
subparsers = parser.add_subparsers(help='more command')
parser.add_argument('-in', nargs='?', dest='spenames', type=argparse.FileType('r'),
                    help='Input file must be contain the species names')
parser.add_argument('-out', action="store", dest="outdata",
                    default='Outdata', help='Out file name be string type')
parser.add_argument('-t', action='store', dest='thread',
                    type=int, default=1, help='Set the thread')
parser.add_argument('-muscle', action='store', dest='muscle',
                    default=musclepara, help='Alignment by muscle')
parser.add_argument('-gblocks', action='store', dest='gblocks',
                    default=gblockspara_pro, help='Use gblock')
parser.add_argument('-raxml', action='store', dest='raxml',
                    default=raxmlpara_pro, help='Build by raxml')
parser.add_argument('-hcp', action='store_true', dest='HCP',
                    default=False, help='Reconstruct phylogenetic tree by highly conserved proteins')
parser.add_argument('-srna', action='store_true', dest='ssurna',
                    default=False, help='Reconstruct phylogenetic tree by 16s ran')
parser.add_argument('-v', '--version', action='store_true',
                    default=False, help='Version information')
parser_combine = subparsers.add_parser('combine', help='combine tree')


args = parser.parse_args()
if args.version:
    version_info()
    sys.exit(0)
if args.spenames is None:
    cmd = 'physpe -h'
    subprocess.call(cmd, shell=True)
    sys.exit(0)
print "in put fasta file is:"
print args.spenames
print "outfile is:"
print args.outdata + "\n"
print "now loading data and constructing species phylogenetic tree..."
print args.thread

# in_put = '/home/yangfang/physpetools/testdata/protein.fastq'
# out_put = '/home/yangfang/physpetools/testdata/phytree.nwk'
# physpe -in /home/yangfang/physpetools/testdata/speciesname.txt -out /home/yangfang/physpetools/testdata/phytree1
in_put = args.spenames

pwd = os.getcwd()

out_put = os.path.join(pwd, args.outdata)





def main():
    if args.HCP:
        setlogdir(out_put)

        hcp_input = checkKeggOrganism(in_put)
        out_retrieve = doretrieve(hcp_input, out_put)
        out_alg = domuscle_file(out_retrieve, out_put, args.muscle)
        out_concat = cocat_path(out_alg)
        out_gblock = dogblocks(out_concat, args.gblocks)
        out_f2p = fasta2phy(out_gblock)
        doraxml(out_f2p, out_put, args.raxml, args.thread)
    elif args.ssurna:
        setlogdir(out_put)

        ssu_input = checkSilvaOrganism(in_put)
        out_retrieve = retrieve16srna(ssu_input, out_put)
        out_alg = domuscle(out_retrieve, out_put, args.muscle)
        if args.gblocks is gblockspara_pro:
            args.gblocks = gblockspara_dna
            out_gblock = dogblocks(out_alg, args.gblocks)
        out_f2p = fasta2phy(out_gblock)
        if args.raxml is raxmlpara_pro:
            args.raxml = raxmlpara_dna
            doraxml(out_f2p, out_put, args.raxml, args.thread)


if __name__ == '__main__':
    main()
