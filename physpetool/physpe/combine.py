import os

from physpetool.phylotree.consensustree import docontree

APP_DESC = ""


def start_agrs(input):
    """
Arguments parse
    :param input:  Arguments
    """
    combine_args = input.add_argument_group("COMBINE OPTIONS")
    combine_args.add_argument('-i', action='store', dest="inputfile",
                              help='input files name')
    combine_args.add_argument('-o', action='store', dest="outputfile",
                              default='combinetree', help='output files name')


def starting(args):
    """
Staring run combine
    :param args: arguments
    """
    pwd = os.getcwd()

    out_put = os.path.join(pwd, args.outputfile)
    docontree(args.inputfile, out_put)
