import ply.yacc as yacc
from reglasSemanticas import reglas
from lexico import tokens

error 				= None 	#Variable para saber si hay error 
contador			= 0  	#Contador para saber cuantas variables hay
Name				= {} 	#Diccionario para guardar las variables con su valor inicial
Name_tipos			= {}	#Diccionario para guardar las variables con su tipo
Name_Functions		= {}	#Diccionario para guardar las funciones declaradas		
index_repetidas		= 0		#Index del diccionario de las palabras repetidas
cuadruplo			= []
pila_saltos			= []
pila_operandos		= []
pila_operadores		= []
contador_cuadruplo 	= 0
temporales 			= ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10',
					   'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18', 'T19', 'T20'
					  ]
dic_temp 			= {'T1':0, 'T2':0, 'T3':0, 'T4':0, 'T5':0, 'T6':0, 'T7':0, 'T8':0, 'T9':0, 'T10':0,
					   'T11':0, 'T12':0, 'T13':0, 'T14':0, 'T15':0, 'T16':0, 'T17':0, 'T18':0, 'T19':0, 'T20':0
					  }
dic_tipos 			= {}
pila_constante		= []
pila_saltos			= []
pila_ejecucion		= []
aux_variable1		= None
aux_variable2		= None
print_type			= 0
variables_string	= None


