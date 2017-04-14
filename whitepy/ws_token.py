from re import Scanner
from .lexerconstants import CHAR_MAP, NUM_CONST, NUM_SIGN_CONST
from .debug import Debug as dbg


class Tokeniser(object):
    def __init__(self, type=None, value=None, debug=False):
        self.value = value
        self.type = type
        self.debug = debug

    def __str__(self):
        return 'Token({}, {})'.format(self.get_type(), self.get_value())

    def __repr__(self):
        return self.__str__()

    def get_type(self):
        return self.type

    def get_value(self):
        value = dbg(self.value) if self.debug is True else self.value
        return value

    def _scan_int(self, string, const):
        # TODO: Add better invalid integer handling
        #       Check for integer sign, possibly treat unsigned integer
        #       as POSITIVE
        patterns = []
        INT_SIGN = (r"^[{}{}]".format(CHAR_MAP['space'], CHAR_MAP['tab']),
                    lambda scanner, token: ("INT_SIGN", token))
        INT_VAL = (r".[{}{}]*".format(CHAR_MAP['space'], CHAR_MAP['tab']),
                   lambda scanner, token: ("INT_VAL", token))
        if const == 'SIGNED_INT':
            patterns.append(INT_SIGN)
        patterns.append(INT_VAL)
        scanner = Scanner(patterns)
        found, remainder = scanner.scan(string)
        self.type = 'INT'
        try:
            self.value = ''.join([f[1] for f in found])
        except IndexError:
            print("Hit IndexError, string trying to check is: {}".
                  format(dbg(string)))

    def _scan_command(self, line, pos, const):
        patterns = [(r"^{}".format(i[0]), i[1]) for i in const]
        scanner = Scanner(patterns)
        found, remainder = scanner.scan(line[pos:])
        self.type = found[0]
        self.value = [i[0] for i in const if i[1] == self.type][0]

    def scan(self, line, pos, const):
        if const in ['LABEL', 'SIGNED_INT']:
            self._scan_int(line[pos:], const)
        else:
            self._scan_command(line, pos, const)
