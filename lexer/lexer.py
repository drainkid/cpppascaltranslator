from tokenType import token
from rules import typeList, LEXER_REGEX_FLAGS,Special,Terminal
import re
import enum

class TranspilerError(Exception):
    pass


class LexerError(TranspilerError):
    pass


class UnexpectedTokenError(LexerError):
    pass



class lexer:
    def __init__(self, code:str):
        self.code = code
    pos: int = 0
    tokenList = list()

    def lexAnalysis(self):
        while self.nextToken():
            pass
        self.tokenList = [token for token in self.tokenList if token.val != typeList[0].name]
        return self.tokenList

    def nextToken(self) -> bool:
        if self.pos >= len(self.code):
            return False
        tokenTypeValues = typeList
        for i in range(len(tokenTypeValues)):
            toType = tokenTypeValues[i]
            regex = re.compile('^' + toType.regex,LEXER_REGEX_FLAGS)
            result = self.code[self.pos:]
            res = re.match(regex,result)
            def _get_line(self):
                return result.count('\n', 0, self.pos) + 1
            if res and res[0]:
                res.group()
                tok = token(toType.name, res[0], self.pos, _get_line(self))
                self.pos += len(res[0])
                self.tokenList.append(tok)
                return True
        raise UnexpectedTokenError