def p_programa(p):
	'''programa : PROGRAM first_cuadruplo ID var_declaration function_declaration rellena_cuadruplo main_declaration POINT'''
	global aux_variable1
	global aux_variable2
	global contador_cuadruplo
	cuadruplo.append(['END'])
	print(cuadruplo)
	print(dic_tipos)
	i = 0

	while True:
		aux = cuadruplo[i]
		for index in range(len(aux)):
			if (aux[index] == '+' or aux[index] == '-' or aux[index] == '*' or aux[index] == '/'): 
				if (aux[2] == 'T1' or aux[2] == 'T2' or aux[2] == 'T3' or aux[2] == 'T4' or aux[2] == 'T5' or aux[2] == 'T6' or
					aux[2] == 'T7' or aux[2] == 'T8' or aux[2] == 'T9' or aux[2] == 'T10' or aux[2] == 'T11' or aux[2] == 'T12' or
					aux[2] == 'T13' or aux[2] == 'T14' or aux[2] == 'T15' or aux[2] == 'T16' or aux[2] == 'T17' or aux[2] == 'T18' or
					aux[2] == 'T19' or aux[2] == 'T20'):

					aux_variable2 = True
					variable2 = dic_temp[aux[2]]

				if (aux[1] == 'T1' or aux[1] == 'T2' or aux[1] == 'T3' or aux[1] == 'T4' or aux[1] == 'T5' or aux[1] == 'T6' or
					aux[1] == 'T7' or aux[1] == 'T8' or aux[1] == 'T9' or aux[1] == 'T10' or aux[1] == 'T11' or aux[1] == 'T12' or
					aux[1] == 'T13' or aux[1] == 'T14' or aux[1] == 'T15' or aux[1] == 'T16' or aux[1] == 'T17' or aux[1] == 'T18' or
					aux[1] == 'T19' or aux[1] == 'T20'):

					aux_variable1 = True
					variable1 = dic_temp[aux[1]]	

				if aux[index] == '+':
					if (dic_tipos[aux[3]] == 'int'):
						if aux_variable1 == True:
							op1 = int(float(variable1))
						elif aux[1] in Name:
							op1 = int(float(Name[aux[1]]))
						else:
							op1 = int(float(aux[1]))
						
						if aux_variable2 == True:
							op2 = int(float(variable2))
						elif aux[2] in Name:
							op2 = int(float(Name[aux[2]]))
						else:
							op2 = int(float(aux[2]))

					elif (dic_tipos[aux[3]] == 'float'):
						if aux_variable1 == True:
							op1 = float(variable1)
						elif aux[1] in Name:
							op1 = float(Name[aux[1]])
						else:
							op1 = float(aux[1])
						
						if aux_variable2 == True:
							op2 = float(variable2)
						elif aux[2] in Name:
							op2 = float(Name[aux[2]])
						else:
							op2 = float(aux[2])

					
					ans = op1 + op2
					for index in range(len(aux)):
						dic_temp[aux[3]] = ans
						break
				
				elif aux[index] == '-':
					if (dic_tipos[aux[3]] == 'int'):
						if aux_variable1 == True:
							op1 = int(float(variable1))
						elif aux[1] in Name:
							op1 = int(float(Name[aux[1]]))
						else:
							op1 = int(float(aux[1]))
						
						if aux_variable2 == True:
							op2 = int(float(variable2))
						elif aux[2] in Name:
							op2 = int(float(Name[aux[2]]))
						else:
							op2 = int(float(aux[2]))

					elif (dic_tipos[aux[3]] == 'float'):
						if aux_variable1 == True:
							op1 = float(variable1)
						elif aux[1] in Name:
							op1 = float(Name[aux[1]])
						else:
							op1 = float(aux[1])
						
						if aux_variable2 == True:
							op2 = float(variable2)
						elif aux[2] in Name:
							op2 = float(Name[aux[2]])
						else:
							op2 = float(aux[2])
					
					
					ans = op1 - op2
					for index in range(len(aux)):
						dic_temp[aux[3]] = ans
						break
				
				elif aux[index] == '*':
					if (dic_tipos[aux[3]] == 'int'):
						if aux_variable1 == True:
							op1 = int(float(variable1))
						elif aux[1] in Name:
							op1 = int(float(Name[aux[1]]))
						else:
							op1 = int(float(aux[1]))
						
						if aux_variable2 == True:
							op2 = int(float(variable2))
						elif aux[2] in Name:
							op2 = int(float(Name[aux[2]]))
						else:
							op2 = int(float(aux[2]))

					elif (dic_tipos[aux[3]] == 'float'):
						if aux_variable1 == True:
							op1 = float(variable1)
						elif aux[1] in Name:
							op1 = float(Name[aux[1]])
						else:
							op1 = float(aux[1])
						
						if aux_variable2 == True:
							op2 = float(variable2)
						elif aux[2] in Name:
							op2 = float(Name[aux[2]])
						else:
							op2 = float(aux[2])
					
					
					ans = op1 * op2
					for index in range(len(aux)):
						dic_temp[aux[3]] = ans
						break
				
				elif aux[index] == '/':
					if (dic_tipos[aux[3]] == 'float'):
						if aux_variable1 == True:
							op1 = int(float(variable1))
						else:
							op1 = int(float(aux[1]))
						if aux_variable2 == True:
							op2 = float(variable2)
						else:
							op2 = float(aux[2])
					
					
					ans = op1 / op2
					for index in range(len(aux)):
						dic_temp[aux[3]] = ans
						break

				aux_variable1 = False
				aux_variable2 = False
			
			elif aux[index] == '=':
				if (aux[1] == 'T1' or aux[1] == 'T2' or aux[1] == 'T3' or aux[1] == 'T4' or aux[1] == 'T5' or aux[1] == 'T6' or
					aux[1] == 'T7' or aux[1] == 'T8' or aux[1] == 'T9' or aux[1] == 'T10' or aux[1] == 'T11' or aux[1] == 'T12' or
					aux[1] == 'T13' or aux[1] == 'T14' or aux[1] == 'T15' or aux[1] == 'T16' or aux[1] == 'T17' or aux[1] == 'T18' or
					aux[1] == 'T19' or aux[1] == 'T20'):
						
					variable1 = dic_temp[aux[1]]
				else:
					variable1 = aux[1]
				for index1 in Name:
					if (aux[3] == index1):
						continua = True
						break
					else:
						continua = False
				if (not continua):
					print('Error. Variable ' + aux[3] + ' no declarada previamente')
					exit(1)
				else:
					Name[aux[3]] = variable1

			elif (aux[index] == 'print'):
				if (variables_string):
					print(aux[3])
				else:
					for index1 in Name:
						if (aux[3] == index1):
							continua = True
							break
						else:
							continua = False
					if (not continua):
						print('Error. Variable ' + aux[3] + ' no declarada previamente')
						exit(1)
					print(Name[aux[3]])

			elif (aux[index] == 'read'):
				if aux[3] not in Name:
					print('Error. Variable ' + aux[3] + ' no declarada previamente')
					exit(1)
				Name[aux[3]] = raw_input('> ')

			elif (aux[index] == '>'):
				if aux[1] in Name:
					op1 = float(Name[aux[1]])
				else:
					op1 = float(aux[1])

				if aux[2] in Name:
					op2 = float(Name[aux[2]])
				else:
					op2 = float(aux[2])
				
				ans = op1 > op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == '<'):
				if aux[1] in Name:
					op1 = float(Name[aux[1]])
				else:
					op1 = float(aux[1])

				if aux[2] in Name:
					op2 = float(Name[aux[2]])
				else:
					op2 = float(aux[2])
				
				ans = op1 < op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == '!='):
				if aux[1] in Name:
					op1 = float(Name[aux[1]])
				else:
					op1 = float(aux[1])

				if aux[2] in Name:
					op2 = float(Name[aux[2]])
				else:
					op2 = float(aux[2])
				
				ans = op1 != op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == '=='):
				if aux[1] in Name:
					op1 = float(Name[aux[1]])
				else:
					op1 = float(aux[1])

				if aux[2] in Name:
					op2 = float(Name[aux[2]])
				else:
					op2 = float(aux[2])

				ans = op1 == op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == '>='):
				if aux[1] in Name:
					op1 = float(Name[aux[1]])
				else:
					op1 = float(aux[1])

				if aux[2] in Name:
					op2 = float(Name[aux[2]])
				else:
					op2 = float(aux[2])
				
				ans = op1 >= op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == '<='):
				if aux[1] in Name:
					op1 = float(Name[aux[1]])
				else:
					op1 = float(aux[1])

				if aux[2] in Name:
					op2 = float(Name[aux[2]])
				else:
					op2 = float(aux[2])
				
				ans = op1 <= op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == '&&'):
				if (aux[2] == 'T1' or aux[2] == 'T2' or aux[2] == 'T3' or aux[2] == 'T4' or aux[2] == 'T5' or aux[2] == 'T6' or
					aux[2] == 'T7' or aux[2] == 'T8' or aux[2] == 'T9' or aux[2] == 'T10' or aux[2] == 'T11' or aux[2] == 'T12' or
					aux[2] == 'T13' or aux[2] == 'T14' or aux[2] == 'T15' or aux[2] == 'T16' or aux[2] == 'T17' or aux[2] == 'T18' or
					aux[2] == 'T19' or aux[2] == 'T20'):

					aux_variable2 = True
					variable2 = dic_temp[aux[2]]

				if (aux[1] == 'T1' or aux[1] == 'T2' or aux[1] == 'T3' or aux[1] == 'T4' or aux[1] == 'T5' or aux[1] == 'T6' or
					aux[1] == 'T7' or aux[1] == 'T8' or aux[1] == 'T9' or aux[1] == 'T10' or aux[1] == 'T11' or aux[1] == 'T12' or
					aux[1] == 'T13' or aux[1] == 'T14' or aux[1] == 'T15' or aux[1] == 'T16' or aux[1] == 'T17' or aux[1] == 'T18' or
					aux[1] == 'T19' or aux[1] == 'T20'):

					aux_variable1 = True
					variable1 = dic_temp[aux[1]]

				if aux_variable1 == True:
					op1 = variable1
				else:
					op1 = aux[1]
				if aux_variable2 == True:
					op2 = variable2
				else:
					op2 = aux[2]
				
				ans = op1 and op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == '||'):
				if (aux[2] == 'T1' or aux[2] == 'T2' or aux[2] == 'T3' or aux[2] == 'T4' or aux[2] == 'T5' or aux[2] == 'T6' or
					aux[2] == 'T7' or aux[2] == 'T8' or aux[2] == 'T9' or aux[2] == 'T10' or aux[2] == 'T11' or aux[2] == 'T12' or
					aux[2] == 'T13' or aux[2] == 'T14' or aux[2] == 'T15' or aux[2] == 'T16' or aux[2] == 'T17' or aux[2] == 'T18' or
					aux[2] == 'T19' or aux[2] == 'T20'):

					aux_variable2 = True
					variable2 = dic_temp[aux[2]]

				if (aux[1] == 'T1' or aux[1] == 'T2' or aux[1] == 'T3' or aux[1] == 'T4' or aux[1] == 'T5' or aux[1] == 'T6' or
					aux[1] == 'T7' or aux[1] == 'T8' or aux[1] == 'T9' or aux[1] == 'T10' or aux[1] == 'T11' or aux[1] == 'T12' or
					aux[1] == 'T13' or aux[1] == 'T14' or aux[1] == 'T15' or aux[1] == 'T16' or aux[1] == 'T17' or aux[1] == 'T18' or
					aux[1] == 'T19' or aux[1] == 'T20'):

					aux_variable1 = True
					variable1 = dic_temp[aux[1]]

				if aux_variable1 == True:
					op1 = variable1
				else:
					op1 = aux[1]
				if aux_variable2 == True:
					op2 = variable2
				else:
					op2 = aux[2]
				
				ans = op1 or op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == 'gotof'):
				if (aux[1] == 'T1' or aux[1] == 'T2' or aux[1] == 'T3' or aux[1] == 'T4' or aux[1] == 'T5' or aux[1] == 'T6' or
					aux[1] == 'T7' or aux[1] == 'T8' or aux[1] == 'T9' or aux[1] == 'T10' or aux[1] == 'T11' or aux[1] == 'T12' or
					aux[1] == 'T13' or aux[1] == 'T14' or aux[1] == 'T15' or aux[1] == 'T16' or aux[1] == 'T17' or aux[1] == 'T18' or
					aux[1] == 'T19' or aux[1] == 'T20'):

					variable1 = dic_temp[aux[1]]
				
				if (variable1 == False):
					i = int(float(aux[3])) - 1

			elif (aux[index] == 'goto'):
				i = int(float(aux[3])) - 1 

			elif (aux[index] == 'gotoFun'):
				i = int(float(aux[3])) - 1

			elif (aux[index] == 'retorno'):
				i = pila_ejecucion.pop() - 1

			break

		i += 1
		if cuadruplo[i] == ['END']:
			break

