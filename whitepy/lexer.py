from .lexerconstants import *
from .ws_token import Tokeniser
from .debug import Debug as dbg


class IntError(ValueError):
    '''Exception when invalid integer is found'''


class Lexer(object):
    def __init__(self, line, debug=False):
        self.line = self._strip_non_ws(line)
        self.pos = 0
        self.tokens = [[]]
        self.debug = debug

    def _strip_non_ws(self, line):
        # remove all characters not defined in CHAR_MAP
        return ''.join([i for i in line if i in CHAR_MAP.values()])

    def _get_int(self, t):
        token = Tokeniser(debug=self.debug)
        if t in [a for a in HAS_ARGS if a is not 'PUSH']:
            const = 'LABEL'
        elif t == 'PUSH':
            const = 'SIGNED_INT'
        token.scan(self.line, self.pos, const)
        return token

    def _get_token(self, const):
        token = Tokeniser(debug=self.debug)
        token.scan(self.line, self.pos, const)
        return token

    def get_all_tokens(self):
        while self.pos < len(self.line):
            print(self.pos)
            req_tokens = 2
            # Get the constant needed to find token
            const = IMP_CONST if len(self.tokens[-1]) == 0 else eval(
                "{}_CONST".format(self.tokens[-1][0].type))
            token = self._get_token(const)
            print(token)
            self.pos = self.pos + len(token.value)
            self.tokens[-1].append(token)
            if token.type in HAS_ARGS:
                self.tokens[-1].append(self._get_int(token.type))
                # Add additional one to cater for lf at the end of int
                self.pos = self.pos + len(self.tokens[-1][-1].value) + 1
                # Increment the need number of tokens for the list
                req_tokens += 1
            if len(self.tokens[-1]) == req_tokens:
                self.tokens.append([])
        # Remove empty token list at the end
        del self.tokens[-1]

