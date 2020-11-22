#Taller para crea un Analizador Sintactico
#Nombre: Bryan Plaza

import ply.yacc as yacc

from lexico import tokens

def p_expression_suma(p):
    'expression : PLUS factor factor'
 
def p_expression_resta(p):
    'expression : MINUS factor factor'
     
def p_expression_term(p):
    'expression : term'

def p_operadoresMat(p):
    '''operadoresMat : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE'''

def p_term_producto(p):
    'term : TIMES factor factor'
 
def p_term_divi(p):
    'term : DIVIDE factor factor'

def p_valor(p):
    '''valor : NUMBER
             | ID'''

def p_term_factor(p):
    'term : factor'
 
def p_factor_num(p):
    'factor : NUMBER'
 
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'

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

 