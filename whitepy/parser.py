from functools import partial
from .lexerconstants import HAS_ARGS, NUM_CONST, NUM_SIGN_CONST
from .stack import Stack
from .heap import Heap
from .ws_io import IO as ws_io
import sys


class Parser(object):
    def __init__(self, tokens):
        self.token_list = tokens
        self.stack = Stack()
        self.heap = Heap(self.stack)
        self.io = ws_io(self.stack)
        self.labels = self.create_labels()
        self.num_of_tokens = len(tokens)
        self.instruction_ptr = 0
        self.call_ptr = []
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
                'READ_NUM': partial(self.io.i_int, self.heap)
            },
            'FLOW_CONTROL': {
                'MARK': (lambda x: None),
                'CALL': partial(self.call_sub),
                'JUMP': partial(self.jump_loc),
                'JUMP_IF_ZERO': partial(self.jump_zero),
                'JUMP_IF_NEG': partial(self.jump_neg),
                'END_SUB': partial(self.end_sub),
                'END': self.end
            },
            'HEAP_ACCESS': {
                'STORE': partial(self.heap.set),
                'RETR': partial(self.heap.get)
            },
            'ARITHMETIC': {
                '+': self.stack.math.add,
                '-': self.stack.math.subtract,
                '*': self.stack.math.multiply,
                '/': self.stack.math.divide,
                '%': self.stack.math.modulo
            }
        }

    def _get_value(self, ws_int, signed=False):
        if signed:
            sign = '-' if NUM_SIGN_CONST[ws_int[0]] == 'NEGATIVE' else ''
            ws_int = ws_int[1:]
        number = int(''.join([NUM_CONST[i] for i in ws_int]), 2)
        return int('{}{}'.format(sign, number)) if signed else number

    def create_labels(self):
        labels = dict(
            (
                (
                    (self._get_value(t[2].value), idx) for
                    idx, t in enumerate(self.token_list)
                    if t[0].type == 'FLOW_CONTROL' and t[1].type == 'MARK'
                )
            )
        )
        return labels

    def call_sub(self, lbl):
        self.call_ptr.append(self.instruction_ptr)
        self.instruction_ptr = self.labels[lbl]

    def jump_loc(self, lbl):
        self.instruction_ptr = self.labels[lbl]

    def jump_zero(self, lbl):
        val = self.stack.pop()
        if val == 0:
            self.instruction_ptr = self.labels[lbl]
        else:
            pass

    def jump_neg(self, lbl):
        if self.stack.pop() < 0:
            self.instruction_ptr = self.labels[lbl]
        else:
            pass

    def end_sub(self):
        self.instruction_ptr = self.call_ptr.pop()

    def end(self):
        sys.exit(0)

    def parse(self):
        while self.instruction_ptr < self.num_of_tokens:
            token = self.token_list[self.instruction_ptr]
            if token[1].type in HAS_ARGS:
                signed = True if token[1].type is 'PUSH' else False
                int_value = self._get_value(token[2].value, signed=signed)
                self.method_map[token[0].type][token[1].type](int_value)
            else:
                self.method_map[token[0].type][token[1].type]()
            self.instruction_ptr += 1
