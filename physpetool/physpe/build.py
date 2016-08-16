import os

from physpetool.phylotree.buildtree import build_hcp, build_srna
from physpetool.phylotree.log import setlogdir

APP_DESC = ""

raxmlpara_pro = "-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1"
raxmlpara_dna = "-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1"
musclepara = '-maxiters 100'
gblockspara_pro = '-t=p -e=-gb1'
gblockspara_dna = '-t=d -e=-gb1'


def start_args(input):
    """
Arguments parse
    :param input:  Arguments
    """
    build_args = input.add_argument_group("BUILD OPTIONS")
    advance_args = input.add_argument_group("ADVANCE OPTIONS")
    build_args.add_argument('-i', action='sotre', dest='input',
                                help="Input file FASTA format for '--sran' method or a directory contain conserved\
                                proteins")
    build_args.add_argument('-o', action='store', dest="outdata",
                                default='Outdata', help='Out file name be string type.')
    build_args.add_argument('-t', action='store', dest='thread',
                                type=int, default=1, help='Set the thread')
    build_args.add_argument('--hcp', action='store_true', dest='HCP',
                                default=False, help='Reconstruct phylogenetic tree by highly conserved proteins.')
    build_args.add_argument('--srna', action='store_true', dest='ssurna',
                                default=False, help='Reconstruct phylogenetic tree by 16s ssu ran.')
    advance_args.add_argument('--muscle', action='store', dest='muscle',
                              default=musclepara, help='Alignment by muscle.')
    advance_args.add_argument('--gblocks', action='store', dest='gblocks',
                              default=gblockspara_pro, help='Use gblock.')
    advance_args.add_argument('--raxml', action='store', dest='raxml',
                              default=raxmlpara_pro, help='Build by raxml.')

def starting(args):
    """
Staring run build
    :param args: arguments
    """

    pwd = os.getcwd()

    out_put = os.path.join(pwd, args.outdata)
    if args.extenddata:
        if os.path.isfile(args.extenddata):
            args_input = args.input
        elif os.path.isdir(args.extenddata):
            args_input = os.path.join(pwd, args.input)

    if args.HCP:
        setlogdir(out_put)
        build_hcp(args_input, out_put, args.muscle, args.gblocks, args.raxml, args.thread)
    # reconstruct phylogenetic tree by ssu RNA
    elif args.ssurna:
        setlogdir(out_put)
        build_srna(args_input, out_put, args.muscle, args.gblocks, args.raxml, args.thread)