
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND COMA COMMENT CONJ COUNT DDOT DEF DEFN DIVIDE DO FALSE FLOAT FOR GET ID IF IGUAL LBRACE LCOR LPAREN MAYORQUE MENORQUE MINUS MOD NOT NTH NUMBER NUMERAL OR PLUS POP PRINT PRINTF PRINTLN QUOTE RBRACE RCOR READ READLINE RPAREN STR STRING THEN TIMES TRUE WHILEgeneral : LPAREN expression RPAREN\n            |    LPAREN comparacion RPAREN\n            |    LPAREN sentenciaif RPAREN\n            |    LPAREN sentenciawhile RPAREN\n            |    LPAREN asignacion RPAREN\n            |    LPAREN imprimir RPAREN\n            |    funcionstruct\n            |    sentenciado\n            |   read\n            | general generalexpression : operadoresMat factor factor comparacion : operadoresComp factor factor operadoresMat : PLUS\n                    | MINUS\n                    | TIMES\n                    | DIVIDE\n                    | MODoperadoresComp : MAYORQUE\n                    | MENORQUE\n                    | IGUAL\n                    | OR\n                    | AND\n                    | NOToperadoresPrint : PRINT\n                    | PRINTLNread : LPAREN READ RPARENfactor : NUMBER\n            |   ID\n            | FLOAT\n            |   booleanosfactor : LPAREN expression RPARENasignacion : DEF ID factor\n                |   DEF ID STRING\n                |   DEF ID booleanos\n                |   DEF ID struct\n                |   DEF ID funcionstructbooleanos : TRUE\n                |   FALSEimprimir : operadoresPrint factor\n                |   operadoresPrint STRING\n                | PRINTF valorlsentenciado : LPAREN DO general RPARENsentenciaif : IF LPAREN comparacion RPAREN general\n                |    IF LPAREN comparacion RPAREN sentenciado sentenciado\n        sentenciawhile : WHILE LPAREN comparacion RPAREN sentenciado\n    \n      struct : lista\n            |   vector\n            |   mapa\n            | conjuntolista : QUOTE LPAREN valorl RPARENvector : LCOR valorl RCORmapa : LBRACE repetirclave RBRACEconjunto : NUMERAL LBRACE valorl RBRACEclavevalor : ID DDOT valor repetirclave : clavevalor\n                    | clavevalor COMA repetirclavevalor : NUMBER\n                    |   ID\n                    |   STRING\n                    |   booleanos\n                    | FLOATvalorl : NUMBER\n                |   ID\n                |   STRING\n                |   booleanos\n                | FLOAT\n                | valorl valorl\n        funcionstruct : conjfunction\n        | LPAREN STR STRING strings RPAREN\n        | LPAREN GET conjunto NUMBER RPAREN\n        | LPAREN GET conjunto ID RPAREN\n        | LPAREN NTH lista NUMBER RPAREN\n        | LPAREN NTH lista ID RPAREN\n        | LPAREN POP vector RPAREN\n        | LPAREN COUNT STRING RPAREN\n        | LPAREN COUNT ID RPAREN\n    \n        conjfunction : LPAREN CONJ lista NUMBER RPAREN\n        | LPAREN CONJ lista ID RPAREN\n        | LPAREN CONJ conjunto NUMBER RPAREN\n        | LPAREN CONJ conjunto ID RPAREN\n        | LPAREN CONJ vector NUMBER RPAREN\n        | LPAREN CONJ vector ID RPAREN\n    \n        strings : STRING\n        | STRING STRING\n    '
    