def p_first_cuadruplo(p):
	'''first_cuadruplo : '''
	global cuadruplo
	global contador_cuadruplo
	global pila_saltos
	pila_saltos.append(len(cuadruplo))
	cuadruplo.append(['goto', ' ', ' ', ' '])
	contador_cuadruplo += 1

def p_var_declaration(p):
	'''var_declaration : INT variable_ent_list var_declaration 
					   | FLOAT variable_float_list var_declaration 
					   | ARRINT variable_arrint_list var_declaration
					   | empty'''

def p_variable_ent_list(p):
	'''variable_ent_list : ID SEMMICOLON 
					 	 | ID COMMA variable_ent_list 
					 	 | ID ASSIGN NUMINT SEMMICOLON
					 	 | ID ASSIGN NUMINT COMMA variable_ent_list'''
	if (p[1] in Name):
		print('Error. Variable ' + p[1] + ' repetida')
		exit(1)
	Name[p[1]] = 0
	if (p[2] == '='):
		Name[p[1]] = p[3]
	Name_tipos[p[1]] = 'int'

def p_variable_float_list(p):
	'''variable_float_list : ID SEMMICOLON
						   | ID COMMA variable_float_list
						   | ID ASSIGN NUMFLOAT SEMMICOLON 
						   | ID ASSIGN NUMFLOAT COMMA variable_float_list'''
	if (p[1] in Name):
		print('Error. Variable ' + p[1] + ' repetida')
		exit(1)
	Name[p[1]] = 0
	if (p[2] == '='):
		Name[p[1]] = p[3]
	Name_tipos[p[1]] = 'float'

