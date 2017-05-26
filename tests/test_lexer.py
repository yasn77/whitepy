from whitepy.lexerconstants import IMP_CONST
import unittest
import whitepy.lexer as lexer


class TestLexer(unittest.TestCase):

    def _get_lexer(self, line):
        return lexer.Lexer(line=line)

    def _get_file_ws(self, filename):
        with open(filename, 'r') as f:
            lines = f.read()
        return lines

    def _sample_ws(self, ws_type):
        ws_samples = {
            'valid': "   \t\n",
            'invalid_int': "   \t",
            'non_ws': "A   \tB\nC",
            'calc': self._get_file_ws('./sample_ws/calc.ws'),
            'fibonacci': self._get_file_ws('./sample_ws/fibonacci.ws')
        }
        return self._get_lexer(ws_samples[ws_type])

    def test_get_int(self):
        lexer = self._sample_ws('valid')
        r = lexer._get_int('PUSH')
        assert r.get_type() == 'INT' and r.get_value() == "   \t"

    def test_get_token(self):
        lexer = self._sample_ws('valid')
        lexer.pos = 1
        r = lexer._get_token(IMP_CONST)
        assert r.get_type() == 'STACK_MANIPULATION'

    def test_get_all_tokens(self):
        lexer = self._sample_ws('valid')
        lexer.get_all_tokens()
        t = lexer.tokens
        assert t[0][0].get_type() is 'STACK_MANIPULATION' and \
            t[0][1].get_type() is 'PUSH' and t[0][2].get_type() is 'INT'

    def test_get_all_tokens_with_non_ws(self):
        lexer = self._sample_ws('non_ws')
        lexer.get_all_tokens()
        t = lexer.tokens
        assert t[0][0].get_type() is 'STACK_MANIPULATION' and \
            t[0][1].get_type() is 'PUSH' and t[0][2].get_type() is 'INT'

    def test_get_const(self):
        lexer = self._sample_ws('fibonacci')
        lexer.get_all_tokens()
        t = lexer.tokens
        self.assertTrue(False not in [True for i in t if
                                      type(lexer._get_const(i[1].get_type()) is
                                           dict)])
