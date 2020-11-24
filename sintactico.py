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
            |    sentenciado'''

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
                    | IGUAL'''

def p_operadoresPrint(p):
    '''operadoresPrint : PRINT
                    | PRINTLN'''

 
def p_factor_num(p):
    '''factor : NUMBER
            |   ID'''
 
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'

def p_asignacion(p):
    '''asignacion : DEF ID factor
                |   DEF ID STRING'''

def p_imprimir(p):
    '''imprimir : operadoresPrint factor
                |   operadoresPrint STRING'''

def p_sentenciado(p):
    'sentenciado : LPAREN DO general RPAREN'

def p_sentenciaif(p):
    '''sentenciaif : IF LPAREN comparacion RPAREN general
                |    IF LPAREN comparacion RPAREN sentenciado sentenciado'''

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

 