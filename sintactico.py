#Taller para crea un Analizador Sintactico
#Nombre: Bryan Plaza

import ply.yacc as yacc

from lexico import tokens

def p_expression_general(p):
    '''general : LPAREN expression RPAREN
            |    LPAREN comparacion RPAREN
            |    LPAREN sentenciaif RPAREN
            |    LPAREN asignacion RPAREN
            |    LPAREN imprimir RPAREN
            |    sentenciado
            |   read'''

def p_expression_mat(p):
    'expression : operadoresMat factor factor '

def p_comparacion(p):
    'comparacion : operadoresComp factor factor '

def p_operadoresMat(p):
    '''operadoresMat : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
                    | MOD'''

def p_operadoresComp(p):
    '''operadoresComp : MAYORQUE
                    | MENORQUE
                    | IGUAL
                    | OR
                    | AND
                    | NOT'''

def p_operadoresPrint(p):
    '''operadoresPrint : PRINT
                    | PRINTLN'''

def p_read(p):
    '''read : LPAREN READ RPAREN'''

def p_factor_num(p):
    '''factor : NUMBER
            |   ID
            |   booleanos'''
 
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'

def p_asignacion(p):
    '''asignacion : DEF ID factor
                |   DEF ID STRING
                |   DEF ID booleanos
                |   DEF ID struct'''


def p_booleanos(p):
    '''booleanos : TRUE
                |   FALSE'''

def p_imprimir(p):
    '''imprimir : operadoresPrint factor
                |   operadoresPrint STRING
                | PRINTF valorl'''

def p_sentenciado(p):
    'sentenciado : LPAREN DO general RPAREN'

def p_sentenciaif(p):
    '''sentenciaif : IF LPAREN comparacion RPAREN general
                |    IF LPAREN comparacion RPAREN sentenciado sentenciado'''

def p_struct(p):
    '''
      struct : lista
            |   vector
            |   mapa'''

def p_lista(p):
    'lista : QUOTE LPAREN valorl RPAREN'

def p_vector(p):
    'vector : LCOR valorl RCOR'

def p_mapa(p):
    'mapa : LBRACE repetirclave RBRACE'

def p_clavevalor(p):
    'clavevalor : ID DDOT valor '
def p_repetirclave(p):
    '''repetirclave : clavevalor
                    | clavevalor COMA repetirclave'''
def p_valor(p):
    '''valor : NUMBER
                    |   ID
                    |   STRING
                    |   booleanos'''

def p_valorl(p):
    '''valorl : NUMBER
                |   ID
                |   STRING
                |   booleanos
                | valorl valorl'''



# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
 
 # Build the parser
parser = yacc.yacc()
 
while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)

 