#Taller para crea un Analizador Sintactico
#Nombre: Bryan Plaza

import ply.yacc as yacc

from lexico import tokens

def p_expression_general(p):
    '''general : LPAREN expression RPAREN
            | LPAREN comparacion RPAREN
            | LPAREN sentenciaif RPAREN
            | LPAREN sentenciawhile RPAREN
            | LPAREN asignacion RPAREN
            | LPAREN imprimir RPAREN
            | LPAREN asignacion_funcion RPAREN
            | funcionstruct
            | sentenciado
            | read
            | general general'''

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
            | FLOAT
            |   booleanos'''
 
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'

def p_asignacion(p):
    '''asignacion : DEF ID factor
                |   DEF ID STRING
                |   DEF ID struct
                |   DEF ID funcionstruct
                | DEF ID read'''


def p_booleanos(p):
    '''booleanos : TRUE
        | FALSE
    '''

def p_imprimir(p):
    '''imprimir : operadoresPrint factor
                |   operadoresPrint STRING
                | PRINTF valorl'''

def p_sentenciado(p):
    'sentenciado : LPAREN DO general RPAREN'

def p_sentenciaif(p):
    '''sentenciaif : IF LPAREN comparacion RPAREN general
                |    IF LPAREN comparacion RPAREN sentenciado sentenciado'''

#CARLOS SALAZAR
def p_sentenciawhile(p):
    '''
        sentenciawhile : WHILE LPAREN comparacion RPAREN sentenciado
    '''
def p_struct(p):
    '''
      struct : lista
            |   vector
            |   mapa
            | conjunto'''

def p_lista(p):
    'lista : QUOTE LPAREN valorl RPAREN'

def p_vector(p):
    'vector : LCOR valorl RCOR'

def p_mapa(p):
    'mapa : LBRACE repetirclave RBRACE'

def p_conjunto(p):
    'conjunto : NUMERAL LBRACE valorl RBRACE'

def p_clavevalor(p):
    'clavevalor : ID DDOT valor '

def p_repetirclave(p):
    '''repetirclave : clavevalor
                    | clavevalor COMA repetirclave'''
def p_valor(p):
    '''valor : NUMBER
                    |   ID
                    |   STRING
                    |   booleanos
                    | FLOAT'''

def p_valorl(p):
    '''valorl : NUMBER
                |   ID
                |   STRING
                |   booleanos
                | FLOAT
                | valorl valorl'''
#CARLOS SALAZAR
def p_funcionstruct(p):
    '''
        funcionstruct : conjfunction
        | LPAREN STR STRING strings RPAREN
        | LPAREN STR ID strings RPAREN
        | LPAREN GET conjunto NUMBER RPAREN
        | LPAREN GET conjunto ID RPAREN
        | LPAREN NTH lista NUMBER RPAREN
        | LPAREN NTH lista ID RPAREN
        | LPAREN POP vector RPAREN
        | LPAREN COUNT STRING RPAREN
        | LPAREN COUNT ID RPAREN
    '''

# Carlos Salazar
def p_conjfunction(p):
    '''
        conjfunction : LPAREN CONJ lista NUMBER RPAREN
        | LPAREN CONJ lista ID RPAREN
        | LPAREN CONJ conjunto NUMBER RPAREN
        | LPAREN CONJ conjunto ID RPAREN
        | LPAREN CONJ vector NUMBER RPAREN
        | LPAREN CONJ vector ID RPAREN
    '''
def p_strings(p):
    '''
        strings : valor_strings
        | valor_strings strings
    '''
# Carlos Salazar
def p_valor_strings(p):
    '''
        valor_strings : STRING
        | ID
    '''


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input! %s" % p.value)


def p_asignacion_funcion(p):
    '''
        asignacion_funcion : DEFN ID LCOR RCOR general
        | DEFN ID LCOR parametros RCOR general
    '''


def p_parametros(p):
    '''
        parametros : valores
    '''


def p_valores(p):
    '''
        valores : ID
        | ID valores
    '''



 # Build the parser
parser = yacc.yacc()
 
while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)

 