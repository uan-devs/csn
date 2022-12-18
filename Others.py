from Valid import is_arquivo_valido, isv, inv
from converter import converter, converter_int_rom, converter_rom_int
from Translator import ext
from os import path


def __exportar(x, y, z):
    with open("c:/Users/sweet/Desktop/ArquivoExportado.num", "w") as abre:
        for i in range(len(x)):
            _ = converter(x[i], y[i], z[i])
            abre.write("(%s)%s = (%s)%s (%s)\n" % (x[i], y[i], _, z[i],
                                                   ext(_, z[i])))


def msg():
    m = '''
              ____________
             /            \\
            /              \\
         /\\/	            \\/\\
         \\ |   ****   ****  | /
          \\|   ****   ****  |/
           |   ***     ***  |
           |                |
           \\_      ***     _/
             |\\    ***   /|
             | |        | |
             | IIIIIIIIII |
             | IIIIIIIIII |
             \\_          _/
               \\_      _/
                  \\___/
        '''
    print(m)


def importar(x):
    if is_arquivo_valido(x):

        with open(x) as abre:
            linhas = abre.readlines()

        numeros, bOrigem, bDestino = [], [], []

        for i in range(len(linhas)):
            numeros.append("")
            bOrigem.append("")
            bDestino.append("")

        for i in range(len(linhas)):
            numeros[i] += linhas[i][1:linhas[i].index(')')]
            bOrigem[i] += linhas[i][linhas[i].index(')') + 1]
            bDestino[i] += linhas[i][linhas[i].index('?') + 2]

        __exportar(numeros, bOrigem, bDestino)

        return True

    else:
        return False


def ver():
    if path.exists('c:/Users/sweet/Desktop/ArquivoExportado.num'):
        with open('c:/Users/sweet/Desktop/ArquivoExportado.num') as f:
            for i in f.readlines():
                print(i)


def sobre():
    prt()
    print("Ajuda do Conversor de Sistemas de Numeração.".center(110))
    prt()
    print("""
        Olá, eu sou o Eliúde P. C. Vemba, e esta é
        a versão python do conversor de siste-
        mas de numeração. A 1ª versão(Java) eu
        fiz no meu 1º ano da faculdade de ciên-
        cias da Universidade Agostinho Neto no
        curso de Ciências da Computação.

        Esta versão(Python) está a ser desenvolvida
        2 meses após eu concluir a versão Java dela.

        Nesta versão(Python) resolvi alguns bugs que
        que encontrei na versão Java, bugs como: con-
        verter números com vírgula para a base hexa-
        decimal, binária e octal, e a função que con-
        verte números romanos inexistentes para inte-
        iro e é possível tenha mais bugs.

        Com este programa é possível:
            1º Verificar se a base numérica é válida.
            Nota: Ao invés de números 10, 2, 16, 8 uti-
            zou-se caracteres D, B, H, O para represen-
            tar as bases númericas e estas são as úni-
            cas existentes no programa.""")

    print("""
            2º Verificar se um número é válido numa base
            numérica.

            3º Converter um número de uma base numérica
            para outra. Esta é a função chave do programa.""")


def listagem():
    prt()
    print("Lista das bases numéricas disponíveis".center(110))
    prt()
    print("""
    Para:
        Binário - B
        Octal - O
        Hexadecimal - H
        Decimal - D
        Romano - R

    Nota: Não utilizar 2, 8, 16, 10, b, o, h, d ou
        outras além das descritas acima, no conversor
        ou nas funções diretamente.\n
    """)


def prt():
    print("-" * 115)


def rep_ascii(x, y):
    x = str(x)
    _ = ''

    for i in x:
        _ += converter(str(ord(i)), 'D', y) if i != ' ' else ' '
    print(_, end='\n')


