import ply.lex

reserved = {
	"if"		:	"IF",
	"else"		:	"ELSE",
	"while"		:	"WHILE",
	"for"		:	"FOR",
	"read"		:	"READ",
	"print"		:	"PRINT",
	"function"	:	"FUNCTION",
	"main"		:	"MAIN",
	"call"		:	"CALL",
	"program"	:	"PROGRAM",
	"int"		:	"INT",
	"float"		:	"FLOAT",
	"arrint"	:	"ARRINT"	
}

tokens = ['NEQ', 'EQ', 'GTEQ', 'LTEQ', 'AND', 'OR', 'ID', 'NUMINT', 'NUMFLOAT', 'CTES','SEMMICOLON', 'POINT',
		  'RPAREN', 'LPAREN', 'RSQUARE', 'LSQUARE', 'RKEY', 'LKEY', 'LT', 'GT', 'PLUS', 'MINUS', 'TIMES',
		  'DIVISION', 'ASSIGN', 'COMMA'] + list(reserved.values())

#tokens
t_ignore 		= ' \t'
t_NUMINT   		= r'[0-9]+' 		#Constantes enteras
t_NUMFLOAT   	= r'[0-9]+\.[0-9]+' #Constantes flotantes
t_CTES			= r'".*"'			#Constantes string
t_OR 			= r'\|\|' 			#Operador logico OR 
t_AND 			= r'&&'   			#Operador logico AND
t_NEQ			= r'!='				#Diferente de
t_EQ 			= r'=='				#Igual a 
t_GTEQ			= r'>='				#Mayor que
t_LTEQ 			= r'<='				#Menor que
t_PLUS 			= r'\+'				#Suma
t_MINUS 		= r'-'				#Resta
t_TIMES 		= r'\*'				#Multiplicacion
t_DIVISION 		= r'/'				#Division
t_ASSIGN 		= r'='				#Asignacion valor
t_LT 			= r'<'				#Menor a
t_GT 			= r'>'				#Mayor a
t_LPAREN 		= r'\('				
t_RPAREN		= r'\)'
t_LSQUARE 		= r'\['
t_RSQUARE		= r'\]'
t_LKEY	 		= r'\{'
t_RKEY			= r'\}'
t_COMMA 		= r'[,]'
t_SEMMICOLON	= r';'
t_POINT 		= r'\.'

#Definicion de ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')
    return t

#Definicion para el salto de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#Define los errores 
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#Build the lexer
import ply.lex as lex
lex.lex()