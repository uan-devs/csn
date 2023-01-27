"""
CSN
"""

import argparse
import sys

from globals.system import CURRENT_VERSION
from commands.convert import convert_handler
from commands.sum import sum_handler

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

    sum_parser = subparsers.add_parser(
        'sum',
        help='Sum two or more numbers from all bases and put the results to a specified base',
        description='Sum two or more numbers'
    )
    sum_parser.add_argument('-v', '--verbose', help='Use verbose output', action="store_true")
    sum_parser.add_argument('-f', '--force', help='Force sum', action="store_true")
    sum_parser.add_argument('--bin', '--binary-numbers', nargs='*', help='Add binary numbers to sum')
    sum_parser.add_argument('--dec', '--decimal-numbers', nargs='*', help='Add decimal numbers to sum')
    sum_parser.add_argument('--hex', '--hexadecimal-numbers', nargs='*', help='Add hex numbers to sum')
    sum_parser.add_argument('--oct', '--octal-numbers', nargs='*', help='Add octal numbers to sum')
    sum_parser.add_argument('--rom', '--roman-numbers', nargs='*', help='Add roman numbers to sum')
    sum_parser.set_defaults(func=sum_handler)

    args = parser.parse_args()

    if args.version:
        print("csn version %s" % CURRENT_VERSION)
    elif args.command is not None:
        args.func(args)
    else:
        parser.print_help(sys.stderr)
        exit(1)

    exit(0)