def p_variable_arrint_list(p):
	'''variable_arrint_list : ID LSQUARE ID RSQUARE SEMMICOLON 
					 	 	| ID LSQUARE ID RSQUARE COMMA variable_arrint_list
					 	 	| ID LSQUARE ID RSQUARE LSQUARE ID RSQUARE SEMMICOLON
					 	 	| ID LSQUARE ID RSQUARE LSQUARE ID RSQUARE COMMA variable_arrint_list'''
	Name[p[1]] = 0
	if (p[2] == '='):
		Name[p[1]] = p[3]

def p_function_declaration(p):
	'''function_declaration : function_1 function_declaration
							| empty'''

def p_function_1(p):
	'''function_1 : FUNCTION ID LPAREN RPAREN function_cuad_1 LKEY estatuto RKEY'''


def p_function_cuad_1(p):
	'''function_cuad_1 : '''
	global Name_Functions
	funcion_cuadruplo = len(cuadruplo)
	if (p[-3] in Name_Functions):
		print('Error. Declaracion repetida de funcion')
		exit(1)
	else:
		Name_Functions[p[-3]] = funcion_cuadruplo


def p_main_declaration(p):
	'''main_declaration : MAIN LPAREN RPAREN LKEY estatuto RKEY '''

def p_rellena_cuadruplo(p):
	'''rellena_cuadruplo : '''
	salto = pila_saltos.pop()
	cuadruplo[salto] = [cuadruplo[salto][0], cuadruplo[salto][1], ' ', len(cuadruplo)]

def p_estatuto(p):
	'''estatuto : ciclo_for estatuto
				| ciclo_if estatuto
				| ciclo_while estatuto
				| read_process estatuto
				| print_process estatuto
				| id_asignacion estatuto
				| id SEMMICOLON estatuto
				| ret_process estatuto
				| empty'''

def p_ret_process(p):
	'''ret_process : RETURN SEMMICOLON'''
	cuadruplo.append(['retorno', ' ', ' ', ' '])

def p_print_process(p):
	'''print_process : PRINT LPAREN print_1 RPAREN SEMMICOLON'''

