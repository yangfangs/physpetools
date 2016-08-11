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
subparsers = parser.add_subparsers(help='sub-command help')
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
parser_a = subparsers.add_parser('combine', help='a help')
parser_b = subparsers.add_parser('build', help='build tree')
parser_a.add_argument('-out', action="store", dest="outdatafile",
                    default='Outdata', help='sub -out')
parser_a.add_argument('-in', nargs='?', action="store",dest='spenames',
                    default=sys.stdin, help='sub -in')

parser_b.add_argument('-out', action="store", dest="testbout",
                    default='Outdata', help='sub -outdata')
parser_b.add_argument('-in', nargs='?', action="store",dest='testbin',
                    default=sys.stdin, help='sub -indata')

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

if