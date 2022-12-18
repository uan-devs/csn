from string import ascii_letters
from os import path

__all__ = ['isv', 'inv', 'isvirgula', 'isletra', 'isFloat',
           'is_arquivo_valido']


def isv(x):
    return x == "D" or x == "B" or x == "O" or x == "H" or x == 'R'


def inv(x, y):
    if not isv(y):
        return False

    contbin = 0
    if y == "B":
        for i in range(len(x)):
            if x[i] == "0" or x[i] == "1" or x[i] == ".":
                contbin += 1

    contoct = 0
    if y == "O":
        for i in range(len(x)):
            if x[i] == ".":
                contoct += 1
            for j in range(0, 8):
                if x[i] == str(j):
                    contoct += 1

    contdec = 0
    if y == "D":
        for i in range(len(x)):
            if x[i] == ".":
                contdec += 1
            for j in range(0, 11):
                if x[i] == str(j):
                    contdec += 1

    conthex = 0
    if y == "H":
        for i in range(len(x)):
            for j in ascii_letters[26:32]:
                if x[i] == j:
                    conthex += 1
        for i in range(len(x)):
            if x[i] == ".":
                conthex += 1
            for j in range(0, 10):
                if x[i] == str(j):
                    conthex += 1

    controm = 0
    if y == "R":
        romanos = ["I", "V", "X", "L", "C", "D", "M"]
        for i in range(len(x)):
            for j in romanos:
                if x[i] == j:
                    controm += 1

        for i in range(len(x)):
            for j in range(0, 10):
                if x[i] == str(j):
                    controm += 1

    return (contdec == len(x) and y == "D") or \
           (contbin == len(x) and y == "B") or \
           (contoct == len(x) and y == "O") or \
           (conthex == len(x) and y == "H") or \
           (controm == len(x) and y == "R")


def isvirgula(x):
    contV = 0
    for i in range(len(x)):
        if x[i] == ".":
            contV += 1
    return contV == 1


def isletra(x):
    """
    Verifica se na string existe letra.
    """
    contL = 0
    for i in range(len(x)):
        for j in ascii_letters[26:32]:
            if x[i] == j:
                contL += 1
    return contL >= 1


def isFloat(x):
    try:
        float(x)
        return True
    except TypeError:
        return False


def is_arquivo_valido(x: str) -> bool:
    if type(x) != str:
        return False

    # Verifica se o (caminho para o) ficheiro existe.
    elif path.exists(x):
        abre = open(x, 'r')
        conteudo = abre.readlines()
        abre.close()

        # Verifica se há conteúdo no ficheiro.
        if len(conteudo) == 0:
            return False

        # Serve para iterar sobre o conteúdo do ficheiro.
        for i in range(len(conteudo)):

            # Verifica se certos caracteres existem e na quantidade certa.
            if conteudo[i].count('(') != 2 and conteudo[i].count(')') != 2 and\
                    conteudo[i].count('=') != 1 and \
                    conteudo[i].count('?') != 1 and \
                    conteudo[i].count(' ') != 2:
                return False

            if conteudo[i][0] != '(':
                return False

            # Serve para iterar sobre o conteúdo de cada linha do ficheiro.
            for k in range(len(conteudo[i])):

                # Verifica se o número é um número válido na base dada.
                if conteudo[i][k] == ')' and conteudo[i][k - 1] != '?' and \
                        not inv(conteudo[i][1:k], conteudo[i][k + 1]):
                    return False

                if conteudo[i][k] == ' ' and not \
                        ((conteudo[i][k + 1] == '=' or
                          conteudo[i][k - 1] == '=') and k > 0):
                    return False

                if conteudo[i][k] == ')' and not isv(conteudo[i][k + 1]):
                    return False

            # Verifica se o último elemento de cada linha do ficheiro
            # é uma base numérica válida.
            if not isv(conteudo[i][len(conteudo[i]) - 2]) and \
                    i < len(conteudo) - 1:
                return False

            if i == len(conteudo) - 1 and not \
                    isv(conteudo[i][len(conteudo[i]) - 1]):
                return False

        return True

    else:
        return False
