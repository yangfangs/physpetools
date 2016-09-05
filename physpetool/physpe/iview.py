import os

from physpetool.view.annotatingtree import colorRange
from physpetool.view.changelabels import annotatingLabels

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

    annotation_args.add_argument('-r', '--range', action='store_true', dest="colorrange", default=False,
                                 help="Colored ranges by %s, you can choice one. The default is phylum." % (taxon))

    annotation_args.add_argument('-a', action='store', dest="assign", choices=taxonomy, default='phylum',
                                 help="Colored ranges by user, choice form [%s]." % (taxon))

    annotation_args.add_argument('-l', '--labels', action='store_true', dest="labels", default=False,
                                 help="Change labels from abbreviation names to full names.")


def starting(args):
    """
Staring run combine
    :param args: arguments
    """
    pwd = os.getcwd()
    out_put = os.path.join(pwd, args.outputfile)
    if args.colorrange:
        colorRange(args.inputfile, out_put, args.assign)
    elif args.labels:
        annotatingLabels(args.outputfile, args.outputfile)
