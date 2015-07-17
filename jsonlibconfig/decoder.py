from yacc import parser
from lex import hextoint


def load(f, _hextoint=False):
    s = ""
    for buff in f.read():
        s = s + buff
    return loads(s, _hextoint)


def loads(s, _hextoint=False):
    hextoint(_hextoint)
    return parser.parse(s)
