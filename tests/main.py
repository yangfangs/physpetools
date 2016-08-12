import argparse
import sys

__version__ = 'v0.0.1'
__DESCRIPTION__ ='test'

def test_main(arguments):
    if arguments[1] == 'build':
        print ('build tree')
    elif arguments[1] == 'start':
        print ('start phy build')
    parser = argparse.ArgumentParser(description=__DESCRIPTION__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-v', '--version', action='store_true',
                        default=False, help='Version information')
    parser.add_argument('-t', action='store', dest='thread', type=int, default=1,
                        help='set the thread')
    parser.add_argument('-muscle', action='store', dest='muscle',
                        help='alignment by muscle')
    parser.add_argument('-gblocks', action='store', dest='gblocks',
                        help='use gblock')
    args = parser.parse_args(arguments)
    print parser.parse_args()
    if args.version:
        print __version__
        sys.exit(0)
def main():
    _main(sys.argv)


def _main(arguments):
    if len(arguments) > 1:
        subcommand = arguments[1]
        if subcommand == "version":
            print(__version__)
            return

        elif subcommand == "build":
            del arguments[1]
            status = test_main(arguments)
            sys.exit(status)
main()

