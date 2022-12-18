"""
Neste módulo podemos encontrar todas as funções que tratam
da conversão de um sistema numérico para outro.
"""

from Valid import inv, isletra, isvirgula


def inverter(x: str) -> str:
    """
    Inverte a string x
    :param x: string à inverter
    :return: string invertida
    """

    return x[::-1] if type(x) is str else None


def hex_int(x: int) -> str:
    d = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    return d[x] if 10 <= x <= 15 else None


def int_hex(x: str) -> int:
    d = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    return d[x] if 64 < ord(x) < 71 else None


def converter2(x, y, z):
    """
        Converte um número(x) de qualquer base(y)
        para a base decimal(z).
    """
    if inv(x, y):
        if z == "D":
            pos = []
            if y == "B":
                if isvirgula(x):
                    partint = ""
                    partdec = ""
                    for i in range(len(x)):
                        if x[i] != ".":
                            partint += x[i]
                        else:
                            break

                    partint = inverter(partint)

                    for i in range(len(partint) + 1, len(x)):
                        partdec += x[i]

                    for i in range(len(partint) - 1, -1, -1):
                        if partint[i] == "1":
                            pos.append(i)

                    for i in range(len(partdec)):
                        if partdec[i] == "1":
                            pos.append(-i - 1)

                    contbin = 0

                    for i in pos:
                        contbin += pow(2, i)

                else:
                    x = inverter(x)

                    for i in range(len(x)):
                        if x[i] == "1":
                            pos.append(i)

                    contbin = 0

                    for i in pos:
                        contbin += pow(2, i)

                return contbin

            if y == "O":
                if isvirgula(x):
                    partint = ""
                    partdec = ""
                    for i in range(len(x)):
                        if x[i] != ".":
                            partint += x[i]
                        else:
                            break

                    partint = inverter(partint)

                    for i in range(len(partint) + 1, len(x)):
                        partdec += x[i]

                    for i in range(len(partint) - 1, -1, -1):
                        if int(partint[i]) >= 1:
                            pos.append(i)

                    for i in range(len(partdec)):
                        if int(partdec[i]) >= 1:
                            pos.append(-i - 1)

                    contoct = 0

                    partint = inverter(partint)
                    for i in range(len(partint)):
                        if int(partint[i]) >= 1:
                            contoct += int(partint[i]) * pow(8, pos[0])
                            pos.remove(pos[0])

                    for i in range(len(partdec)):
                        if int(partdec[i]) >= 1:
                            contoct += int(partdec[i]) * pow(8, pos[i])

                else:
                    x = inverter(x)

                    for i in range(len(x)):
                        if int(x[i]) >= 1:
                            pos.append(i)

                    contoct = 0

                    for i in pos:
                        contoct += int(x[i]) * pow(8, i)

                return contoct

            if y == "H":
                if isvirgula(x):
                    partint = ""
                    partdec = ""
                    for i in range(len(x)):
                        if x[i] != ".":
                            partint += x[i]
                        else:
                            break

                    partint = inverter(partint)

                    for i in range(len(partint) + 1, len(x)):
                        partdec += x[i]

                    for i in range(len(partint) - 1, -1, -1):
                        if isletra(partint[i]):
                            pos.append(i)
                        else:
                            if int(partint[i]) >= 1:
                                pos.append(i)

                    for i in range(len(partdec)):
                        if isletra(partdec[i]):
                            pos.append(-i - 1)
                        else:
                            if int(partdec[i]) >= 1:
                                pos.append(-i - 1)

                    conthex = 0

                    partint = inverter(partint)
                    for i in range(len(partint)):
                        if isletra(partint[i]):
                            conthex += int_hex(partint[i]) * pow(16, pos[0])
                            pos.remove(pos[0])
                        else:
                            if int(partint[i]) >= 1:
                                conthex += int(partint[i]) * pow(16, pos[0])
                                pos.remove(pos[0])

                    for i in range(len(partdec)):
                        if isletra(partdec[i]):
                            conthex += int_hex(partdec[i]) * pow(16, pos[i])
                        else:
                            if int(partdec[i]) >= 1:
                                conthex += int(partdec[i]) * pow(16, pos[i])

                else:
                    x = inverter(x)

                    for i in range(len(x)):
                        if isletra(x[i]):
                            pos.append(i)
                        else:
                            if int(x[i]) >= 1:
                                pos.append(i)

                    conthex = 0

                    for i in pos:
                        if isletra(x[i]):
                            conthex += int_hex(x[i]) * pow(16, i)
                        else:
                            conthex += int(x[i]) * pow(16, i)

                return conthex

            if y == 'R':
                return converter_rom_int(x)


def converter3(x, y, z):
    """
        Converte números(x) de base decimal(y)
        sem vírgula para qualquer base(z).
    """
    if inv(x, y):
        if y == "D":
            res = ""
            if z == "B":
                num = int(x)
                while num >= 1:
                    res += str(num % 2)
                    num = num // 2
                return inverter(res)

            if z == "O":
                num = int(x)
                while num >= 1:
                    res += str(num % 8)
                    num = num // 8
                return inverter(res)

            if z == "H":
                num = int(x)
                while num >= 1:
                    if num % 16 < 10:
                        res += str(num % 16)
                    else:
                        res += hex_int(num % 16)
                    num = num // 16
                return inverter(res)

            if z == "R":
                return converter_int_rom(int(x))


