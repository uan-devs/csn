"""
Este é o 'main' do Conversor De Sistemas Numéricos.
"""

from sys import argv
from time import time
from Others import menu, msg
from Translator import ext
from converter import converter


if __name__ == '__main__':
    a = time()
    if len(argv) == 1:
        menu()
        b = time()
        t = b - a
        if t <= 59:
            print("\nTempo de utilização: %is" % t)
        else:
            print("\nTempo de utilização: %.2fmin" % (t / 60))
    else:
        if argv[1] == "ext" and len(argv) == 4:
            print("%s" % ext(argv[2], argv[3]))

        elif argv[1] == "msg" and len(argv) == 2:
            msg()

        elif argv[1] == "converter" and len(argv) == 5:
            print("%s" % converter(argv[2], argv[3], argv[4]))