def p_print_1(p):
	'''print_1 : id print_aux_1 print_prima_1
			   | string_type print_aux_2 print_prima_1'''

def p_print_aux_1(p):
	'''print_aux_1 : '''
	global print_type
	print_type = 1

def p_print_aux_2(p):
	'''print_aux_2 : '''
	global print_type
	print_type = 2

def p_print_prima_1(p):
	'''print_prima_1 : COMMA print_prima_2 print_1
					 | empty print_prima_2'''

def p_print_prima_2(p):
	'''print_prima_2 : '''
	global print_type
	global contador_cuadruplo
	if (print_type == 1):
		cuadruplo.append(['print', ' ', ' ', pila_operandos.pop()[0]])
		contador_cuadruplo += 1
	elif (print_type == 2):
		cuadruplo.append(['print', ' ', ' ', pila_operandos.pop()[0]])
		contador_cuadruplo += 1

def p_read_process(p):
	'''read_process : READ LPAREN sexp RPAREN SEMMICOLON'''
	global contador_cuadruplo
	cuadruplo.append(['read', ' ', ' ', pila_operandos.pop()[0]])

def p_id_asignacion(p):
	'''id_asignacion : id id_asignacion_prima'''

def p_id_asignacion_prima(p):
	'''id_asignacion_prima : ASSIGN sexp SEMMICOLON
						   | LSQUARE expression RSQUARE ASSIGN sexp SEMMICOLON
					 	   | LSQUARE expression RSQUARE LSQUARE expression RSQUARE ASSIGN sexp SEMMICOLON'''
	global contador_cuadruplo
	cuadruplo.append(['=', pila_operandos.pop()[0], ' ', pila_operandos.pop()[0]])
	contador_cuadruplo += 1

#Ciclo for
def p_ciclo_for(p):
	'''ciclo_for : FOR LPAREN id ASSIGN sexp ciclo_for_1 SEMMICOLON sexp ciclo_for_2 SEMMICOLON id ASSIGN sexp RPAREN LKEY estatuto RKEY ciclo_for_3'''


def p_ciclo_for_1(p):
	'''ciclo_for_1 : '''
	cuenta = pila_operandos.pop()
	identificador = pila_operandos.pop()
	if (identificador[0] in Name):
		cuadruplo.append(['=', cuenta[0], ' ', identificador[0]])
	else:
		print('Variable ' + str(identificador[0]) + ' no declarada previamente')
		exit(1)

def p_ciclo_for_2(p):
	'''ciclo_for_2 : '''
	condicion = pila_operandos.pop()
	pila_saltos.append(len(cuadruplo))
	cuadruplo.append(['gotof', condicion[0], ' ', ' '])

def p_ciclo_for_3(p):
	'''ciclo_for_3 : '''
	global pila_saltos
	fin = pila_saltos.pop()
	cuenta = pila_operandos.pop()
	identificador = pila_operandos.pop()
	cuadruplo.append(['=', cuenta[0], ' ', identificador[0]])
	cuadruplo[fin] = [cuadruplo[fin][0], cuadruplo[fin][1], ' ', len(cuadruplo) + 1]
	cuadruplo.append(['goto', ' ', ' ', fin - 1])


#Ciclo while
def p_ciclo_while(p):
	'''ciclo_while : WHILE ciclo_while_1 LPAREN sexp RPAREN ciclo_while_2 LKEY estatuto RKEY'''
	global cuadruplo
	global contador_cuadruplo
	falso = pila_saltos.pop()
	retorno = pila_saltos.pop()
	cuadruplo.append(['goto', ' ', ' ', str(retorno)])
	cuadruplo[falso] = [cuadruplo[falso][0], cuadruplo[falso][1], ' ', str(len(cuadruplo))]
	contador_cuadruplo += 1

def p_ciclo_while_1(p):
	'''ciclo_while_1 : '''
	pila_saltos.append(len(cuadruplo))


def p_ciclo_while_2(p):
	'''ciclo_while_2 : '''
	global cuadruplo
	global contador_cuadruplo
	aux = pila_operandos.pop()
	if (aux[1] != 'bool'):
		print('Error semantico. Tipo diferente de Booleano')
		exit(1)
	else:
		pila_saltos.append(len(cuadruplo))
		cuadruplo.append(['gotof', aux[0], ' ', ' '])
		contador_cuadruplo += 1

#Ciclo if
def p_ciclo_if(p):
	'''ciclo_if : IF LPAREN sexp RPAREN ciclo_if_1 LKEY estatuto RKEY if_else'''

