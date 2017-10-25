import ply.yacc as yacc
from reglasSemanticas import reglas
from lexico import tokens

error 				= None 	#Variable para saber si hay error 
contador_repetidas	= 0  	#Contador para las variables repetidas
contador			= 0  	#Contador para saber cuantas variables hay
Name				= {} 	#Diccionario para guardar las variables
Name_tipos			= {}	#Diccionario para guardar las variables con su tipo
Name_repetidas		= {}	#Diccionario para guardar las variables repetidas
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
pila_tipos 			= []
pila_constante		= []
pila_saltos			= []
aux_variable1		= None
aux_variable2		= None
print_type			= 0


def p_programa(p):
	'''programa : PROGRAM ID var_declaration function_declaration main_declaration POINT'''
	global aux_variable1
	global aux_variable2
	global contador_cuadruplo
	cuadruplo.append(['END'])
	print(cuadruplo)
	#print(Name)
	i = 0
	contador_tipos = 0
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
					if (pila_tipos[contador_tipos] == ['int']):
						if aux_variable1 == True:
							op1 = int(float(variable1))
						else:
							op1 = int(float(aux[1]))
						if aux_variable2 == True:
							op2 = int(float(variable2))
						else:
							op2 = int(float(aux[2]))
					elif (pila_tipos[contador_tipos] == ['float']):
						if aux_variable1 == True:
							op1 = float(variable1)
						else:
							op1 = float(aux[1])
						if aux_variable2 == True:
							op2 = float(variable2)
						else:
							op2 = float(aux[2])
					contador_tipos += 1
					ans = op1 + op2
					for index in range(len(aux)):
						dic_temp[aux[3]] = ans
						break
				
				elif aux[index] == '-':
					if (pila_tipos[contador_tipos] == ['int']):
						if aux_variable1 == True:
							op1 = int(float(variable1))
						else:
							op1 = int(float(aux[1]))
						if aux_variable2 == True:
							op2 = int(float(variable2))
						else:
							op2 = int(float(aux[2]))
					elif (pila_tipos[contador_tipos] == ['float']):
						if aux_variable1 == True:
							op1 = float(variable1)
						else:
							op1 = float(aux[1])
						if aux_variable2 == True:
							op2 = float(variable2)
						else:
							op2 = float(aux[2])
					
					contador_tipos += 1
					ans = op1 - op2
					for index in range(len(aux)):
						dic_temp[aux[3]] = ans
						break
				
				elif aux[index] == '*':
					if (pila_tipos[contador_tipos] == ['int']):
						if aux_variable1 == True:
							op1 = int(float(variable1))
						else:
							op1 = int(float(aux[1]))
						if aux_variable2 == True:
							op2 = int(float(variable2))
						else:
							op2 = int(float(aux[2]))
					elif (pila_tipos[contador_tipos] == ['float']):
						if aux_variable1 == True:
							op1 = float(variable1)
						else:
							op1 = float(aux[1])
						if aux_variable2 == True:
							op2 = float(variable2)
						else:
							op2 = float(aux[2])
					
					contador_tipos += 1
					ans = op1 * op2
					for index in range(len(aux)):
						dic_temp[aux[3]] = ans
						break
				
				elif aux[index] == '/':
					if (pila_tipos[contador_tipos] == ['float']):
						if aux_variable1 == True:
							op1 = int(float(variable1))
						else:
							op1 = int(float(aux[1]))
						if aux_variable2 == True:
							op2 = float(variable2)
						else:
							op2 = float(aux[2])
					
					contador_tipos += 1
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

			elif (aux[index] == '>'):
				op1 = float(aux[1])
				op2 = float(aux[2])
				
				ans = op1 > op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == '<'):
				op1 = float(aux[1])
				op2 = float(aux[2])
				
				ans = op1 < op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == '!='):
				op1 = float(aux[1])
				op2 = float(aux[2])
				
				ans = op1 != op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == '=='):
				op1 = float(aux[1])
				op2 = float(aux[2])
				
				ans = op1 == op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == '>='):
				op1 = float(aux[1])
				op2 = float(aux[2])
				
				ans = op1 >= op2
				for index in range(len(aux)):
					dic_temp[aux[3]] = ans
					break

			elif (aux[index] == '<='):
				op1 = float(aux[1])
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
				print(ans)
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
				print(ans)
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
 
			break

		i += 1
		if cuadruplo[i] == ['END']:
			print(dic_temp)
			break

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
	Name[p[1]] = 0
	if (p[2] == '='):
		Name[p[1]] = p[3]
	Name_tipos[p[1]] = 'int'

def p_variable_float_list(p):
	'''variable_float_list : ID SEMMICOLON
						   | ID COMMA variable_float_list
						   | ID ASSIGN NUMFLOAT SEMMICOLON 
						   | ID ASSIGN NUMFLOAT COMMA variable_float_list'''
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
	'''function_declaration : function_1
							| empty'''

