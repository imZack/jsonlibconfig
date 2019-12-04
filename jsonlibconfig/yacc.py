from __future__ import absolute_import

import ply.yacc as yacc
from jsonlibconfig.lex import tokens  # noqa: F401


# configuration = setting-list | empty
def p_configuration(p):
    '''CONFIGURATION : SETTING_LIST
                     | EMPTY'''
    p[0] = p[1]
###############################################################################


# setting-list = setting | setting-list setting
def p_setting_list(p):
    '''SETTING_LIST : SETTING
                    | SETTING_LIST SETTING'''
    if len(p) > 2:
        p[1].update(p[2])
    p[0] = p[1]
###############################################################################


# setting = name (":" | "=") value (";" | "," | empty)
def p_setting(p):
    '''SETTING : NAME COLON VALUE SEMICOLON
               | NAME COLON VALUE COMMA
               | NAME COLON VALUE EMPTY
               | NAME EQUAL VALUE SEMICOLON
               | NAME EQUAL VALUE COMMA
               | NAME EQUAL VALUE EMPTY'''
    p[0] = {}
    p[0][p[1]] = p[3]
###############################################################################


# group = "{" (setting-list | empty) "}"
def p_group(p):
    '''GROUP : LBRACE SETTING_LIST RBRACE
             | LBRACE EMPTY RBRACE'''
    if p.slice[2].type == 'SETTING_LIST':
        p[0] = p[2]
    else:
        p[0] = {}

###############################################################################


# list = "(" (value-list | empty) ")"
def p_list(p):
    '''LIST : LPAREN VALUE_LIST RPAREN
            | LPAREN EMPTY RPAREN'''
    p[0] = p[2] if p[2] is not None else []
###############################################################################


# array = "[" (scalar-value-list | empty) "]"
def p_array(p):
    '''ARRAY : LSQUARE SCALAR_VALUE_LIST RSQUARE
             | EMPTY'''
    if len(p) >= 3:
        p[0] = p[2]
    else:
        p[0] = []
###############################################################################


def p_empty(p):
    'EMPTY : '
    p[0] = "empty"


# value-list = value | value-list "," value
def p_value_list(p):
    '''VALUE_LIST : VALUE
                  | VALUE_LIST COMMA VALUE'''
    if len(p) > 2:
        if isinstance(p[1], list):
            p[1].append(p[3])
            p[0] = p[1]
        else:
            lst = [p[1], p[3]]
            p[0] = lst
    else:
        p[0] = p[1]
###############################################################################


# value = scalar-value | array | list | group
def p_value_scalar_value(p):
    '''VALUE : SCALAR_VALUE
             | ARRAY
             | LIST
             | GROUP'''
    p[0] = p[1]
###############################################################################


# scalar-value-list = scalar-value | scalar-value-list "," scalar-value
def p_scalar_value_list(p):
    '''SCALAR_VALUE_LIST : SCALAR_VALUE
                         | SCALAR_VALUE_LIST COMMA SCALAR_VALUE'''
    if len(p) > 2:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]
###############################################################################


# scalar-value = boolean | integer | integer64 | hex | hex64 | float | string
def p_scalar_value(p):
    '''SCALAR_VALUE : BOOLEAN
                    | INTEGER
                    | INTEGER64
                    | HEX
                    | HEX64
                    | FLOAT
                    | STRING'''
    p[0] = p[1]
###############################################################################


def p_error(p):
    print(p)
    print(p.type)
    print("Syntax error in input!")


parser = yacc.yacc()
