#!/usr/bin/env python

import whitepy.lexer as lexer
import whitepy.parser as ws_parser
from whitepy.lexerconstants import *

import pprint
pp = pprint.PrettyPrinter(width=41, depth=2, compact=True)


#with open('./count.ws', 'r') as f:
with open('./helloworld.ws', 'r') as f:
    lines = f.read()

item = lexer.Lexer(line=lines, debug=True)
item.get_all_tokens()
p = ws_parser.Parser(item.tokens)
p.parse()
#index = 0
#for i in item.tokens:
#    index += 1
#    pp.pprint([x.type if type(x) == "Token" else x for x in i])
