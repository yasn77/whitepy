from unittest.mock import patch, call
import unittest
from whitepy.ws_io import IO as ws_io
from whitepy.heap import Heap
from whitepy.stack import Stack


class TestIo(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.heap = Heap(self.stack)
        self.io = ws_io(self.stack)

    @patch('builtins.input', side_effect='TEST'.split())
    def test_i_chr(self, input):
        self.stack.push('1')  # Heap address used for stack.pop()
        self.stack.push('1')  # Heap address for storing input
        self.io.i_chr(self.heap)
        self.heap.get()
        assert self.stack.pop() == 'TEST'

    @patch('builtins.input', side_effect='1')
    def test_i_int(self, input):
        self.stack.push('1')  # Heap address used for stack.pop()
        self.stack.push('1')  # Heap address for storing input
        self.io.i_int(self.heap)
        self.heap.get()
        assert self.stack.pop() == 1

    def test_o_int(self):
        self.stack.push('1')
        with patch('sys.stdout') as fake_stdout:
            self.io.o_int()
        (fake_stdout.asset_has_calls[call.buffer.write(b'1')])

    def test_o_chr(self):
        self.stack.push(65)
        with patch('sys.stdout') as fake_stdout:
            self.io.o_chr()
        (fake_stdout.asset_has_calls[call.buffer.write(b'A')])
