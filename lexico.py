 # ------------------------------------------------------------
 # Grupo Clojure 1
 # ------------------------------------------------------------

import ply.lex as lex

reserved = {
    'if' : 'IF',
    'when' : 'THEN',
    'for' : 'FOR',
    'def':'DEF',
    'and' : 'AND',
    'not' : 'NOT',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'or' : 'OR',
    'while': 'WHILE',
    'do': 'DO',
    'str': 'STR',
    'count': 'COUNT',
    'pop': 'POP',
    'get': 'GET',
    'conj': 'CONJ',
    'nth': 'NTH',
    'defn': 'DEFN',
    'printf': 'PRINTF',
    'print': 'PRINT',
    'println' : 'PRINTLN',
    'read': 'READ',
    'mod' : 'MOD',
    'comment' : 'COMMENT'
}

tokens = (
    'NUMBER',
    'FLOAT',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LCOR',
    'RCOR',
    'LBRACE',
    'RBRACE',
    'DDOT',
    'MAYORQUE',
    'MENORQUE',
    'NUMERAL',
    'IGUAL',
    'QUOTE',
    'COMA',
    'ID'
 ) + tuple(reserved.values())


t_MINUS   = r'-'
t_COMA    = r','
t_QUOTE   = r'\''
t_PLUS    = r'\+'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LCOR  = r'\['
t_RCOR  = r'\]'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_IGUAL = r'='
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DDOT = r':'
t_NUMERAL = r'\#'

def t_FLOAT(t):
    r'[-+]?(\d+(\.\d*)|\.\d+)'
    t.value = float(t.value)
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_\%0-9]*'
    t.type = reserved.get(t.value,'ID')    
    return t

def t_STRING(t):
    r'"[a-zA-Z_0-9\s]*"'
    t.value = str(t.value)    
    return t


t_ignore  = ' \t'
 
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

'''
lexer = lex.lex()
 


archivo = open("codigo.txt", 'r',  encoding="utf-8")

contenido = archivo.read()

archivo.close()

 # Give the lexer some input
lexer.input(contenido)

 # Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
'''


def verLexer(data):
    lexer = lex.lex()
    lexer.input(data)

    while True:
        tok= lexer.token()
        if not tok:

            break
        print(tok)




