from .lexerconstants import *
from .ws_token import Tokeniser


class Lexer(object):
    def __init__(self, line):
        self.line = line
        self.pos = 0
        self.tokens = []

    def _get_int(self):
        token = Tokeniser()
        if self.line[-1] == '\n':
            const = 'INT'
            token.scan(self.line, self.pos, const)
        else:
            # TODO: Add error handling for invalid integer
            pass
        return token

    def _get_token(self, const):
        token = Tokeniser()
        token.scan(self.line, self.pos, const)
        return token

    def get_all_tokens(self):
        while self.pos < len(self.line):
            const = IMP_CONST if self.pos is 0 else eval(
                "{}_CONST".format(self.tokens[0].type))
            token = self._get_token(const)
            self.tokens.append(token)
            self.pos = self.pos + len(token.value)
            if token.type == 'PUSH':
                self.tokens.append(self._get_int())
                self.pos = len(self.line)

