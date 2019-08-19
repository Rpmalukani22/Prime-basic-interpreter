"""
Author : Ruchitesh Malukani
Aim : Create interpreter for new language named 'prime' ( OPEN ENDED PROBLEM )
"""
from sly import Lexer


class PrimeLexer(Lexer):
    tokens = {NAME, NUMBER, STRING, IF, THEN, ELSE ,FOR, FUN, TO, ARROW, EQEQ}
    ignore='\t'

    # Token definition
    IF = r'PRIME_IF'
    THEN = r'THEN'
    ELSE = r'ELSE'
    FOR = r'PRIME_FOR'
    FUN = r'PRIME_FUN'
    TO = r'TO'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    EQEQ = r'=='

    #literals
    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';'}

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')


if __name__ == '__main__':
    lexer = PrimeLexer()
    env = {}
    while True:
        try:
            text = input('Prime > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
