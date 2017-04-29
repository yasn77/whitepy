from collections import deque


class StackMath(object):
    def __init__(self, stack):
        self.stack = stack

    def _get_operands(self):
        # TODO: Exception handling if value can't be casted to int
        right = int(self.stack.pop())
        left = int(self.stack.pop())
        return (left, right)

    def add(self):
        operands = self._get_operands()
        self.stack.push(operands[0] + operands[1])

    def subtract(self):
        operands = self._get_operands()
        self.stack.push(operands[0] - operands[1])

    def multiply(self):
        operands = self._get_operands()
        self.stack.push(operands[0] * operands[1])

    def divide(self):
        operands = self._get_operands()
        self.stack.push(operands[0] // operands[1])

    def modulo(self):
        operands = self._get_operands()
        self.stack.push(operands[0] % operands[1])


class Stack(deque):
    def __init__(self, item=''):
        super(Stack, self).__init__(item)
        self.math = StackMath(self)

    def push(self, item):
        self.append(item)

    def isempty(self):
        return True if len(self) is 0 else False

    def dup(self):
        if not self.isempty():
            self.append(self[-1])
        else:
            pass

    def swap(self):
        self[-1], self[-2] = self[-2], self[-1]

    def discard(self):
        self.pop()