_lr_action_items = {'LPAREN':([0,1,3,4,5,6,7,19,22,23,24,25,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,52,57,58,62,63,64,65,66,68,69,70,73,90,92,93,94,119,120,121,123,124,127,128,129,130,131,132,133,134,135,142,143,],[2,2,-7,-8,-9,-68,2,2,67,67,71,72,67,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-1,-2,-3,-4,-5,-6,89,2,-26,67,-27,-28,-29,-30,-37,-38,67,111,-74,-75,-76,-42,-69,-70,-71,-72,-73,-77,-78,-79,-80,-81,-82,-31,141,144,2,144,]),'$end':([1,3,4,5,6,7,42,43,44,45,46,47,58,90,92,93,94,119,120,121,123,124,127,128,129,130,131,132,],[0,-7,-8,-9,-68,-10,-1,-2,-3,-4,-5,-6,-26,-74,-75,-76,-42,-69,-70,-71,-72,-73,-77,-78,-79,-80,-81,-82,]),'STR':([2,111,141,],[14,14,14,]),'GET':([2,111,141,],[15,15,15,]),'NTH':([2,111,141,],[16,16,16,]),'POP':([2,111,141,],[17,17,17,]),'COUNT':([2,111,141,],[18,18,18,]),'DO':([2,141,144,],[19,19,19,]),'READ':([2,141,],[20,20,]),'CONJ':([2,111,141,],[21,21,21,]),'IF':([2,141,],[24,24,]),'WHILE':([2,141,],[25,25,]),'DEF':([2,141,],[26,26,]),'PRINTF':([2,141,],[28,28,]),'PLUS':([2,67,111,141,],[29,29,29,29,]),'MINUS':([2,67,111,141,],[30,30,30,30,]),'TIMES':([2,67,111,141,],[31,31,31,31,]),'DIVIDE':([2,67,111,141,],[32,32,32,32,]),'MOD':([2,67,111,141,],[33,33,33,33,]),'MAYORQUE':([2,71,72,141,],[34,34,34,34,]),'MENORQUE':([2,71,72,141,],[35,35,35,35,]),'IGUAL':([2,71,72,141,],[36,36,36,36,]),'OR':([2,71,72,141,],[37,37,37,37,]),'AND':([2,71,72,141,],[38,38,38,38,]),'NOT':([2,71,72,141,],[39,39,39,39,]),'PRINT':([2,141,],[40,40,]),'PRINTLN':([2,141,],[41,41,]),'RPAREN':([3,4,5,6,7,8,9,10,11,12,13,20,42,43,44,45,46,47,53,55,56,57,58,63,64,65,66,68,69,74,75,76,77,78,79,80,81,82,83,84,85,87,88,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,133,139,140,142,143,145,146,149,],[-7,-8,-9,-68,-10,42,43,44,45,46,47,58,-1,-2,-3,-4,-5,-6,90,92,93,94,-26,-27,-28,-29,-30,-37,-38,-39,-40,-41,-62,-63,-64,-65,-66,-83,119,120,121,123,124,-74,-75,-76,-42,127,128,129,130,131,132,-11,133,-12,134,135,-32,-33,-30,-35,-36,-46,-47,-48,-49,-67,-84,-69,-70,-71,-72,-73,140,-51,-77,-78,-79,-80,-81,-82,-31,-53,-50,-43,-8,-45,-52,-44,]),'STRING':([14,18,27,28,40,41,48,54,68,69,73,76,77,78,79,80,81,82,86,89,91,117,122,125,148,],[48,55,75,79,-24,-25,82,79,-37,-38,107,79,-62,-63,-64,-65,-66,118,79,79,79,79,79,79,154,]),'NUMERAL':([15,21,73,],[50,50,50,]),'QUOTE':([16,21,73,],[52,52,52,]),'LCOR':([17,21,73,],[54,54,54,]),'ID':([18,22,23,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,49,51,54,59,60,61,62,63,64,65,66,68,69,70,73,76,77,78,79,80,81,86,89,91,116,117,122,125,126,133,139,140,147,148,],[56,64,64,73,64,78,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,85,88,78,96,98,100,64,-27,-28,-29,-30,-37,-38,64,64,78,-62,-63,-64,-65,-66,78,78,78,138,78,78,78,-51,-31,-53,-50,138,151,]),'NUMBER':([22,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,49,51,54,59,60,61,62,63,64,65,66,68,69,70,73,76,77,78,79,80,81,86,89,91,117,122,125,126,133,139,140,148,],[63,63,63,77,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,84,87,77,95,97,99,63,-27,-28,-29,-30,-37,-38,63,63,77,-62,-63,-64,-65,-66,77,77,77,77,77,77,-51,-31,-53,-50,153,]),'FLOAT':([22,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,54,62,63,64,65,66,68,69,70,73,76,77,78,79,80,81,86,89,91,117,122,125,133,148,],[65,65,65,81,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,81,65,-27,-28,-29,-30,-37,-38,65,65,81,-62,-63,-64,-65,-66,81,81,81,81,81,81,-31,156,]),'TRUE':([22,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,54,62,63,64,65,66,68,69,70,73,76,77,78,79,80,81,86,89,91,117,122,125,133,148,],[68,68,68,68,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,68,68,-27,-28,-29,-30,-37,-38,68,68,68,-62,-63,-64,-65,-66,68,68,68,68,68,68,-31,68,]),'FALSE':([22,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,54,62,63,64,65,66,68,69,70,73,76,77,78,79,80,81,86,89,91,117,122,125,133,148,],[69,69,69,69,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,69,69,-27,-28,-29,-30,-37,-38,69,69,69,-62,-63,-64,-65,-66,69,69,69,69,69,69,-31,69,]),'LBRACE':([50,73,],[86,116,]),'RCOR':([68,69,77,78,79,80,81,91,117,],[-37,-38,-62,-63,-64,-65,-66,126,-67,]),'RBRACE':([68,69,77,78,79,80,81,117,122,136,137,150,151,152,153,154,155,156,],[-37,-38,-62,-63,-64,-65,-66,-67,139,146,-55,-56,-58,-54,-57,-59,-60,-61,]),'COMA':([68,69,137,151,152,153,154,155,156,],[-37,-38,147,-58,-54,-57,-59,-60,-61,]),'DDOT':([138,],[148,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'general':([0,1,7,19,57,134,142,],[1,7,7,57,7,142,7,]),'funcionstruct':([0,1,7,19,57,73,134,142,],[3,3,3,3,3,110,3,3,]),'sentenciado':([0,1,7,19,57,134,135,142,143,],[4,4,4,4,4,143,145,4,149,]),'read':([0,1,7,19,57,134,142,],[5,5,5,5,5,5,5,]),'conjfunction':([0,1,7,19,57,73,134,142,],[6,6,6,6,6,6,6,6,]),'expression':([2,67,111,141,],[8,102,102,8,]),'comparacion':([2,71,72,141,],[9,104,105,9,]),'sentenciaif':([2,141,],[10,10,]),'sentenciawhile':([2,141,],[11,11,]),'asignacion':([2,141,],[12,12,]),'imprimir':([2,141,],[13,13,]),'operadoresMat':([2,67,111,141,],[22,22,22,22,]),'operadoresComp':([2,71,72,141,],[23,23,23,23,]),'operadoresPrint':([2,141,],[27,27,]),'conjunto':([15,21,73,],[49,60,115,]),'lista':([16,21,73,],[51,59,112,]),'vector':([17,21,73,],[53,61,113,]),'factor':([22,23,27,62,70,73,],[62,70,74,101,103,106,]),'booleanos':([22,23,27,28,54,62,70,73,76,86,89,91,117,122,125,148,],[66,66,66,80,80,66,66,108,80,80,80,80,80,80,80,155,]),'valorl':([28,54,76,86,89,91,117,122,125,],[76,91,117,122,125,117,117,117,117,]),'strings':([48,],[83,]),'struct':([73,],[109,]),'mapa':([73,],[114,]),'repetirclave':([116,147,],[136,150,]),'clavevalor':([116,147,],[137,137,]),'valor':([148,],[152,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> general","S'",1,None,None,None),
  ('general -> LPAREN expression RPAREN','general',3,'p_expression_general','sintactico.py',9),
  ('general -> LPAREN comparacion RPAREN','general',3,'p_expression_general','sintactico.py',10),
  ('general -> LPAREN sentenciaif RPAREN','general',3,'p_expression_general','sintactico.py',11),
  ('general -> LPAREN sentenciawhile RPAREN','general',3,'p_expression_general','sintactico.py',12),
  ('general -> LPAREN asignacion RPAREN','general',3,'p_expression_general','sintactico.py',13),
  ('general -> LPAREN imprimir RPAREN','general',3,'p_expression_general','sintactico.py',14),
  ('general -> funcionstruct','general',1,'p_expression_general','sintactico.py',15),
  ('general -> sentenciado','general',1,'p_expression_general','sintactico.py',16),
  ('general -> read','general',1,'p_expression_general','sintactico.py',17),
  ('general -> general general','general',2,'p_expression_general','sintactico.py',18),
  ('expression -> operadoresMat factor factor','expression',3,'p_expression_mat','sintactico.py',21),
  ('comparacion -> operadoresComp factor factor','comparacion',3,'p_comparacion','sintactico.py',24),
  ('operadoresMat -> PLUS','operadoresMat',1,'p_operadoresMat','sintactico.py',27),
  ('operadoresMat -> MINUS','operadoresMat',1,'p_operadoresMat','sintactico.py',28),
  ('operadoresMat -> TIMES','operadoresMat',1,'p_operadoresMat','sintactico.py',29),
  ('operadoresMat -> DIVIDE','operadoresMat',1,'p_operadoresMat','sintactico.py',30),
  ('operadoresMat -> MOD','operadoresMat',1,'p_operadoresMat','sintactico.py',31),
  ('operadoresComp -> MAYORQUE','operadoresComp',1,'p_operadoresComp','sintactico.py',34),
  ('operadoresComp -> MENORQUE','operadoresComp',1,'p_operadoresComp','sintactico.py',35),
  ('operadoresComp -> IGUAL','operadoresComp',1,'p_operadoresComp','sintactico.py',36),
  ('operadoresComp -> OR','operadoresComp',1,'p_operadoresComp','sintactico.py',37),
  ('operadoresComp -> AND','operadoresComp',1,'p_operadoresComp','sintactico.py',38),
  ('operadoresComp -> NOT','operadoresComp',1,'p_operadoresComp','sintactico.py',39),
  ('operadoresPrint -> PRINT','operadoresPrint',1,'p_operadoresPrint','sintactico.py',42),
  ('operadoresPrint -> PRINTLN','operadoresPrint',1,'p_operadoresPrint','sintactico.py',43),
  ('read -> LPAREN READ RPAREN','read',3,'p_read','sintactico.py',46),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintactico.py',49),
  ('factor -> ID','factor',1,'p_factor_num','sintactico.py',50),
  ('factor -> FLOAT','factor',1,'p_factor_num','sintactico.py',51),
  ('factor -> booleanos','factor',1,'p_factor_num','sintactico.py',52),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','sintactico.py',55),
  ('asignacion -> DEF ID factor','asignacion',3,'p_asignacion','sintactico.py',58),
  ('asignacion -> DEF ID STRING','asignacion',3,'p_asignacion','sintactico.py',59),
  ('asignacion -> DEF ID booleanos','asignacion',3,'p_asignacion','sintactico.py',60),
  ('asignacion -> DEF ID struct','asignacion',3,'p_asignacion','sintactico.py',61),
  ('asignacion -> DEF ID funcionstruct','asignacion',3,'p_asignacion','sintactico.py',62),
  ('booleanos -> TRUE','booleanos',1,'p_booleanos','sintactico.py',66),
  ('booleanos -> FALSE','booleanos',1,'p_booleanos','sintactico.py',67),
  ('imprimir -> operadoresPrint factor','imprimir',2,'p_imprimir','sintactico.py',70),
  ('imprimir -> operadoresPrint STRING','imprimir',2,'p_imprimir','sintactico.py',71),
  ('imprimir -> PRINTF valorl','imprimir',2,'p_imprimir','sintactico.py',72),
  ('sentenciado -> LPAREN DO general RPAREN','sentenciado',4,'p_sentenciado','sintactico.py',75),
  ('sentenciaif -> IF LPAREN comparacion RPAREN general','sentenciaif',5,'p_sentenciaif','sintactico.py',78),
  ('sentenciaif -> IF LPAREN comparacion RPAREN sentenciado sentenciado','sentenciaif',6,'p_sentenciaif','sintactico.py',79),
  ('sentenciawhile -> WHILE LPAREN comparacion RPAREN sentenciado','sentenciawhile',5,'p_sentenciawhile','sintactico.py',84),
  ('struct -> lista','struct',1,'p_struct','sintactico.py',88),
  ('struct -> vector','struct',1,'p_struct','sintactico.py',89),
  ('struct -> mapa','struct',1,'p_struct','sintactico.py',90),
  ('struct -> conjunto','struct',1,'p_struct','sintactico.py',91),
  ('lista -> QUOTE LPAREN valorl RPAREN','lista',4,'p_lista','sintactico.py',94),
  ('vector -> LCOR valorl RCOR','vector',3,'p_vector','sintactico.py',97),
  ('mapa -> LBRACE repetirclave RBRACE','mapa',3,'p_mapa','sintactico.py',100),
  ('conjunto -> NUMERAL LBRACE valorl RBRACE','conjunto',4,'p_conjunto','sintactico.py',103),
  ('clavevalor -> ID DDOT valor','clavevalor',3,'p_clavevalor','sintactico.py',106),
  ('repetirclave -> clavevalor','repetirclave',1,'p_repetirclave','sintactico.py',109),
  ('repetirclave -> clavevalor COMA repetirclave','repetirclave',3,'p_repetirclave','sintactico.py',110),
  ('valor -> NUMBER','valor',1,'p_valor','sintactico.py',112),
  ('valor -> ID','valor',1,'p_valor','sintactico.py',113),
  ('valor -> STRING','valor',1,'p_valor','sintactico.py',114),
  ('valor -> booleanos','valor',1,'p_valor','sintactico.py',115),
  ('valor -> FLOAT','valor',1,'p_valor','sintactico.py',116),
  ('valorl -> NUMBER','valorl',1,'p_valorl','sintactico.py',119),
  ('valorl -> ID','valorl',1,'p_valorl','sintactico.py',120),
  ('valorl -> STRING','valorl',1,'p_valorl','sintactico.py',121),
  ('valorl -> booleanos','valorl',1,'p_valorl','sintactico.py',122),
  ('valorl -> FLOAT','valorl',1,'p_valorl','sintactico.py',123),
  ('valorl -> valorl valorl','valorl',2,'p_valorl','sintactico.py',124),
  ('funcionstruct -> conjfunction','funcionstruct',1,'p_funcionstruct','sintactico.py',128),
  ('funcionstruct -> LPAREN STR STRING strings RPAREN','funcionstruct',5,'p_funcionstruct','sintactico.py',129),
  ('funcionstruct -> LPAREN GET conjunto NUMBER RPAREN','funcionstruct',5,'p_funcionstruct','sintactico.py',130),
  ('funcionstruct -> LPAREN GET conjunto ID RPAREN','funcionstruct',5,'p_funcionstruct','sintactico.py',131),
  ('funcionstruct -> LPAREN NTH lista NUMBER RPAREN','funcionstruct',5,'p_funcionstruct','sintactico.py',132),
  ('funcionstruct -> LPAREN NTH lista ID RPAREN','funcionstruct',5,'p_funcionstruct','sintactico.py',133),
  ('funcionstruct -> LPAREN POP vector RPAREN','funcionstruct',4,'p_funcionstruct','sintactico.py',134),
  ('funcionstruct -> LPAREN COUNT STRING RPAREN','funcionstruct',4,'p_funcionstruct','sintactico.py',135),
  ('funcionstruct -> LPAREN COUNT ID RPAREN','funcionstruct',4,'p_funcionstruct','sintactico.py',136),
  ('conjfunction -> LPAREN CONJ lista NUMBER RPAREN','conjfunction',5,'p_conjfunction','sintactico.py',142),
  ('conjfunction -> LPAREN CONJ lista ID RPAREN','conjfunction',5,'p_conjfunction','sintactico.py',143),
  ('conjfunction -> LPAREN CONJ conjunto NUMBER RPAREN','conjfunction',5,'p_conjfunction','sintactico.py',144),
  ('conjfunction -> LPAREN CONJ conjunto ID RPAREN','conjfunction',5,'p_conjfunction','sintactico.py',145),
  ('conjfunction -> LPAREN CONJ vector NUMBER RPAREN','conjfunction',5,'p_conjfunction','sintactico.py',146),
  ('conjfunction -> LPAREN CONJ vector ID RPAREN','conjfunction',5,'p_conjfunction','sintactico.py',147),
  ('strings -> STRING','strings',1,'p_strings','sintactico.py',152),
  ('strings -> STRING STRING','strings',2,'p_strings','sintactico.py',153),
]