def p_ciclo_if_1(p):
	'''ciclo_if_1 : '''
	global cuadruplo
	global contador_cuadruplo
	aux = pila_operandos.pop()
	if (aux[1] != 'bool'):
		print('Error semantico. Tipo diferente de Booleano')
		exit(1)
	else:
		pila_saltos.append(len(cuadruplo))
		cuadruplo.append(['gotof', aux[0], ' ', ' '])
		contador_cuadruplo += 1
		


def p_if_else(p):
	'''if_else : ELSE LKEY if_else_1 estatuto RKEY 
			   | empty'''
	global cuadruplo
	global contador_cuadruplo
	fin = pila_saltos.pop()
	cuadruplo[fin] = [cuadruplo[fin][0], cuadruplo[fin][1], ' ', str(len(cuadruplo))]
	contador_cuadruplo += 1


def p_if_else_1(p):
	'''if_else_1 : '''
	global cuadruplo
	falso = pila_saltos.pop()
	cuadruplo[falso] = [cuadruplo[falso][0], cuadruplo[falso][1], ' ', str(len(cuadruplo) + 1)]
	pila_saltos.append(len(cuadruplo))
	cuadruplo.append(['goto', ' ', ' ', ' '])



def p_sexp(p):
	'''sexp : cuadruplo_1 sexprima'''

def p_cuadruplo_1(p): 
    '''cuadruplo_1 : expression'''
    if pila_operadores:
    	if pila_operadores[-1] == '&&' or pila_operadores[-1] == '||':
			global cuadruplo
			global contador_cuadruplo
			operador = pila_operadores.pop()
			operando1 = pila_operandos.pop()
			operando2 = pila_operandos.pop()
			for index in Name:
				if operando1[0] == index:
					for index2 in Name_tipos:
						if operando1[0] == index2:
							pila_operandos.append([Name[index], Name_tipos[index2]])
							operando1 = pila_operandos.pop()
			for index in Name:
				if operando2[0] == index:
					for index2 in Name_tipos:
						if operando2[0] == index2:
							pila_operandos.append([Name[index], Name_tipos[index2]])
							operando2 = pila_operandos.pop()
			tipo = reglas.get((operando2[1], operador, operando1[1]), 'Error')
			if tipo != 'Error':
				resultado = temporales.pop()
				cuadruplo.append([operador, operando2[0], operando1[0], resultado])
				contador_cuadruplo += 1
				if (operando1 == 'T1' or operando1 == 'T2' or operando1 == 'T3' or operando1 == 'T4' or operando1 == 'T5' or operando1 == 'T6' or
				    operando1 == 'T7' or operando1 == 'T8' or operando1 == 'T9' or operando1 == 'T10' or operando1 == 'T11' or operando1 == 'T12' or 
				    operando1 == 'T13' or operando1 == 'T14' or operando1 == 'T15' or operando1 == 'T16' or operando1 == 'T17' or operando1 == 'T18' or
				    operando1 == 'T19' or operando1 == 'T20'):
					temporales.append(operando1)
				elif (operando2 == 'T1' or operando2 == 'T2' or operando2 == 'T3' or operando2 == 'T4' or operando2 == 'T5' or operando2 == 'T6' or
				    operando2 == 'T7' or operando2 == 'T8' or operando2 == 'T9' or operando2 == 'T10' or operando2 == 'T11' or operando2 == 'T12' or 
				    operando2 == 'T13' or operando2 == 'T14' or operando2 == 'T15' or operando2 == 'T16' or operando2 == 'T17' or operando2 == 'T18' or
				    operando2 == 'T19' or operando2 == 'T20'):
					temporales.append(operando2)
				pila_operandos.append([resultado, tipo])
			else:
				print('Error4')
				exit(1)


def p_sexprima(p): 
    '''sexprima : AND push_operator sexp
                | OR push_operator sexp
                | empty'''

def p_expression(p):
	'''expression : cuadruplo_2 expressionp'''

