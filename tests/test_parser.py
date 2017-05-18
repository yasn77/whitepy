import unittest
from unittest.mock import patch, call

import whitepy.lexer as lexer
from whitepy.parser import Parser


class TestParser(unittest.TestCase):

    def _get_tokens(self, filename):
        with open(filename, 'r') as f:
            lines = f.read()
            item = lexer.Lexer(line=lines)
            item.get_all_tokens()
        return item.tokens

    def test_get_value_signed(self):
        num = Parser._get_value(Parser, '  ', signed=True)
        self.assertEqual(num, 0)

    def test_get_value_notsigned(self):
        num = Parser._get_value(Parser, ' ', signed=False)
        self.assertEqual(num, 0)

    def test_hello_world(self):
        tokens = self._get_tokens('./sample_ws/helloworld.ws')
        p = Parser(tokens)
        with self.assertRaises(SystemExit) as ec:
            with patch('sys.stdout') as fake_stdout:
                p.parse()
        (fake_stdout.asset_has_calls[
                call.buffer.write(b'H'),
                call.buffer.write(b'e'),
                call.buffer.write(b'l'),
                call.buffer.write(b'l'),
                call.buffer.write(b'o'),
                call.buffer.write(b','),
                call.buffer.write(b' '),
                call.buffer.write(b'W'),
                call.buffer.write(b'o'),
                call.buffer.write(b'r'),
                call.buffer.write(b'l'),
                call.buffer.write(b'd'),
                call.buffer.write(b'!'),
                call.buffer.write(b'\n')]) and self.assertEqual(
                    ec.exception.code, 0)

    def test_fibonacci(self):
        tokens = self._get_tokens('./sample_ws/helloworld.ws')
        p = Parser(tokens)
        with self.assertRaises(SystemExit) as ec:
            with patch('builtins.input', side_effect='2'):
                with patch('sys.stdout') as fake_stdout:
                    p.parse()
        (fake_stdout.asset_has_calls[
                call.buffer.write(b'1'),
                call.buffer.write(b'1'),
                call.buffer.write(b'2'),
                call.buffer.write(b'3'),
                call.buffer.write(b'\n')]) and self.assertEqual(
                    ec.exception.code, 0)
