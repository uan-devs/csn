from helpers.validation import is_valid_number, has_coma, is_base, is_letter
from commands.convert import convert_rom_dec
from globals.numbers import BASE_VERBOSE


def extenso(x):
    try:
        x = int(x)
    except TypeError:
        return None

    if x == 0:
        return "Zero"

    else:
        num: str = ""
        units = ["Um", "Dois", "Três", "Quatro", "Cinco", "Seis",
                    "Sete", "Oito", "Nove"]
        dozens = ["Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze",
                   "Dezasseis", "Dezassete", "Dezoito", "Dezanove"]
        dozens2 = ["Vinte ", "Trinta ", "Quarenta ", "Cinquenta ",
                    "Sessenta ", "Setenta ", "Oitenta ", "Noventa "]
        hundreds = ["Cento e ", "Duzentos ", "Trezentos ", "Quatrocentos ",
                    "Quinhentos ", "Seiscentos ",
                    "Setecentos ", "Oitocentos ", "Novecentos "]

        uni, dez, cent, mil = x % 10, x % 100 // 10, x % pow(10, 3) // 100, \
                              x % pow(10, 4) // pow(10, 3)
        dmil, cmil, milho = x % pow(10, 5) // pow(10, 4), \
                            x % pow(10, 6) // pow(10, 5), \
                            x % pow(10, 7) // pow(10, 6)
        dmilho, cmilho, bil = x % pow(10, 8) // pow(10, 7), \
                              x % pow(10, 9) // pow(10, 8), \
                              x % pow(10, 10) // pow(10, 9)
        sum_udc, sum_mdc = uni + dez + cent, mil + dmil + cmil

        if 1 <= bil <= 9:
            if bil == 1:
                num += "Um Bilhão "
            elif bil >= 2:
                num += units[bil-1] + " Bilhões "

            if (sum_udc == cent or sum_udc == dez + uni or sum_udc == dez or
                 sum_udc == uni) and sum_udc != 0 and sum_mdc == 0:
                num += "e "

        if milho >= 1 or dmilho >= 1 or cmilho >= 1:
            if cmilho == 1 and dmilho == 0 and milho == 0:
                num += "Cem" + " Milhões"

            if cmilho == 1 and (dmilho != 0 or milho != 0):
                num += hundreds[0]
            if cmilho >= 2:
                num += hundreds[cmilho-1]
                if dmilho != 0 or milho != 0:
                    num += "e "
                if dmilho == 0 and milho == 0:
                    num += "Milhões "

            if dmilho == 1:
                num += dozens[milho] + " Milhões "

            if dmilho >= 2:
                num += dozens2[dmilho-2]
                if milho != 0:
                    num += "e "
                if milho == 0:
                    num += "Milhões "

            if milho >= 1 and dmilho != 1:
                if milho == 1 and dmilho != 0:
                    num += "Um Milhões "
                if milho == 1 and dmilho == 0:
                    num += "Um Milhão "
                else:
                    num += units[milho-1] + " Milhões "

            if (sum_udc == cent or sum_udc == dez + uni or sum_udc == dez or
                 sum_udc == uni) and sum_udc != 0 and sum_mdc == 0:
                num += "e "

        if mil >= 1 or dmil >= 1 or cmil >= 1:
            if cmil == 1 and dmil == 0 and mil == 0:
                num += "Cem" + " Mil "

            if cmil == 1 and (dmil != 0 or mil != 0):
                num += hundreds[0]
            if cmil >= 2:
                num += hundreds[cmil-1]
                if dmil != 0 or mil != 0:
                    num += "e "
                if dmil == 0 and mil == 0:
                    num += "Mil "

            if dmil == 1:
                num += dozens[mil] + " Mil "

            if dmil >= 2:
                num += dozens2[dmil-2]
                if mil != 0:
                    num += "e "
                if mil == 0:
                    num += "Mil "

            if mil >= 1 and dmil != 1:
                if mil == 1 and dmil == 0 and cmil == 0:
                    num += "Mil "
                else:
                    num += units[mil-1] + " Mil "

            if (sum_udc == cent or sum_udc == dez + uni or sum_udc == dez or
                sum_udc == uni) \
                    and sum_udc != 0:
                num += "e "

        if 2 <= cent == sum_udc:
            num += hundreds[cent-1]

        if 2 <= cent < sum_udc:
            num += hundreds[cent-1] + "e "

        if cent == 1:
            if cent == 1 and dez == 0 and uni == 0:
                num += "Cem"
            else:
                num += hundreds[0]

        if dez >= 2 and uni == 0:
            num += dozens2[dez-2]

        if dez >= 2 and uni >= 1:
            num += dozens2[dez-2] + "e "

        if dez == 1 and uni <= 9:
            num += dozens[uni]

        if uni != 0 and (dez >= 2 or dez == 0):
            num += units[uni-1]

        return num


def translate(number: str, base: str, verbose: str) -> str:
    word = ''

    if len(number) == 0:
        return ''
    if not is_base(base):
        if verbose:
            print('\'%s\': unknown base' % base)
        return ''
    if not is_valid_number(number, base, verbose=verbose):
        if verbose and is_base(base):
            print('%s does not exist in %s system' % (number, BASE_VERBOSE[base]))
        return ''
    if has_coma(number) and base == 'R':
        if verbose:
            print('Roman numbers are not float')
        return ''

    if base == 'D':
        if has_coma(number):
            part_int, part_float = number.split('.')
            word = extenso(part_int) + ' vírgula ' + extenso(part_float)
        else:
            word = extenso(number)

        return word
    
    if base == 'R':
        word = extenso(convert_rom_dec(number))
        return word

    for i in number:
        if i == '.':
            word += 'vírgula '
            continue
        elif is_letter(i):
            word += i
        else:
            word += extenso(i) + ' '

    return word


def translate_handler(args):
    print(translate(args.number, args.base, args.verbose))
