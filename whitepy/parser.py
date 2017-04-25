from functools import partial
from .lexerconstants import HAS_ARGS, NUM_CONST, NUM_SIGN_CONST
from .stack import Stack
from .heap import Heap
from .ws_io import IO as ws_io


class Parser(object):
    def __init__(self, tokens):
        self.token_list = tokens
        self.stack = Stack()
        self.heap = Heap(self.stack)
        self.io = ws_io(self.stack)
        self.method_map = {
            'STACK_MANIPULATION': {
                'PUSH': partial(self.stack.push),
                'DUP': self.stack.dup,
                'SWAP': self.stack.swap,
                'POP': self.stack.pop
            },
            'IO': {
                'OUTPUT_CHAR': self.io.o_chr,
                'OUTPUT_NUM': self.io.o_int,
                'READ_CHAR': partial(self.io.i_chr, self.heap),
                'READ_NUM': partial(self.io.i_chr, self.heap)
            },
            'FLOW_CONTROL': {
                'END': self.clean
            }
        }

    def _get_value(self, ws_int, signed=False):
        if signed:
            sign = '-' if NUM_SIGN_CONST[ws_int.pop(0)] == 'NEGATIVE' else ''
        number = int(''.join([NUM_CONST[i] for i in ws_int]), 2)
        return int('{}{}'.format(sign, number)) if signed else number

    def parse(self):
        for token in self.token_list:
            if token[1].type in HAS_ARGS:
                signed = True if token[1] is 'PUSH' else False
                int_value = self._get_value(token[2].value, signed=signed)
                self.method_map[token[0].type][token[1].type](int_value)
            else:
                self.method_map[token[0].type][token[1].type]()

    def clean(self):
        del self.stack
        del self.heap

