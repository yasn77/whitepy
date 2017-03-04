#!/usr/bin/env python

import whitepy.lexer as lexer

line = "   \t\n"
item = lexer.Lexer(line=line)
item.get_all_tokens()
print("{}".format(item.tokens))
