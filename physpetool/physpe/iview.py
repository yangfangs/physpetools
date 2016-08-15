import os

from physpetool.view.annotatingtree import colorRange

APP_DESC = ""


def start_args(input):
    """
Arguments parse
    :param input:  Arguments
    """
    taxonomy = ['kingdom', 'phylum', 'class', 'order']
    taxon = ', '.join(taxonomy)
    annotation_args = input.add_argument_group("ANNOTATION OPTIONS")
    annotation_args.add_argument('-i', action='store', dest="inputfile",
                                 help="Input organisms names file, which used reconstructed \
                              phylogenetic tree.")
    annotation_args.add_argument('-o', action='store', dest="outputfile",
                                 default='iview', help="It's a directory name contain iview convert files to \
                               view tree by use iTol v3 web applications. default output directory is iview.")
    annotation_args.add_argument('-r', '--range', action='store', dest="colorrange",
                                 choices=taxonomy, default='phylum',
                                 help="Colored ranges by %s, choice you should choice one." % (taxon))


def starting(args):
    """
Staring run combine
    :param args: arguments
    """
    pwd = os.getcwd()

    out_put = os.path.join(pwd, args.outputfile)
    colorRange(args.inputfile, out_put, args.colorrange)