def p_function_1(p):
	'''function_1 : FUNCTION ID LPAREN RPAREN LKEY estatuto RKEY function_1
				  | FUNCTION ID LPAREN RPAREN LKEY estatuto RKEY '''

def p_main_declaration(p):
	'''main_declaration : MAIN LPAREN RPAREN LKEY estatuto RKEY '''


def p_estatuto(p):
	'''estatuto : ciclo_for estatuto
				| ciclo_if estatuto
				| ciclo_while estatuto
				| read_process estatuto
				| print_process estatuto
				| call_process estatuto
				| id_asignacion estatuto
				| empty'''

def p_call_process(p):
	'''call_process : CALL ID LPAREN RPAREN SEMMICOLON'''

def p_print_process(p):
	'''print_process : PRINT LPAREN print_1 RPAREN SEMMICOLON'''

def p_print_1(p):
	'''print_1 : id print_aux_1 print_prima_1'''

def p_print_aux_1(p):
	'''print_aux_1 : '''
	global print_type
	print_type = 1

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

def p_read_process(p):
	'''read_process : READ LPAREN sexp RPAREN SEMMICOLON'''

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
	'''ciclo_for : FOR LPAREN ID ASSIGN sexp SEMMICOLON sexp SEMMICOLON ID ASSIGN sexp RPAREN LKEY estatuto RKEY'''

#Ciclo while
def p_ciclo_while(p):
	'''ciclo_while : WHILE ciclo_while_1 LPAREN sexp RPAREN LKEY estatuto RKEY ciclo_while_2'''
	global cuadruplo
	global contador_cuadruplo
	global ciclo_while
	falso = pila_saltos.pop()
	retorno = pila_saltos.pop()
	cuadruplo.append(['goto', ' ', ' ', str(retorno)])
	cuadruplo[falso] = [cuadruplo[falso][0], cuadruplo[falso][1], ' ', str(len(cuadruplo))]
	contador_cuadruplo += 1
	ciclo_while = True

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
				print('Error')
				exit(1)


def p_sexprima(p): 
    '''sexprima : AND push_operator sexp
                | OR push_operator sexp
                | empty'''

def p_expression(p):
	'''expression : cuadruplo_2 expressionp'''

def p_expression(p): 
    '''expression : exp'''
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
    			print('Error')
    			exit(1)
  
def p_expressionp(p): 
    '''expressionp : LT push_operator exp
                   | GT push_operator exp
                   | LTEQ push_operator exp 
                   | GTEQ push_operator exp
                   | EQ push_operator exp
                   | NEQ push_operator exp 
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
				pila_tipos.append([tipo])
    		else:
    			print('Error')
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
				pila_tipos.append([tipo])
    		else:
    			print('Error')
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
              | LPAREN expression RPAREN'''

def p_cons(p): 
    '''cons : id
    		| NUMINT int_type
    		| NUMFLOAT float_type'''

def p_int_type(p): 
    '''int_type :'''
    global pila_operandos
    pila_operandos.append([p[-1], 'int'])


def p_float_type(p): 
    '''float_type :'''
    global pila_operandos
    pila_operandos.append([p[-1], 'float'])


def p_id(p): 
    '''id : ID idp'''

def p_idp(p): 
    '''idp : LSQUARE sexp RSQUARE 
           | LPAREN idpp RPAREN
           | empty'''
    global pila_operandos
    res = p[-1]
    pila_operandos.append([res])

def p_idpp(p): 
    '''idpp : sexp idppaux
            | empty''' 

def p_idppaux(p): 
    '''idppaux : COMMA idpp 
               | empty''' 

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
    if p: 
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

archi = open('/Users/gerardogutierrez/Documents/ITESM/7 Semestre/Lenguajes y traductores/Traductor/Pruebas/test1.txt','r')
text = archi.read()
parser.parse(text)
archi.close()


# Funcion que checa si hay variables repetidas
def check_error(variable):
	global contador_repetidas
	global index_repetidas
	contador_repetidas = 0
	for aux2 in Name_repetidas:
		if (variable == Name_repetidas[aux2]):
			return False
	for aux in Name:
		if (variable == Name[aux]):
			contador_repetidas += 1	
			if (contador_repetidas == 2):
				index_repetidas += 1
				Name_repetidas[index_repetidas] = var
				return True
	return False

# Imprime la tabla de simbolos
#print("---------------------- Tabla de simbolos --------------------")
#for aux in Name:
#	var = Name[aux]
#	print(str(aux) + " " + var)

for aux in Name:
	var = Name[aux]
	if (check_error(var) == True):
		print("Error. Variable " + var + " repetida")