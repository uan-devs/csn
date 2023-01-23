"""
CSN
"""

import argparse
import sys

from globals.system import CURRENT_VERSION
from commands.convert import convert_handler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A command line utility to numbers', prog='csn')
    parser.add_argument('-v', '--version', help='Display the current version', action="store_true")
    subparsers = parser.add_subparsers(dest='command', help='command help')

    convert_parser = subparsers.add_parser(
        'convert',
        help='Convert a number from one base to another',
        description='Convert a number'
    )
    convert_parser.add_argument('-v', '--verbose', help='Use verbose output', action="store_true")
    convert_parser.add_argument('number', help='number')
    convert_parser.add_argument('base01', help='number base')
    convert_parser.add_argument('base02', help='base to convert to')
    convert_parser.set_defaults(func=convert_handler)

    args = parser.parse_args()

    if args.version:
        print("csn version %s" % CURRENT_VERSION)
    elif args.command is not None:
        args.func(args)
    else:
        parser.print_help(sys.stderr)
        exit(1)

    exit(0)
