import unittest
from whitepy.stack import Stack
from whitepy.heap import Heap


class TestHeap(unittest.TestCase):

    def test_set(self):
        stack = Stack(['addr', 'item'])
        heap = Heap(stack)
        heap.set()
        assert heap['addr'] == 'item'

    def test_get(self):
        stack = Stack(['addr', 'item'])
        heap = Heap(stack)
        heap.set()
        stack.push('addr')
        heap.get()
        assert stack.pop() == 'item'
