"""
Author : Ruchitesh Malukani
Aim : Create interpreter for new language named 'prime' ( OPEN ENDED PROBLEM )
"""
from sly import Lexer


class primeLexer(Lexer):
    tokens = {NAME, NUMBER, STRING, IF, THEN, ELSE ,FOR, FUN, TO, ARROW, EQEQ}
