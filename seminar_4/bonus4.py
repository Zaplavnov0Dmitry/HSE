#bonus4 Zaplavnov
#4.5 Zaplavnov
import numpy as np
#Dna_1 = input('enter the first DNA sequence: ')
#Dna_2 = input('enter the second DNA sequence: ')
Dna_1 = 'CTGTCTCCTG'
Dna_2 = 'ATGAGTCTCT'
#Dna_1 = 'CTCGA'
#Dna_2 = 'CTA'

x = '-' + Dna_1 # добавляю прочерк, чтобы легче обращаться по индексу во время вызова функции "replacement_matrix"
y = '-' + Dna_2

table_A = [[ 0 for j in range(len(y))] for i in range(len(x))]
table_B = [[ 0 for j in range(len(y))] for i in range(len(x))]
transition_table = [[[] for j in range(len(Dna_2)+1)] for i in range(len(Dna_1)+1)]
table = [[ 0 for j in range(len(Dna_2)+1)] for i in range(len(Dna_1)+1)] # создаем с массив с n подмассивами, в которых m нулей
# n - это количество букв в первом слове, которое пишется по вертикили(по x) + 1(для гэпов)
# m - это количество букв во втором слове, которое пишется по горизнотали(по y) + 1(для гэпов)

#Выполняем граничные условия
#Заполняем таблицу S
for gap_y in range(1, len(y)): # заполняем гэпы по горизонтали 
	table[0][gap_y] = -10 - 0.5*(gap_y - 1)
for gap_x in range(1, len(x)): # заполняем гэпы по вертикали 
	table[gap_x][0] = -10 - 0.5*(gap_x - 1)
#Заполняем таблицу A
for el_y in range(1, len(Dna_2)+1): # заполняем гэпы по горизонтали 
	table_A[1][el_y] = table[0][el_y] - 10
for el_z in range(0, len(Dna_2)+1):
	table_A[0][el_z] = 'end'
for el_z in range(0, len(Dna_1)+1):
	table_A[el_z][0] = 'end'
#Заполняем таблицу B
for el_x in range(1, len(Dna_1)+1): # заполняем гэпы по вертикали 
	table_B[el_x][1] = table[el_x][0] - 10
for el_z in range(0, len(Dna_2)+1):
	table_B[0][el_z] = 'end'
for el_z in range(0, len(Dna_1)+1):
	table_B[el_z][0] = 'end'


def replacement_matrix(x, y):
	if x == y:
		return 5
	elif x != y:
		return -4
	else:
		print('Что пошло не так при использовании функции "replacement_matrix" внутри функции "S"')

def A(i,j): # функция для заполнения таблицы A
	if i == 0 or j == 0:
		if table_A[i][j] == 'end':
			return S(i, j)
		elif table_A[i][j] != 'end':
			return table_A[i][j]
	if table_A[i][j] != 0:
		return table_A[i][j]

	e = 0.5
	d = 10
	stepA1 = A(i-1, j) - e
	stepA2 = S(i-1, j) - d
	table_A[i][j] = max(stepA1, stepA2)
	return max(stepA1, stepA2)

def B(i, j): # функция для заполнения таблицы B
	if i == 0 or j == 0:
		if table_B[i][j] == 'end':
			return S(i, j)
		elif table_B[i][j] != 'end':
			return table_B[i][j]
	if table_B[i][j] != 0:
		return table_B[i][j]
	e = 0.5
	d = 10
	stepB1 = B(i, j-1) - e
	stepB2 = S(i, j-1) - d
	table_B[i][j] = max(stepB1, stepB2)
	return max(stepB1, stepB2)

