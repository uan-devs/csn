from helpers.validation import is_valid_number, has_coma, is_coma_valid, is_base
from globals.numbers import BASE, BASE_VERBOSE


def convert_bin_dec(number: str) -> str:
    convert_number = 0
    if has_coma(number):
        if not is_coma_valid(number):
            return ''

    try:
        for i, j in enumerate(number[::-1]):
            if j != '0':
                convert_number += pow(2, i)
        return str(convert_number)
    except TypeError:
        return ''


def convert(number: str, base_from: str, base_to: str, verbose: bool = False) -> str:
    if len(number) == 0:
        return ''
    if not is_base(base_to):
        return ''
    if not is_valid_number(number, base_from, verbose=verbose):
        if verbose and is_base(base_from):
            print('%s does not exist in %s system' % (number, BASE_VERBOSE[base_from]))
        return ''

    if base_from == base_to:
        return number

    if base_from == BASE[0] and base_to == BASE[1]:
        return convert_bin_dec(number)

    return 'EMPTY'


def convert_handler(args):
    print(convert(args.number, args.base01, args.base02, verbose=args.verbose))
