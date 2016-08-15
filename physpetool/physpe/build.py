import os

APP_DESC = ""


def start_args(input):
    """
Arguments parse
    :param input:  Arguments
    """
    annotation_args = input.add_argument_group("EBUILD OPTIONS")
    annotation_args.add_argument('-i', action='store', dest="inputfile",
                                 help="Input organisms names file, which used reconstructed \
                              phylogenetic tree.")
    annotation_args.add_argument('-o', action='store', dest="outputfile",
                                 default='ebuildtree', help="It's a directory contain extend phylogenetic tree")
    annotation_args.add_argument('-e', action='store', dest="extendfile",
                                 help="a extend file for extend phylogenetic tree")
    annotation_args.add_argument('-m', action='store', dest="method",
                                 choices=['hcp', 'srna'],
                                 help="Choice the method to reconstruct phylogenetic treee.")


def starting(args):
    """
Staring run combine
    :param args: arguments
    """
    pwd = os.getcwd()

    out_put = os.path.join(pwd, args.outputfile)
