from helpers.validation import is_valid_number, has_coma, is_coma_valid, is_base
from globals.numbers import BASE_VERBOSE, MAX_DECIMAL_ROMAN_NUMBER, MAX_MANTISSA


def convert_bin_dec(number: str) -> str:
    convert_number = 0
    if has_coma(number):
        if is_coma_valid(number):
            part_int, part_float = number.split('.')
            convert_number += int(convert_bin_dec(part_int))
            try:
                for i, j in enumerate(part_float):
                    if j != '0':
                        convert_number += pow(2, -(i+1))
                return str(convert_number)
            except TypeError:
                return ''
        return ''

    try:
        for i, j in enumerate(number[::-1]):
            if j != '0':
                convert_number += pow(2, i)
        return str(convert_number)
    except TypeError:
        return ''


def convert_oct_dec(number: str) -> str:
    convert_number = 0
    if has_coma(number):
        if is_coma_valid(number):
            part_int, part_float = number.split('.')
            convert_number += int(convert_oct_dec(part_int))
            try:
                for i, j in enumerate(part_float):
                    if j != '0':
                        convert_number += int(j) * pow(8, -(i + 1))
                return str(convert_number)
            except TypeError:
                return ''
        return ''

    try:
        for i, j in enumerate(number[::-1]):
            if j != '0':
                convert_number += int(j) * pow(8, i)
        return str(convert_number)
    except TypeError:
        return ''


def convert_hex_dec(number: str) -> str:
    convert_number = 0
    hex_letters_values = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    if has_coma(number):
        if is_coma_valid(number):
            part_int, part_float = number.split('.')
            convert_number += int(convert_hex_dec(part_int))
            try:
                for i, j in enumerate(part_float):
                    if j.isnumeric():
                        convert_number += int(j) * pow(16, -(i+1))
                    else:
                        convert_number += hex_letters_values[j] * pow(16, -(i+1))
                return str(convert_number)
            except TypeError:
                return ''
        return ''

    try:
        for i, j in enumerate(number[::-1]):
            if j != '0':
                if j.isnumeric():
                    convert_number += int(j) * pow(16, i)
                else:
                    convert_number += hex_letters_values[j] * pow(16, i)
        return str(convert_number)
    except TypeError:
        return ''


def convert_rom_dec(number: str) -> str:
    convert_number = 0
    rom_base_numbers = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    try:
        i = 0
        while i < len(number):
            # Get the value of current symbol
            n1 = rom_base_numbers[number[i]]

            if (i + 1) < len(number):
                # Get the value of next symbol
                n2 = rom_base_numbers[number[i+1]]
                if n1 >= n2:
                    convert_number += n1
                    i += 1
                else:
                    convert_number += n2 - n1
                    i += 2
            else:
                convert_number += n1
                i += 1

        return str(convert_number) \
            if number == convert_dec_rom(str(convert_number)) \
            else ''

    except KeyError:
        return ''


def convert_dec_bin(number: str, mantissa: int = 7) -> str:
    convert_number = ''
    if has_coma(number):
        if is_coma_valid(number):
            part_int, part_float = number.split('.')
            convert_number += convert_dec_bin(part_int) + '.'

            try:
                ctrl = float('.' + part_float)
                for i in range(mantissa):
                    ctrl *= 2
                    if ctrl > 1:
                        convert_number += str(ctrl)[0]
                        ctrl -= 1
                    else:
                        convert_number += str(ctrl)[0]
                    if ctrl == int(ctrl):
                        print(ctrl)
                        break
            except ValueError:
                return ''

            return convert_number
        return ''
    try:
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


def convert_dec_oct(number: str, mantissa: int = 7) -> str:
    convert_number = ''
    if has_coma(number):
        if is_coma_valid(number):
            part_int, part_float = number.split('.')
            convert_number += convert_dec_oct(part_int) + '.'

            try:
                ctrl = float('.' + part_float)
                for i in range(mantissa):
                    ctrl *= 8
                    if ctrl > 7:
                        convert_number += str(ctrl)[0]
                        ctrl -= 7
                    else:
                        convert_number += str(ctrl)[0]
                    if ctrl == int(ctrl):
                        break
            except ValueError:
                return ''

            return convert_number
        return ''
    try:
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


