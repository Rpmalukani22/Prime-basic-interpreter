"""
Author : Ruchitesh Malukani
Aim : Create interpreter for new language named 'prime' ( OPEN ENDED PROBLEM )
"""
from sly import Lexer


class primeLexer(Lexer):
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


