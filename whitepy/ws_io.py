import readchar
import sys


class IO(object):
    def __init__(self, stack):
        self.stack = stack

    def i_chr(self, heap):
        self.stack.push(readchar.readchar())
        heap.set()

    def i_int(self, heap):
        num = None
        while type(num) is not int:
            try:
                num = int(readchar.readchar())
            except ValueError:
                pass
        self.stack.push(num)
        heap.set()

    def o_chr(self):
        char = chr(self.stack.pop())
        sys.stdout.buffer.write(char.encode('utf-8'))

    def o_int(self):
        integer = int(chr(self.stack.pop()))
        sys.stdout.buffer.write(str(integer).encode('utf-8'))
