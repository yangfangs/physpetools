import argparse

import sys

__version__ = 'v0.0.1'
__DESCRIPTION__ ='test'

DESC = ""
def populate_args(annotate_args_p):
    autobuild_args = annotate_args_p.add_argument_group("TREE AUTOBUILD OPTIONS")
    autobuild_args.add_argument('-out', action="store", dest="outdatafile",
                          default='Outdata', help='sub -out')
    autobuild_args.add_argument('-in', nargs='?', action="store", dest='spenames',
                          default=sys.stdin, help='sub -in')

def run(args):
    lenth = len(args)
    print  lenth

    print ('hello')
