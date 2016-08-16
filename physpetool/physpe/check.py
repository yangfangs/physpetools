import os

from physpetool.utils.checkdb import check_ehcp
from physpetool.view.annotatingtree import colorRange

APP_DESC = ""


def start_args(input):
    """
Arguments parse
    :param input:  Arguments
    """

    annotation_args = input.add_argument_group("CHECK OPTIONS")
    annotation_args.add_argument('-i', action='store', dest="inputfile",
                                 help="Input organisms names file, which used reconstructed \
                              phylogenetic tree.")
    annotation_args.add_argument('-o', action='store', dest="outputfile",
                                 default='check', help="It's a directory name contain check result.")

    annotation_args.add_argument('-r', '--ehcp', action='store_true', dest="checkehcp",
                                 default=False, help="Check organisms for extend highly conserved proteins.")


def starting(args):
    """
Staring run combine
    :param args: arguments
    """
    pwd = os.getcwd()

    out_put = os.path.join(pwd, args.outputfile)
    if args.checkehcp:
        check_ehcp(args.inputfile, out_put)
