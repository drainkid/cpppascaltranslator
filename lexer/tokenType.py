from enum import Enum

class tokenType:
    def __init__(self, name:Enum, regex) -> None:
        self.name = name # название
        self.regex: str = regex # регулярка

class Symbol(Enum):
    def __repr__(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)

class Terminal(Symbol):
    pass

class token:
    def __init__(self, val, text, pos, line):
        self.val: Symbol = val # тип токена
        self.text: str = text # значение
        self.pos: int = pos
        self.line: int = line

    def __str__(self):
        return str(self.val) + ' | ' + str(self.text) + ' |Позиция: ' +  str(self.pos) + '  строка:' + str(self.line)

    # def __repr__(self):
    #     return str(self.val) + ' ' + str(self.text)
