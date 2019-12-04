import ply.lex as lex


_hextoint = False

tokens = (
    "COLON",
    "EQUAL",
    "SEMICOLON",
    "COMMA",
    "LBRACE",
    "RBRACE",
    "LPAREN",
    "RPAREN",
    "LSQUARE",
    "RSQUARE",
    "COMMENT",
    "INTEGER",
    "INTEGER64",
    "BOOLEAN",
    "HEX",
    "HEX64",
    "FLOAT",
    "STRING",
    "NAME"
)


def t_BOOLEAN(t):
    r"([Tt][Rr][Uu][Ee])|([Ff][Aa][Ll][Ss][Ee])"
    t.value = False if t.value.lower() == 'false' else True
    return t


def t_HEX64(t):
    r"0[Xx][0-9A-Fa-f]+(L(L)?)?"
    if _hextoint:
        t.value = int(t.value, 0)
    return t


def t_HEX(t):
    r"0[Xx][0-9A-Fa-f]+"
    if _hextoint:
        print("to int")
        t.value = int(t.value, 0)
    print("not to int")
    return t


def t_FLOAT(t):
    r"([-+]?([0-9]*)?\.[0-9]*([eE][-+]?[0-9]+)?)|([-+]([0-9]+)(\.[0-9]*)?[eE][-+]?[0-9]+)"  # noqa: E501
    t.value = float(t.value)
    return t


def t_INTEGER64(t):
    r"[-+]?[0-9]+L(L)?"
    t.value = int(t.value[:-1])
    return t


def t_INTEGER(t):
    r"[-+]?[0-9]+"
    t.value = int(t.value)
    return t


def t_STRING(t):
    r"\"([^\"\\]|\\.)*\""
    t.value = t.value[1:-1]
    return t


t_NAME = r"[A-Za-z\*][-A-Za-z0-9_\*]*"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LSQUARE = r"\["
t_RSQUARE = r"\]"
t_COMMA = r","
t_COLON = r":"
t_EQUAL = r"="
t_SEMICOLON = r";"
t_ignore = ' \t'


def t_COMMENT(t):
    r'\#.*|\/\/.*'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))


def hextoint(b=True):
    global _hextoint
    _hextoint = b


lex.lex(debug=0)
