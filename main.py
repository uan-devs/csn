"""
CSN
"""

import argparse
import sys

from globals.system import CURRENT_VERSION
from commands.convert import convert_handler
from commands.test import test_handler
from commands.info import info_handler
from commands.show import show_handler
from commands.file import file_handler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A command line utility to numbers', prog='csn')
    parser.add_argument('-v', '--version', help='Display the current version', action="store_true")
    subparsers = parser.add_subparsers(dest='command', help='command help')

    info_parser = subparsers.add_parser('info', help='Display info about the project')
    info_parser.set_defaults(func=info_handler)

    show_parser = subparsers.add_parser('show', help='Show a number in words')
    show_parser.set_defaults(func=show_handler)

    file_parser = subparsers.add_parser('load', help='Load a file and convert all numbers')
    file_parser.add_argument('filename', help='file name')
    file_parser.set_defaults(func=file_handler)

    test_parser = subparsers.add_parser(
        'test',
        help='Tests if a number or base or both are valid',
        description='Test number and/or base'
    )
    test_parser.add_argument('base', help='base')
    test_parser.add_argument('number', help='number')
    test_parser.set_defaults(func=test_handler)

    convert_parser = subparsers.add_parser(
        'convert',
        help='Convert a number from one base to another',
        description='Convert a number'
    )
    convert_parser.add_argument('number', help='number')
    convert_parser.add_argument('from', help='number base')
    convert_parser.add_argument('to', help='convert to')
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
