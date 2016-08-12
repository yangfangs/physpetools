import argparse
import sys
import build
import builds

__version__ = 'v0.0.1'
__DESCRIPTION__ = 'test'

parser = argparse.ArgumentParser(description="reconstruct phylogenetic tree",
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
subparser = parser.add_subparsers(title="AVAILABLE PROGRAMS")
test = subparser.add_parser("build", help='tst')
test.set_defaults(func=build.run)
build.populate_args(test)

combine = subparser.add_parser("combine", help='to do combine')
combine.set_defaults(func=builds.run)
builds.populate_args(combine)

# argument =sys.argv
# args = parser.parse_args(argument[1:])
args = parser.parse_args()
args.func(args)

print parser.usage()