import unittest
from whitepy.debug import Debug as debug


class TestLexer(unittest.TestCase):

    def _get_debug(self, line):
        return debug(line)

    def _sample_ws(self, ws_type):
        ws_samples = {
            'valid': "   \t\n",
            'invalid_int': "   \t",
            'non_ws': "A   \tB\nC"
        }
        return self._get_debug(ws_samples[ws_type])

    def test_get_int(self):
        dbg = self._sample_ws('valid')
        assert dbg.__str__() == '..._|'
