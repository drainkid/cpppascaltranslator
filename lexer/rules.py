from tokenType import Symbol,Terminal,tokenType

import re

LEXER_REGEX_FLAGS = re.IGNORECASE

class Special(Symbol):
    LAMBDA = '__LAMBDA__'

class val(Terminal):
    ID = 'id'
    NUMBER_INT = 'number_int'
    NUMBER_FLOAT = 'number_float'
    LBRACKET = 'lbracket'
    RBRACKET = 'rbracket'
    LBRACKET_SQUARE = 'lbracket_square'
    RBRACKET_SQUARE = 'rbracket_square'
    RBRACKET_CURLY = 'rbracket_curly'
    LBRACKET_CURLY = 'lbracket_curly'
    SEMICOLON = 'semicolon'
    COLON = 'colon'
    STD = 'std'
    COMMA = 'comma'
    DOT = 'dot'
    CHAR = 'char'
    TYPE_HINT = 'type_hint'
    COMPARE = 'compare'
    MATH_OPERATOR = 'math_operator'
    BOOLEAN_OPERATOR = 'boolean_operator'
    BOOLEAN_NOT = 'boolean_not'
    ASSIGN = 'assign'
    OP_ASSIGN = 'op_assign'
    BOOLEAN_VALUE = 'boolean_value'
    WHITESPACE = 'whitespace'

    IF = 'if'
    ELSE = 'else'
    FOR = 'for'
    WHILE = 'while'
    DO = 'do'
    MAX = 'max'
    MIN = 'min'
    STATIC = 'static'
    CLASS = 'class'
    PUBLIC = 'public'
    MAIN = 'main'
    INCREMENT = 'increment'
    VOID = 'void'
    STRING = 'string_args'
    RETURN = 'return'
    PROCEDURE = 'procedure'
    FUNCTION = 'function'
    COUT = 'cout'
    VALUE = 'value'
    QUOTE = 'quote'
    QUOTE2 ='quote2'
    CIN ='cin'
    ID2 = 'id2'

    ONE_LINE_COMMENT = '__ONE_LINE_COMMENT__'
    MULTI_LINE_COMMENT = '__MULTI_LINE_COMMENT__'

typeList = [
        tokenType(val.WHITESPACE, r'\s'),
        tokenType(val.ONE_LINE_COMMENT, r'//.*\n'),
        tokenType(val.TYPE_HINT, r'\bint|boolean|float|double|char\b'),
        tokenType(val.STRING, r'\bString\[\]\sargs\b'),
        tokenType(val.RETURN, r'\breturn\b'),
        tokenType(val.INCREMENT, r'\+\+|\-\-'),
        tokenType(val.IF, r'\bif\b'),
        tokenType(val.ELSE, r'\belse\b'),
        tokenType(val.MATH_OPERATOR, r'\+|\-|\*|/'),
        tokenType(val.NUMBER_INT, r'[\-\+]?\d+'),
        tokenType(val.NUMBER_FLOAT, r'[\-\+]?\d+\.\d+'),

        tokenType(val.FOR, r'\bfor\b'),
        tokenType(val.WHILE, r'\bwhile\b'),

        tokenType(val.LBRACKET, r'\('),
        tokenType(val.RBRACKET, r'\)'),
        tokenType(val.LBRACKET_SQUARE,r'\['),
        tokenType(val.RBRACKET_SQUARE,r'\]'),
        tokenType(val.LBRACKET_CURLY, r'\{'),
        tokenType(val.RBRACKET_CURLY, r'\}'),
        tokenType(val.SEMICOLON, r';'),
        tokenType(val.COLON, r':'),
        tokenType(val.COMMA, r','),
        tokenType(val.DOT, r'\.'),
        tokenType(val.CHAR, r"\'.\'"),
        tokenType(val.QUOTE, r"\""),
        tokenType(val.QUOTE2, r"\'"),

        tokenType(val.COMPARE, r'=|\<\>|\<=|\<|\>=|\>'),
        tokenType(val.BOOLEAN_VALUE, r'\band|or|xor\b'),
        tokenType(val.VOID, r'\bvoid\b'),
        tokenType(val.MAIN, r'\bmain\b'),
        tokenType(val.STATIC, r'\bstatic\b'),
        tokenType(val.STD, r'\bstd\b'),
        tokenType(val.COUT,  r'\bcout\b'),
        tokenType(val.VALUE, r'"\[a-z]\"'),
        tokenType(val.CIN, r'\bcin\b'),

    tokenType(val.ID, r'\b[_a-zA-Z]\w*\b')
    ]