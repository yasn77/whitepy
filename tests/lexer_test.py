from whitepy.lexerconstants import *
import whitepy.lexer as lexer
import unittest


class TestLexer(unittest.TestCase):

    def _get_lexer(self, line):
        return lexer.Lexer(line=line)

    def _valid_ws(self):
        return self._get_lexer("   \t\n")

    def test_get_int(self):
        lexer = self._valid_ws()
        r = lexer._get_int()
        assert r.get_type() == 'INT' and r.get_value() == 'POSITIVE 001'

    def test_get_token(self):
        lexer = self._valid_ws()
        lexer.pos = 1
        r = lexer._get_token(IMP_CONST)
        assert r.get_type() == 'STACK_MANIPULATION'

    def test_get_all_tokens(self):
        lexer = self._valid_ws()
        lexer.get_all_tokens()
        t = lexer.tokens
        assert t[0].get_type() is 'STACK_MANIPULATION' and \
            t[1].get_type() is 'PUSH' and t[2].get_type() is 'INT'
