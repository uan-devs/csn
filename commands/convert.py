from helpers.validation import is_valid_number, has_coma, is_coma_valid, is_base
from globals.numbers import BASE_VERBOSE, MAX_DECIMAL_ROMAN_NUMBER


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


def convert_dec_bin(number: str) -> str:
    try:
        convert_number = ''
        op_number = int(number)
        if has_coma(number):
            if not is_coma_valid(number):
                return ''

        while op_number >= 1:
            convert_number += str(op_number % 2)
            op_number //= 2
        return convert_number[::-1]
    except TypeError:
        return ''


def convert_dec_oct(number: str) -> str:
    try:
        convert_number = ''
        op_number = int(number)
        if has_coma(number):
            if not is_coma_valid(number):
                return ''

        while op_number >= 1:
            convert_number += str(op_number % 8)
            op_number //= 8
        return convert_number[::-1]
    except TypeError:
        return ''


def convert_dec_hex(number: str) -> str:
    try:
        convert_number = ''
        op_number = int(number)
        decimal_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        if has_coma(number):
            if not is_coma_valid(number):
                return ''

        while op_number >= 1:
            if op_number % 16 < 10:
                convert_number += str(op_number % 16)
            else:
                convert_number += decimal_letters[op_number % 16]
            op_number //= 16
        return convert_number[::-1]
    except TypeError:
        return ''


def convert_dec_rom(number: str) -> str:
    try:
        op_number = int(number)
        units = op_number % 10
        tens = (op_number % 100) // 10
        hundreds = (op_number % 1000) // 100
        thousands = op_number // 1000
        units_rom_numbers = {
            0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI',
            7: 'VII', 8: 'VIII', 9: 'IX'
        }
        tens_rom_numbers = {
            0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX',
            7: 'LXX', 8: 'LXXX', 9: 'XC'
        }
        hundreds_rom_numbers = {
            0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC',
            7: 'DCC', 8: 'DCCC', 9: 'CM'
        }
        thousands_rom_numbers = {
            0: '', 1: 'M', 2: 'MM', 3: 'MMM'
        }
        if has_coma(number):
            return ''

        return thousands_rom_numbers[thousands] + \
            hundreds_rom_numbers[hundreds] + tens_rom_numbers[tens] + \
            units_rom_numbers[units]
    except TypeError:
        return ''
    except KeyError:
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

    match base_from:
        case 'B':
            match base_to:
                case 'D':
                    return convert_bin_dec(number)
                case 'H':
                    return 'Hexadecimal'
                case 'O':
                    return 'Octal'
                case 'R':
                    if verbose and has_coma(number):
                        print('Unable to convert floating point number to roman base')
                    return 'Roman'
        case 'D':
            match base_to:
                case 'B':
                    return convert_dec_bin(number)
                case 'H':
                    return convert_dec_hex(number)
                case 'O':
                    return convert_dec_oct(number)
                case 'R':
                    if verbose:
                        if has_coma(number):
                            print(
                                'Unable to convert '
                                'floating point number to roman base'
                            )
                        try:
                            _ = int(number)
                            if _ > MAX_DECIMAL_ROMAN_NUMBER:
                                print('Max value to convert to roman base reached')
                        except TypeError:
                            print('%s does not exist in %s system' % (number, BASE_VERBOSE[base_from]))
                    return convert_dec_rom(number)

    return 'EMPTY'


def convert_handler(args):
    print(convert(args.number, args.base01, args.base02, verbose=args.verbose))