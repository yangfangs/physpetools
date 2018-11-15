import argparse
__version__ = 'v0.0.1'
__DESCRIPTION__ ='test'

DESC = ""
def populate_args(annotate_args_p):
    annotate_args_p.add_argument("-n", dest="ncbi", action="store_true",
                               help="annotate tree nodes using ncbi taxonomy database.")
    annotate_args_p.add_argument("-t", dest="taxid_attr", default='name',
                               help="attribute used as NCBI taxid number")
    annotate_args_p.add_argument("--feature", dest="feature", nargs="+", action='append', default=[],
                               help="")
def run(args):
    print (args.ncbi)






