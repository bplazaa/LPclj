#Taller para crea un Analizador Sintactico
#Nombre: Bryan Plaza

import ply.yacc as yacc

from lexico import tokens

def p_expression_suma(p):
    'expression : PLUS term term'
    for i in p:
        print(i)
    p[0] = p[2] + p[3]
 
def p_expression_resta(p):
    'expression : expression MINUS term'
    for i in p:
        print(i)
    p[0] = p[1] - p[3]
 
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_operadoresMat(p):
    '''operadoresMat : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE'''

def p_term_producto(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]
 
def p_term_divi(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_valor(p):
    '''valor : NUMBER
             | ID'''

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
 
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]
 
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

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
   print(result)
 