def converter4(x, y, z):
    """
        Converte números(x) da base decimal(y)
        com vírgula para qualquer base(z).
    """
    if inv(x, y):
        partint = ""
        partdec = "0"

        for i in range(len(x)):
            if x[i] != ".":
                partint += x[i]
            else:
                break

        for i in range(len(partint), len(x)):
            partdec += x[i]

        if z == "B":
            contbin = converter3(partint, "D", z) + "."
            numdec = float(partdec)
            ctrl = numdec
            for i in range(7):
                ctrl *= 2
                if ctrl > 1:
                    contbin += str(ctrl)[0]
                    ctrl -= 1
                else:
                    contbin += str(ctrl)[0]
                if ctrl == int(ctrl):
                    break
            return contbin

        if z == "O":
            contoct = converter3(partint, "D", z) + "."
            numdec = float(partdec)
            ctrl = numdec
            for i in range(7):
                ctrl *= 8
                if ctrl > 7:
                    contoct += str(ctrl)[0]
                    ctrl -= 7
                else:
                    contoct += str(ctrl)[0]
                if ctrl == int(ctrl):
                    break
            return contoct

        if z == "H":
            conthex = converter3(partint, "D", z) + "."
            numdec = float(partdec)
            ctrl = numdec
            for i in range(7):
                ctrl *= 16
                if ctrl > 15:
                    conthex += hex_int(int(ctrl))
                    ctrl -= 15
                else:
                    if ctrl >= 10:
                        conthex += hex_int(int(ctrl))
                        ctrl -= int(ctrl)
                    else:
                        conthex += str(ctrl)[0]
                        ctrl -= int(ctrl)
                if ctrl == int(ctrl):
                    break
            return conthex


def converter_rom_int(x):
    cont: int = 0
    if inv(x, "R"):
        for i in range(len(x)):
            if x[i] == "I":
                if i < len(x) - 1:
                    if x[i + 1] == "V" or x[i + 1] == "X":
                        cont -= 1
                    else:
                        cont += 1
                else:
                    cont += 1

            if x[i] == "V":
                cont += 5

            if x[i] == "X":
                if i < len(x) - 1:
                    if x[i + 1] == "L" or x[i + 1] == "C":
                        cont -= 10
                    else:
                        cont += 10
                else:
                    cont += 10

            if x[i] == "L":
                cont += 50

            if x[i] == "C":
                if i < len(x) - 1:
                    if x[i + 1] == "D" or x[i + 1] == "M":
                        cont -= 100
                    else:
                        cont += 100
                else:
                    cont += 100

            if x[i] == "D":
                cont += 500

            if x[i] == "M":
                cont += 1000

    return cont


def converter_int_rom(x):
    rom = ""
    uni = x % 10
    dez = (x % 100) // 10
    cent = (x % 1000) // 100
    mil = x / 1000

    if mil != 0:
        rom += "M" * int(mil)

    if cent != 0:
        if cent == 1:
            rom += "C"
        elif cent == 2:
            rom += "CC"
        elif cent == 3:
            rom += "CCC"
        elif cent == 4:
            rom += "CD"
        elif cent == 5:
            rom += "D"
        elif cent == 6:
            rom += "DC"
        elif cent == 7:
            rom += "DCC"
        elif cent == 8:
            rom += "DCCC"
        else:
            rom += "CM"

    if dez != 0:
        if dez == 1:
            rom += "X"
        elif dez == 2:
            rom += "XX"
        elif dez == 3:
            rom += "XXX"
        elif dez == 4:
            rom += "XL"
        elif dez == 5:
            rom += "L"
        elif dez == 6:
            rom += "LX"
        elif dez == 7:
            rom += "LXX"
        elif dez == 8:
            rom += "LXXX"
        else:
            rom += "XC"

    if uni != 0:
        if uni == 1:
            rom += "I"
        elif uni == 2:
            rom += "II"
        elif uni == 3:
            rom += "III"
        elif uni == 4:
            rom += "IV"
        elif uni == 5:
            rom += "V"
        elif uni == 6:
            rom += "VI"
        elif uni == 7:
            rom += "VII"
        elif uni == 8:
            rom += "VIII"
        else:
            rom += "IX"

    if rom.count('M') > 3 and x < 3900:
        return None

    return rom


def converter(x, y, z):
    if y == "D":
        if isvirgula(x):
            return converter4(x, y, z)
        else:
            return converter3(x, y, z)

    elif z == "D":
        return str(converter2(x, y, z))

    else:
        if isvirgula(x):
            return converter4(str(converter2(x, y, "D")), "D", z)
        else:
            return converter3(str(converter2(x, y, "D")), "D", z)
