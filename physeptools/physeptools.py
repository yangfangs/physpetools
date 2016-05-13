import argparse
import sys

"""
the main module as enter point and contain a main() function to invoke other
script same as pipeline.
"""

APP_DESC = """
 constructing phylogenetic trees now
"""

if len(sys.argv) == 1:
    sys.argv.append('--help')
parser = argparse.ArgumentParser()
parser.add_argument('-q', '--quality', type=int, default=0,
                    help="quality")
parser.add_argument('-v', '--verbose', default=0, help="print more debuging information")
parser.add_argument('-s', '--store', help="the srotre")
parser.add_argument('-c', '--config', default=0, help="construct")
parser.add_argument('url', metavar='URL', nargs='+', help="www.xiaofeiyangyang.github.io")


# main function as
def main():
    args = parser.parse_args()
    url = args.url[0]
    print(url)
