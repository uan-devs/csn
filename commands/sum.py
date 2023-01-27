from helpers.validation import is_valid_number
from commands.convert import convert
from globals.numbers import BASE_VERBOSE


def extract_numbers(
        _bin: list[str], _dec: list[str], _oct: list[str],
        _hex: list[str], _rom: list[str], verbose: bool = False
) -> dict:
    numbers = dict()
    if _bin is not None:
        for i in _bin:
            if not is_valid_number(i, 'B'):
                if verbose:
                    print(
                        '%s is not valid at %s system\nWill not be added\n'
                        % (i, BASE_VERBOSE['B'])
                    )
                _bin.remove(i)
        numbers['bin'] = _bin
    else:
        numbers['bin'] = []

    if _dec is not None:
        for i in _dec:
            if not is_valid_number(i, 'D'):
                if verbose:
                    print(
                        '%s is not valid at %s system\nWill not be added\n'
                        % (i, BASE_VERBOSE['D'])
                    )
                _dec.remove(i)
        numbers['dec'] = _dec
    else:
        numbers['dec'] = []

    if _oct is not None:
        for i in _oct:
            if not is_valid_number(i, 'O'):
                if verbose:
                    print(
                        '%s is not valid at %s system\nWill not be added\n'
                        % (i, BASE_VERBOSE['O'])
                    )
                _oct.remove(i)
        numbers['oct'] = _oct
    else:
        numbers['oct'] = []

    if _hex is not None:
        for i in _hex:
            if not is_valid_number(i, 'H'):
                if verbose:
                    print(
                        '%s is not valid at %s system\nWill not be added\n'
                        % (i, BASE_VERBOSE['H'])
                    )
                _hex.remove(i)
        numbers['hex'] = _hex
    else:
        numbers['hex'] = []

    if _rom is not None:
        for i in _rom:
            if not is_valid_number(i, 'R'):
                if verbose:
                    print(
                        '%s is not valid at %s system\nWill not be added\n'
                        % (i, BASE_VERBOSE['R'])
                    )
                _rom.remove(i)
        numbers['rom'] = _rom
    else:
        numbers['rom'] = []

    return numbers


def sum_numbers(numbers: dict, verbose: bool = False, force: bool = False) -> str:
    result = 0
    for i in numbers:
        for j in numbers[i]:
            try:
                result += int(convert(j, i[0].capitalize(), 'D', verbose=verbose))
            except ValueError:
                if verbose and not force:
                    print('Operation will be stopped\n')
                    return '-1'
                if force:
                    continue
                return '-1'

    return str(result)


def sum_handler(args):
    print(
        'Sum result [mode +] = %s'
        % sum_numbers(
            extract_numbers(
                _bin=args.bin, _dec=args.dec, _hex=args.hex,
                _oct=args.oct, _rom=args.rom, verbose=args.verbose
            ),
            verbose=args.verbose,
            force=args.force
        )
    )
