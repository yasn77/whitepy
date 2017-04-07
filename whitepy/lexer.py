from .lexerconstants import *
from .ws_token import Tokeniser


class IntError(ValueError):
    '''Exception when invalid integer is found'''


class Lexer(object):
    def __init__(self, line):
        self.line = self._strip_non_ws(line)
        self.pos = 0
        self.tokens = [[]]

    def _strip_non_ws(self, line):
        # remove all characters not defined in CHAR_MAP
        return ''.join([i for i in line if i in CHAR_MAP.values()])

    def _get_int(self):
        token = Tokeniser()
        const = 'INT'
        token.scan(self.line, self.pos, const)
        return token

    def _get_token(self, const):
        token = Tokeniser()
        token.scan(self.line, self.pos, const)
        return token

    def get_all_tokens(self):
        while self.pos < len(self.line):
            req_tokens = 2
            # Get the constant needed to find token
            const = IMP_CONST if len(self.tokens[-1]) == 0 else eval(
                "{}_CONST".format(self.tokens[-1][0].type))
            token = self._get_token(const)
            self.pos = self.pos + len(token.value)
            self.tokens[-1].append(token)
            if token.type in HAS_ARGS:
                self.tokens[-1].append(self._get_int())
                # Add additional one to cater for lf at the end of int
                self.pos = self.pos + len(self.tokens[-1][-1].value) + 1
                # Increment the need number of tokens for the list
                req_tokens += 1
            if len(self.tokens[-1]) == req_tokens:
                self.tokens.append([])
        # Remove empty token list at the end
        del self.tokens[-1]