def p_cuadruplo_2(p): 
    '''cuadruplo_2 : exp'''
    if pila_operadores:
		if pila_operadores[-1] == '>' or pila_operadores[-1] == '<' or pila_operadores[-1] == '>=' or pila_operadores[-1] == '<=' or pila_operadores[-1] == '==' or pila_operadores[-1] == '!=':
			global cuadruplo
			global contador_cuadruplo
			operador = pila_operadores.pop()
			operando1 = pila_operandos.pop()
			operando2 = pila_operandos.pop()
			for index in Name:
				if operando1[0] == index:
					for index2 in Name_tipos:
						if operando1[0] == index2:
							pila_operandos.append([index, Name_tipos[index2]])
							operando1 = pila_operandos.pop()
			
			for index in Name:
				if operando2[0] == index:
					for index2 in Name_tipos:
						if operando2[0] == index2:
							pila_operandos.append([index, Name_tipos[index2]])
							operando2 = pila_operandos.pop()
			tipo = reglas.get((operando2[1], operador, operando1[1]), 'Error')
			if tipo != 'Error':
				resultado = temporales.pop()
				cuadruplo.append([operador, operando2[0], operando1[0], resultado])
				contador_cuadruplo += 1
				if (operando1 == 'T1' or operando1 == 'T2' or operando1 == 'T3' or operando1 == 'T4' or operando1 == 'T5' or operando1 == 'T6' or
					operando1 == 'T7' or operando1 == 'T8' or operando1 == 'T9' or operando1 == 'T10' or operando1 == 'T11' or operando1 == 'T12' or 
					operando1 == 'T13' or operando1 == 'T14' or operando1 == 'T15' or operando1 == 'T16' or operando1 == 'T17' or operando1 == 'T18' or
					operando1 == 'T19' or operando1 == 'T20'):
					temporales.append(operando1)
				elif (operando2 == 'T1' or operando2 == 'T2' or operando2 == 'T3' or operando2 == 'T4' or operando2 == 'T5' or operando2 == 'T6' or
					operando2 == 'T7' or operando2 == 'T8' or operando2 == 'T9' or operando2 == 'T10' or operando2 == 'T11' or operando2 == 'T12' or 
					operando2 == 'T13' or operando2 == 'T14' or operando2 == 'T15' or operando2 == 'T16' or operando2 == 'T17' or operando2 == 'T18' or
					operando2 == 'T19' or operando2 == 'T20'):
					temporales.append(operando2)
				pila_operandos.append([resultado, tipo])
			else:
				print('Error')
				exit(1)
  
def p_expressionp(p): 
    '''expressionp : LT push_operator expression
                   | GT push_operator expression
                   | LTEQ push_operator expression 
                   | GTEQ push_operator expression
                   | EQ push_operator expression
                   | NEQ push_operator expression 
                   | empty'''
 
def p_exp(p):
	'''exp : cuadruplo_3 expp'''

def p_cuadruplo_3(p): 
    '''cuadruplo_3 : term'''
    if pila_operadores:
		if pila_operadores[-1] == '+' or pila_operadores[-1] == '-':
			global cuadruplo
			global contador_cuadruplo
			operador = pila_operadores.pop()
			operando1 = pila_operandos.pop()
			operando2 = pila_operandos.pop()
			for index in Name:
				if operando1[0] == index:
					for index2 in Name_tipos:
						if operando1[0] == index2:
							pila_operandos.append([index, Name_tipos[index2]])
							operando1 = pila_operandos.pop()
			for index in Name:
				if operando2[0] == index:
					for index2 in Name_tipos:
						if operando2[0] == index2:
							pila_operandos.append([index, Name_tipos[index2]])
							operando2 = pila_operandos.pop()
			tipo = reglas.get((operando2[1], operador, operando1[1]), 'Error')
			if tipo != 'Error':
				resultado = temporales.pop()
				cuadruplo.append([operador, operando2[0], operando1[0], resultado])
				contador_cuadruplo += 1
				if (operando1 == 'T1' or operando1 == 'T2' or operando1 == 'T3' or operando1 == 'T4' or operando1 == 'T5' or operando1 == 'T6' or
				    operando1 == 'T7' or operando1 == 'T8' or operando1 == 'T9' or operando1 == 'T10' or operando1 == 'T11' or operando1 == 'T12' or 
				    operando1 == 'T13' or operando1 == 'T14' or operando1 == 'T15' or operando1 == 'T16' or operando1 == 'T17' or operando1 == 'T18' or
				    operando1 == 'T19' or operando1 == 'T20'):
					temporales.append(operando1)
				elif (operando2 == 'T1' or operando2 == 'T2' or operando2 == 'T3' or operando2 == 'T4' or operando2 == 'T5' or operando2 == 'T6' or
				    operando2 == 'T7' or operando2 == 'T8' or operando2 == 'T9' or operando2 == 'T10' or operando2 == 'T11' or operando2 == 'T12' or 
				    operando2 == 'T13' or operando2 == 'T14' or operando2 == 'T15' or operando2 == 'T16' or operando2 == 'T17' or operando2 == 'T18' or
				    operando2 == 'T19' or operando2 == 'T20'):
					temporales.append(operando2)
				pila_operandos.append([resultado, tipo])
				dic_tipos[resultado] = tipo
			else:
				print('Error2')
				exit(1)


