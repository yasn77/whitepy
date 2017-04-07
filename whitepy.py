#!/usr/bin/env python

import whitepy.lexer as lexer
from whitepy.lexerconstants import *

import pprint
pp = pprint.PrettyPrinter(width=41, depth=2, compact=True)


with open('./helloworld.ws', 'r') as f:
    lines = f.read()

item = lexer.Lexer(line=lines)
item.get_all_tokens()
index = 0
for i in item.tokens:
    index += 1
    print(index)
    pp.pprint([x.type if type(x) == "Token" else x for x in i])