def convert_dec_hex(number: str, mantissa: int = 7) -> str:
    convert_number = ''
    decimal_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if has_coma(number):
        if is_coma_valid(number):
            part_int, part_float = number.split('.')
            convert_number += convert_dec_hex(part_int) + '.'

            try:
                ctrl = float('.' + part_float)
                for i in range(mantissa):
                    ctrl *= 16
                    if ctrl > 15:
                        convert_number += decimal_letters[int(ctrl)]
                        ctrl -= 15
                    elif ctrl >= 10:
                        convert_number += decimal_letters[int(ctrl)]
                        ctrl -= int(ctrl)
                    else:
                        convert_number += str(ctrl)[0]
                        ctrl -= int(ctrl)
                    if ctrl == int(ctrl):
                        break
            except ValueError:
                return ''

            return convert_number
        return ''
    try:
        op_number = int(number)
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


def convert(number: str, base_from: str, base_to: str, mantissa: int = 7, verbose: bool = False) -> str:
    if len(number) == 0:
        return ''
    if not is_base(base_to):
        if verbose:
            print('\'%s\': unknown base' % base_to)
        return ''
    if not is_valid_number(number, base_from, verbose=verbose):
        if verbose and is_base(base_from):
            print('%s does not exist in %s system' % (number, BASE_VERBOSE[base_from]))
        return ''

    if mantissa <= 0 or mantissa > MAX_MANTISSA:
        mantissa = 7
        if verbose:
            print('Mantissa out of bounds, changing to 7')

    if has_coma(number) and base_to == 'R':
        if verbose:
            print('Roman numbers are not float')
        return ''

    if base_from == base_to:
        return number

    match base_from:
        case 'B':
            match base_to:
                case 'D':
                    return convert_bin_dec(number)
                case 'H':
                    return convert_dec_hex(convert_bin_dec(number))
                case 'O':
                    return convert_dec_oct(convert_bin_dec(number))
                case 'R':
                    _ = int(convert_bin_dec(number))
                    if _ > MAX_DECIMAL_ROMAN_NUMBER:
                        if verbose:
                            print('Max value to convert to roman base reached')
                        return ''
                    return convert_dec_rom(str(_))
        case 'D':
            match base_to:
                case 'B':
                    return convert_dec_bin(number, mantissa)
                case 'H':
                    return convert_dec_hex(number, mantissa)
                case 'O':
                    return convert_dec_oct(number, mantissa)
                case 'R':
                    _ = int(number)
                    if _ > MAX_DECIMAL_ROMAN_NUMBER:
                        if verbose:
                            print('Max value to convert to roman base reached')
                        return ''
                    return convert_dec_rom(number)
        case 'O':
            match base_to:
                case 'D':
                    return convert_oct_dec(number)
                case 'H':
                    return convert_dec_hex(convert_oct_dec(number))
                case 'B':
                    return convert_dec_bin(convert_oct_dec(number))
                case 'R':
                    _ = int(convert_oct_dec(number))
                    if _ > MAX_DECIMAL_ROMAN_NUMBER:
                        if verbose:
                            print('Max value to convert to roman base reached')
                        return ''
                    return convert_dec_rom(str(_))
        case 'H':
            match base_to:
                case 'D':
                    return convert_hex_dec(number)
                case 'O':
                    return convert_dec_oct(convert_hex_dec(number))
                case 'B':
                    return convert_dec_bin(convert_hex_dec(number))
                case 'R':
                    _ = int(convert_hex_dec(number))
                    if _ > MAX_DECIMAL_ROMAN_NUMBER:
                        if verbose:
                            print('Max value to convert to roman base reached')
                        return ''
                    return convert_dec_rom(str(_))
        case 'R':
            match base_to:
                case 'D':
                    return convert_rom_dec(number)
                case 'O':
                    return convert_dec_oct(convert_rom_dec(number))
                case 'B':
                    return convert_dec_bin(convert_rom_dec(number))
                case 'H':
                    return convert_dec_hex(convert_rom_dec(number))

    return 'EMPTY'


def convert_handler(args):
    print(convert(args.number, args.base01, args.base02, verbose=args.verbose, mantissa=args.mantissa or 7))
