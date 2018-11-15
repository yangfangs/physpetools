import argparse
import os

import sys

__version__ = 'v0.0.1'

__DESCRIPTION__ = (
    """
          --------------------------------------------------------------------------------
                      Physpe (%s) - reconstruct phylogenetic tree

          Citation: null


          --------------------------------------------------------------------------------
          """ % (__version__))

print (__DESCRIPTION__)


def version_info():
    VERSION_INFO = 'V0.0.8'
    AUTHOR_INFO = 'Author: Yang Fang'
    print (VERSION_INFO)
    print (AUTHOR_INFO)


raxmlpara = "xxxxx"

parser = argparse.ArgumentParser(description=__DESCRIPTION__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
input_group = parser.add_argument_group('==== Input Options ====')
output_group = parser.add_argument_group('==== Output Options ====')
subparsers = parser.add_subparsers(help='sub-command help')
input_group.add_argument('-in', nargs='?', dest='spenames', type=argparse.FileType('r'),
                         default=sys.stdin, help='input file must be contain the species names')
output_group.add_argument('-o', '--out', action="store", dest="outdatafile",
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
parser_a.add_argument('-in', nargs='?', action="store", dest='spenames',
                      default=sys.stdin, help='sub -in')

parser_b.add_argument('-out', action="store", dest="testbout",
                      help='sub -outdata')
parser_b.add_argument('-in', nargs='?', action="store", dest='testbin',
                      default=sys.stdin, help='sub -indata')

args = parser.parse_args()
print (parser.parse_args())
if args.version:
    version_info()
    sys.exit(0)

if args.testbout:
    print ('yes  have muscle parameter')

if args.raxml:
    print (args.raxml)
if args.raxml is raxmlpara:
    print ('defult ffff')

# test pwd
pwd = os.getcwd()
outpath = os.path.join(pwd, args.outdatafile)
print (outpath)