def S(i,j): # функция для заполнения таблицы S
	if i == 0 or j == 0:
		return table[i][j]
	elif table[i][j] != 0:
		return table[i][j]
	d = 10 # гэп
	step1 = B(i, j) # шаг со смещением по горизонтали вправо(по y)
	step2 = S(i-1, j-1) + replacement_matrix(x[i], y[j])
	step3 = A(i, j) # шаг со смещением по вертикали вниз(по x)
	if i == 10 and j == 10:
		print(step1)
		print(step2)
		print(step3)
	if table[i][j-1] == B(i, j-1):
		if max(step1, step2, step3) == step1:
			transition_table[i][j] = [i, j-1]
			table[i][j] = step1
			return '0'

		elif max(step1, step2, step3) == step2:
			transition_table[i][j] = [i-1, j-1]
			table[i][j] = step2
			return '0'

		elif max(step1, step2, step3) == step3:
			transition_table[i][j] = [i-1, j]
			table[i][j] = step3
			return '0'

	elif table[i][j-1] == A(i-1, j-1):
		if max(step1, step2, step3) == step3:
			transition_table[i][j] = [i-1, j]
			table[i][j] = step3
			return '0'

		elif max(step1, step2, step3) == step1:
			transition_table[i][j] = [i, j-1]
			table[i][j] = step1
			return '0'

		elif max(step1, step2, step3) == step2:
			transition_table[i][j] = [i-1, j-1]
			table[i][j] = step2
			return '0'
	if max(step1, step2, step3) == step3:
		if i == 8 and j == 9:
			print('step3')
		transition_table[i][j] = [i-1, j]
		table[i][j] = step3
		return '0'
	elif max(step1, step2, step3) == step2:
		if i == 8 and j == 9:
			print('step2')
		transition_table[i][j] = [i-1, j-1]
		table[i][j] = step2
		return '0'
	
	elif max(step1, step2, step3) == step1:
		if i == 8 and j == 9:
			print('step1')
		transition_table[i][j] = [i, j-1]
		table[i][j] = step1
		return '0'
	else:
		print('Что-то пошло не так в функции "S"')

for index_x in range(1, len(x)): # заполнение таблицы
	for index_y in range(1, len(y)):
		S(index_x,index_y)
print('table_S\n',np.array(table), sep = '') # показываем заполненную таблицу(S) с очками
for i in transition_table: # показываем таблицу с координатами от какой ячейка мы перешли, чтобы получить max очки
	print(i)


def build_alignment(transition_table, x, y):
	Dna1_alignment = []
	Dna2_alignment = []
	first_coordinates = [len(x)-1, len(y)-1]
	second_coordinates = transition_table[len(x)-1][len(y)-1]
	while first_coordinates != [0, 0]:
		if first_coordinates[0] == second_coordinates[0] and first_coordinates[1] > second_coordinates[1]:
			Dna1_alignment.append('-')
			Dna2_alignment.append(y[first_coordinates[1]])

			
		elif first_coordinates[0] > second_coordinates[0] and first_coordinates[1] > second_coordinates[1]:
			Dna1_alignment.append(x[first_coordinates[0]])
			Dna2_alignment.append(y[first_coordinates[1]])

		elif first_coordinates[0] > second_coordinates[0] and first_coordinates[1] == second_coordinates[1]:
			Dna1_alignment.append(x[first_coordinates[0]])
			Dna2_alignment.append('-')
		else:
			print('Что-то пошло не так')

		first_coordinates = [second_coordinates[0], second_coordinates[1]]
		second_coordinates = transition_table[second_coordinates[0]][second_coordinates[1]]
	return [Dna1_alignment[::-1], Dna2_alignment[::-1]]
D = build_alignment(transition_table, x, y)
def show_alignment(D):
	D1 = D[0]
	D2 = D[1]
	mezh = ''
	for x1,y1 in zip(D1, D2):
		if x1 == '-' or y1 == '-':
			mezh += ' '
		elif x1 == y1:
			mezh += '|'
		elif x1 != y1:
			mezh += '*'
		else:
			print('Что-то пошло не так')
	print(''.join(D1))
	print(mezh)
	print(''.join(D2))
show_alignment(D)
print(f'score: {table[len(x)-1][len(y)-1]}')
