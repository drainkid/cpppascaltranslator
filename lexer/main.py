from lexer import lexer
from pathlib import Path

code = Path('input.cpp').read_text()


#
lex = lexer(code)
lex.lexAnalysis()

huy = lex.tokenList
for i in huy:
    print(i)

# print(code)