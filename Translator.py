"""
Neste módulo encontramos as funções que tratam da representação
"""

from Valid import isvirgula, isv, isFloat


def extenso(x):
    try:
        x = int(x)
    except TypeError:
        return None

    if x == 0:
        return "Zero"

    else:
        num: str = ""
        unidades = ["Um", "Dois", "Três", "Quatro", "Cinco", "Seis",
                    "Sete", "Oito", "Nove"]
        dezenas = ["Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze",
                   "Dezasseis", "Dezassete", "Dezoito", "Dezanove"]
        dezenas2 = ["Vinte ", "Trinta ", "Quarenta ", "Cinquenta ",
                    "Sessenta ", "Setenta ", "Oitenta ", "Noventa "]
        centenas = ["Cento e ", "Duzentos ", "Trezentos ", "Quatrocentos ",
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
        somaUDC, somaMDC = uni + dez + cent, mil + dmil + cmil

        if 1 <= bil <= 9:
            if bil == 1:
                num += "Um Bilhão "
            elif bil >= 2:
                num += unidades[bil-1] + " Bilhões "

            if (somaUDC == cent or somaUDC == dez + uni or somaUDC == dez or
                 somaUDC == uni) and somaUDC != 0 and somaMDC == 0:
                num += "e "

        if milho >= 1 or dmilho >= 1 or cmilho >= 1:
            if cmilho == 1 and dmilho == 0 and milho == 0:
                num += "Cem" + " Milhões"

            if cmilho == 1 and (dmilho != 0 or milho != 0):
                num += centenas[0]
            if cmilho >= 2:
                num += centenas[cmilho-1]
                if dmilho != 0 or milho != 0:
                    num += "e "
                if dmilho == 0 and milho == 0:
                    num += "Milhões "

            if dmilho == 1:
                num += dezenas[milho] + " Milhões "

            if dmilho >= 2:
                num += dezenas2[dmilho-2]
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
                    num += unidades[milho-1] + " Milhões "

            if (somaUDC == cent or somaUDC == dez + uni or somaUDC == dez or
                 somaUDC == uni) and somaUDC != 0 and somaMDC == 0:
                num += "e "

        if mil >= 1 or dmil >= 1 or cmil >= 1:
            if cmil == 1 and dmil == 0 and mil == 0:
                num += "Cem" + " Mil "

            if cmil == 1 and (dmil != 0 or mil != 0):
                num += centenas[0]
            if cmil >= 2:
                num += centenas[cmil-1]
                if dmil != 0 or mil != 0:
                    num += "e "
                if dmil == 0 and mil == 0:
                    num += "Mil "

            if dmil == 1:
                num += dezenas[mil] + " Mil "

            if dmil >= 2:
                num += dezenas2[dmil-2]
                if mil != 0:
                    num += "e "
                if mil == 0:
                    num += "Mil "

            if mil >= 1 and dmil != 1:
                if mil == 1 and dmil == 0 and cmil == 0:
                    num += "Mil "
                else:
                    num += unidades[mil-1] + " Mil "

            if (somaUDC == cent or somaUDC == dez + uni or somaUDC == dez or
                somaUDC == uni) \
                    and somaUDC != 0:
                num += "e "

        if 2 <= cent == somaUDC:
            num += centenas[cent-1]

        if 2 <= cent < somaUDC:
            num += centenas[cent-1] + "e "

        if cent == 1:
            if cent == 1 and dez == 0 and uni == 0:
                num += "Cem"
            else:
                num += centenas[0]

        if dez >= 2 and uni == 0:
            num += dezenas2[dez-2]

        if dez >= 2 and uni >= 1:
            num += dezenas2[dez-2] + "e "

        if dez == 1 and uni <= 9:
            num += dezenas[uni]

        if uni != 0 and (dez >= 2 or dez == 0):
            num += unidades[uni-1]

        return num


def ext(x, y):
    if not isv(y):
        return None

    num = ""

    if y == "B":
        if isvirgula(x):
            for i in range(len(x)):
                if x[i] == ".":
                    num += "vírgula "
                else:
                    num += extenso(int(x[i])) + " "
        else:
            for i in range(len(x)):
                num += extenso(int(x[i])) + " "

    elif y == "O":
        if isvirgula(x):
            for i in range(len(x)):
                if x[i] == ".":
                    num += "vírgula "
                else:
                    num += extenso(int(x[i])) + " "
        else:
            for i in range(len(x)):
                num += extenso(int(x[i])) + " "

    elif y == "H":
        if isvirgula(x):
            for i in range(len(x)):
                if x[i] == ".":
                    num += "vírgula "
                elif isFloat(x[i]):
                    num += extenso(int(x[i])) + " "
                else:
                    num += x[i] + " "
        else:
            for i in range(len(x)):
                if isFloat(x[i]):
                    num += extenso(int(x[i])) + " "
                else:
                    num += x[i] + " "

    elif y == "D":
        if isvirgula(x):
            partint, partdec = "", ""

            for i in range(len(x)):
                if x[i] != ".":
                    partint += x[i]
                else:
                    break

            for i in range(len(partint) + 1, len(x)):
                partdec += x[i]

            num += extenso(int(partint)) + " vírgula " + extenso(int(partdec))

        else:
            num += extenso(int(x))
    else:
        return None

    return num