def p_expp(p): 
    '''expp : PLUS push_operator exp
            | MINUS push_operator exp
            | empty'''

def p_term(p):
	'''term : cuadruplo_4 termp'''

def p_cuadruplo_4(p): 
    '''cuadruplo_4 : factor'''
    if pila_operadores:
    	if pila_operadores[-1] == '*' or pila_operadores[-1] == '/':
    		global cuadruplo
    		global contador_cuadruplo
    		operador = pila_operadores.pop()
    		operando1 = pila_operandos.pop()
    		operando2 = pila_operandos.pop()
    		for index in Name:
    			if operando1[0] == index:
    				for index2 in Name_tipos:
						if operando1[0] == index2:
							pila_operandos.append([Name[index], Name_tipos[index2]])
							operando1 = pila_operandos.pop()
			for index in Name:
				if operando2[0] == index:
					for index2 in Name_tipos:
						if operando2[0] == index2:
							pila_operandos.append([Name[index], Name_tipos[index2]])
							operando2 = pila_operandos.pop()
    		tipo = reglas.get((operando2[1], operador, operando1[1]), 'Error')
    		if tipo != 'Error':
				resultado = temporales.pop()
				cuadruplo.append([operador, operando2[0], operando1[0], resultado])
				contador_cuadruplo += 1
				if (operando1 == 'T1' or operando1 == 'T2' or operando1 == 'T3' or operando1 == 'T4' or operando1 == 'T5' or operando1 == 'T6' or
				    operando1 == 'T7' or operando1 == 'T8' or operando1 == 'T9' or operando1 == 'T10' or operando1 == 'T11' or operando1 == 'T12' or 
				    operando1 == 'T13' or operando1 == 'T14' or operando1 == 'T15' or operando1 == 'T16' or operando1 == 'T17' or operando1 == 'T18' or
				    operando1 == 'T19' or operando1 == 'T20'):
					temporales.append(operando1)
				elif (operando2 == 'T1' or operando2 == 'T2' or operando2 == 'T3' or operando2 == 'T4' or operando2 == 'T5' or operando2 == 'T6' or
				    operando2 == 'T7' or operando2 == 'T8' or operando2 == 'T9' or operando2 == 'T10' or operando2 == 'T11' or operando2 == 'T12' or 
				    operando2 == 'T13' or operando2 == 'T14' or operando2 == 'T15' or operando2 == 'T16' or operando2 == 'T17' or operando2 == 'T18' or
				    operando2 == 'T19' or operando2 == 'T20'):
					temporales.append(operando2)
				pila_operandos.append([resultado, tipo])
				dic_tipos[resultado] = tipo
    		else:
    			print('Error1')
    			exit(1)

def p_termp(p): 
    '''termp : DIVISION push_operator term 
             | TIMES push_operator term 
             | empty'''

def p_push_operator(p):
	'''push_operator : '''
	global pila_operadores
	if (p[-1]):
		pila_operadores.append(p[-1])

def p_factor(p): 
    '''factor : cons
              | LPAREN push_operator sexp RPAREN pop_parentesis 
              | empty'''

def p_pop_parentesis(p):
	'''pop_parentesis : '''
	pila_operadores.pop()


def p_cons(p): 
	'''cons : id
			| NUMINT int_type
			| NUMFLOAT float_type'''

def p_int_type(p): 
    '''int_type : '''
    global pila_operandos
    pila_operandos.append([p[-1], 'int'])


def p_float_type(p): 
    '''float_type : '''
    global pila_operandos
    pila_operandos.append([p[-1], 'float'])

def p_string_type(p):
	'''string_type : CTES'''
	global pila_operandos
	global variables_string
	pila_operandos.append([p[1]])
	variables_string = True

def p_id(p): 
    '''id : ID idp'''
    global pila_operandos
    pila_operandos.append(p[1])


def p_idp(p):
	'''idp : LPAREN RPAREN
		   | empty'''
	global Name_Functions
	global pila_ejecucion
	if (p[1] == '('):
		if (p[-1] in Name_Functions):
			salto = Name_Functions[p[-1]]
			cuadruplo.append(['gotoFun', ' ', ' ', str(salto)])
			pila_ejecucion.append(len(cuadruplo))
		else:
			print('Error. Funcion ' + p[-1] + ' no declarada previamente')
			exit(1)

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
    if p: 
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

archi = open('/Users/gerardogutierrez/Documents/ITESM/7 Semestre/Lenguajes y traductores/Traductor/Pruebas/test2.txt','r')
text = archi.read()
parser.parse(text)
archi.close()