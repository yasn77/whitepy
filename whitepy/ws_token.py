from re import Scanner
from .lexerconstants import CHAR_MAP, NUM_CONST, NUM_SIGN_CONST


class Tokeniser(object):
    def __init__(self, type=None, value=None):
        self.value = value
        self.type = type

    def __str__(self):
        return 'Token({}, {})'.format(self.type, self.value)

    def __repr__(self):
        return self.__str__()

    def get_type(self):
        return self.type

    def get_value(self):
        return self.value

    def _scan_int(self, string):
        patterns = [
            (r"^[{}{}]".format(CHAR_MAP['space'], CHAR_MAP['tab']),
             lambda scanner, token: ("INT_SIGN", token)),
            (r".[{}{}]*".format(CHAR_MAP['space'], CHAR_MAP['tab']),
             lambda scanner, token: ("INT_VAL", token)),
            (r".{}*".format(CHAR_MAP['lf']),
             lambda scanner, token: ("LINEFEED", token)),
        ]
        scanner = Scanner(patterns)
        found, remainder = scanner.scan(string)
        self.type = 'INT'
        self.value = ''.join([found[0][1], found[1][1]])

    def _scan_command(self, line, pos, const):
        patterns = [(r"^[{}]".format(i[0]), i[1]) for i in const]
        scanner = Scanner(patterns)
        found, remainder = scanner.scan(line[pos:])
        self.type = found[0]
        self.value = [i[0] for i in const if i[1] == self.type][0]

    def scan(self, line, pos, const):
        if const is 'INT':
            self._scan_int(line[pos:])
        else:
            self._scan_command(line, pos, const)