def menu():
    prt()
    print("\t\t\tBem-vindo ao Sistema de conversão bases númericas")
    prt()
    print("\n\t1-Sobre")
    print("\n\t2-Verificar se a base é válida.")
    print("\n\t3-Verificar se um número é válido numa determinada base.")
    print("\n\t4-Converter um número de uma determinada base para outra.")
    print("\n\t5-Converter um número romano para um número árabe.")
    print("\n\t6-Converter um número árabe para um número romano.")
    print("\n\t7-Mostrar um número por extenso.")
    print("\n\t8-Importar um ficheiro com números e converter o mesmo.")
    print("\n\t9-ASCII")
    print("\n\t10-Sair\n")

    opc = int(input("Selecione a sua opção: "))

    if opc == 10 or opc not in list(range(1, 10)):
        pass

    if opc == 1:
        sobre()
        menu()

    if opc == 2:
        try:
            prt()
            print("Verificação de bases numéricas.".center(110))
            prt()
            x = input("\nIntroduza a base: ").upper()
            print("\nA base é válida.\n" if isv(x) else "\nNão é válida.\n")
            esc = input("Deseja ver as bases disponíveis(S/N): ").upper()
            if esc == "S":
                listagem()
            menu()
        except TypeError:
            msg()
            print("Parâmetro inválido.\n")
            menu()

    if opc == 3:
        try:
            prt()
            print("Verificação de números nas bases numéricas.".center(110))
            prt()
            x = input("\nIntroduza o número: ").upper()
            y = input("Introduza a base: ").upper()
            print("\nO número é valido.\n" if inv(x, y) else "\nÑ é válido.\n")
            menu()
        except TypeError:
            msg()
            print("Parâmetro inválido.\n")
            menu()

    if opc == 4:
        try:
            prt()
            print("Conversão de um número de uma base numérica para outra"
                  ".".center(110))
            prt()
            x = input("\nIntroduza o número: ").upper()
            y = input("Introduza a base do número digitado: ").upper()
            z = input("Introduza a base do número pretendido: ").upper()
            if inv(x, y) and isv(z):
                print("\n(%s)%s = (%s)%s\n" % (x, y, converter(x, y, z), z))
            else:
                print('\nIntroduza números válidos e bases válidas.\n')
            menu()
        except TypeError:
            msg()
            print("Parâmetro inválido.\n")
            menu()

    if opc == 5:
        try:
            prt()
            print("Conversão de um número romano para inteiro.".center(110))
            prt()
            x = input("\nIntroduza o número: ").upper()
            a = converter_rom_int(x)
            b = converter_int_rom(a)
            if b == x:
                print("\n(%s)%s = (%i)%s\n" % (
                    x, "R", converter_rom_int(x), "D"))
                menu()
            else:
                print("\nO número não existe.\n")
                menu()
        except TypeError:
            msg()
            print("Parâmetro inválido.\n")
            menu()

    if opc == 6:
        try:
            prt()
            print("Conversão de um número inteiro para romano.".center(110))
            prt()
            x = int(input("\nIntroduza o número: "))
            if x <= 0 or x > 3999:
                print("Não existe representação romana para %i\n" % x)
            else:
                print("\n(%i)%s = (%s)%s\n" % (
                    x, "D", converter_int_rom(x), "R"))
            menu()
        except TypeError:
            msg()
            print("Parâmetro inválido.\n")
            menu()

    if opc == 7:
        try:
            prt()
            print("Apresentação de um número por extenso.".center(110))
            prt()
            x = input("\nIntroduza o número: ").upper()
            y = input("Base numérica: ").upper()
            print("\n%s\n" % ext(x, y))
            menu()
        except TypeError:
            msg()
            print("Parâmetro inválido.\n")
            menu()

    if opc == 8:
        try:
            prt()
            print("Exportar ficheiro com números convertidos.".center(110))
            prt()
            f = input("\nIntroduza o nome do ficheiro à importar: ")
            print("\nO ficheiro foi exportado com sucesso...\n" if importar(
                f) else "\nO ficheiro é inválido...\n")
            esc = input('Ver o arquivo exportado(S/N): ').upper()
            if esc == 'S':
                ver()
            menu()
        except TypeError:
            msg()
            print("O ficheiro não foi exportado.\n")
            menu()

    if opc == 9:
        try:
            prt()
            print("Representação ASCII.".center(110))
            prt()
            x = input("\nEscreva qualquer coisa: ")
            y = input("Base numérica para representação: ").upper()
            rep_ascii(x, y)
            menu()
        except TypeError:
            msg()
            print("Parâmetro inválido.\n")
            menu()
