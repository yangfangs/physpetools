import os

from physpetool.phylotree.consensustree import docontree

APP_DESC = ""


def start_agrs(input):
    combine_args = input.add_argument_group("TREE combine OPTIONS")
    combine_args.add_argument('-in', action='store', dest="inputfile",
                              help='input files name')
    combine_args.add_argument('-out', action='store', dest="outputfile",
                              default='combinetree', help='output files name')


def starting(args):
    pwd = os.getcwd()

    out_put = os.path.join(pwd, args.outputfile)
    docontree(args.inputfile, out_put)
