import argparse
import os

import sys

APP_DESC = """
constructing phylogenetic trees now

"""


def version_info():
    VERSION_INFO = 'V0.0.8'
    AUTHOR_INFO = 'Author: Yang Fang'
    print VERSION_INFO
    print AUTHOR_INFO


raxmlpara = "xxxxx"

parser = argparse.ArgumentParser(description=APP_DESC)

parser.add_argument('-in', nargs='?', dest='spenames', type=argparse.FileType('r'),
                    default=sys.stdin, help='input file must be contain the species names')
parser.add_argument('-out', action="store", dest="outdatafile",
                    default='Outdata', help='out file name be String type')
parser.add_argument('-v', '--version', action='store_true',
                    default=False, help='Version information')
parser.add_argument('-raxml', action='store', dest='raxml',
                    default=raxmlpara, help='build by raxml')
parser.add_argument('-t', action='store', dest='thread', type=int, default=1,
                    help='set the thread')
parser.add_argument('-muscle', action='store', dest='muscle',
                    help='alignment by muscle')
parser.add_argument('-gblocks', action='store', dest='gblocks',
                    help='use gblock')

args = parser.parse_args()
print parser.parse_args()
if args.version:
    version_info()
    sys.exit(0)

if args.raxml:
    print args.raxml
if args.raxml is raxmlpara:
    print 'defult ffff'

pwd = os.getcwd()

outpath = os.path.join(pwd, args.outdatafile)

print outpath
