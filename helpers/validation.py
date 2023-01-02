from string import ascii_letters
from globals.numbers import BINARY, OCTAL, DECIMAL, ROMAN, HEX, BASE

# __all__ = ['isv']


def is_base(base: str) -> bool:
    return base in BASE


def is_binary(number: str) -> bool:
    if has_coma(number) and not is_coma_valid(number):
        return False

    count_bin = 0
    for i in number:
        if i in BINARY:
            count_bin += 1

    return count_bin == len(number)


def is_octal(number: str) -> bool:
    if has_coma(number) and not is_coma_valid(number):
        return False

    count_octal = 0
    for i in number:
        if i in OCTAL:
            count_octal += 1

    return count_octal == len(number)


def is_decimal(number: str) -> bool:
    if has_coma(number) and not is_coma_valid(number):
        return False

    count_decimal = 0
    for i in number:
        if i in DECIMAL:
            count_decimal += 1

    return count_decimal == len(number)


def is_roman(number: str) -> bool:
    if has_coma(number) and not is_coma_valid(number):
        return False

    count_roman = 0
    for i in number:
        if i in ROMAN:
            count_roman += 1

    return count_roman == len(number)


def is_hexadecimal(number: str) -> bool:
    if has_coma(number) and not is_coma_valid(number):
        return False

    count_hex = 0
    for i in number:
        if i in HEX:
            count_hex += 1

    return count_hex == len(number)


def is_valid_number(number: str, base: str, verbose: bool = False) -> bool:
    if not is_base(base):
        print('\'%s\': unknown base' % base)
        return False
    if (
        number.count(' ') != 0 or number.count('\n') != 0 or
        number.count('\t') != 0
    ):
        if verbose:
            print('Whitespaces are not valid in numbers and bases')
        return False

    return (
        (base == BASE[0] and is_binary(number)) or
        (base == BASE[1] and is_decimal(number)) or
        (base == BASE[2] and is_hexadecimal(number)) or
        (base == BASE[3] and is_octal(number)) or
        (base == BASE[4] and is_roman(number))
    )


def is_coma_valid(number: str) -> bool:
    return number.count('.') == 1


def has_coma(number: str) -> bool:
    return number.count('.') > 0


def is_letter(value: str) -> bool:
    """
    Check if value has letter
    """
    for i in value:
        if i in ascii_letters[26:32]:
            return True
    return False


def is_float(x) -> bool:
    try:
        float(x)
        return True
    except TypeError:
        return False
