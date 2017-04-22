from nose2.tools import *
import unittest
from whitepy.stack import Stack


class TestStack(unittest.TestCase):

    def test_isempty(self):
        stack = Stack()
        assert stack.isempty() is True

    def test_push(self):
        stack = Stack()
        stack.push(True)
        assert stack[-1]

    def test_duplicate_empty(self):
        stack = Stack()
        stack.dup()
        assert stack.isempty() is True

    def test_dupicate_nonempty(self):
        stack = Stack([True])
        stack.dup()
        assert len(stack) is 2 and stack[-1]

    def test_swap(self):
        stack = Stack('abc')
        stack.swap()
        assert stack[-1] is 'b' and stack[-2] is 'c'

    def test_discard(self):
        stack = Stack('abc')
        stack.discard()
        assert len(stack) is 2 and stack[-1] is 'b'

    def test_add(self):
        stack = Stack([1, 1])
        stack.math.add()
        assert len(stack) is 1 and stack[-1] is 2

    def test_subtract(self):
        stack = Stack([1, 3])
        stack.math.subtract()
        assert len(stack) is 1 and stack[-1] is 2

    def test_multiply(self):
        stack = Stack([2, 3])
        stack.math.multiply()
        assert len(stack) is 1 and stack[-1] is 6

    def test_divide(self):
        stack = Stack([2, 6])
        stack.math.divide()
        assert len(stack) is 1 and stack[-1] is 3

    def test_modulo(self):
        stack = Stack([3, 5])
        stack.math.modulo()
        assert len(stack) is 1 and stack[-1] is 2

    def test_stack_opper_dup_add(self):
        stack = Stack()
        stack.append(1)
        stack.dup()
        stack.math.add()
        assert len(stack) is 1 and stack[-1] is 2

    def test_stack_opper_swap_subtract(self):
        stack = Stack()
        stack.append(10)
        stack.append(5)
        stack.swap()
        stack.math.subtract()
        assert len(stack) is 1 and stack[-1] is 5
