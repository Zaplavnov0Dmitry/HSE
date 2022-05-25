#4.5 Zaplavnov
import numpy as np
#Dna_1 = input('enter the first DNA sequence: ')
#Dna_2 = input('enter the second DNA sequence: ')

Dna_1 = 'CTGTCTCCTG'
Dna_2 = 'ATGAGTCTCT'

x = '-' + Dna_1 # добавляю прочерк, чтобы легче обращаться по индексу во время вызова функции "replacement_matrix"
y = '-' + Dna_2

transition_table = [[[] for j in range(len(Dna_2)+1)] for i in range(len(Dna_1)+1)]
table = [[ 0 for j in range(len(Dna_2)+1)] for i in range(len(Dna_1)+1)] # создаем с массив с n подмассивами, в которых m нулей
# n - это количество букв в первом слове, которое пишется по вертикили(по x) + 1(для гэпов)
# m - это количество букв во втором слове, которое пишется по горизнотали(по y) + 1(для гэпов)

for gap_y in range(len(y)): # заполняем гепы по горизонтали
	table[0][gap_y] = gap_y * (-10)
for gap_x in range(1, len(x)): # заполняем гепы по вертикали
	table[gap_x][0] = gap_x * (-10)


def replacement_matrix(x, y):
	if x == y:
		return 5
	elif x != y:
		return -4
	else:
		print('Что пошло не так при использовании функции "replacement_matrix" внутри функции "S"')

def S(i,j): # функция для заполнения таблицы
	if i == 0:
		return table[i][j]
	elif j == 0:
		return table[i][j]
	d = 10 # гэп
	step1 = S(i, j-1) - d # шаг со смещением по горизонтали вправо(по y)
	step2 = S(i-1, j-1) + replacement_matrix(x[i], y[j])
	step3 = S(i-1, j) - d # шаг со смещением по вертикали вниз(по x)

	if max(step1, step2, step3) == step1:
		transition_table[i][j] = [i, j-1]

		return step1
	elif max(step1, step2, step3) == step2:
		transition_table[i][j] = [i-1, j-1]

		return step2
	elif max(step1, step2, step3) == step3:
		transition_table[i][j] = [i-1, j]

		return step3
	else:
		print('Что-то пошло не так в функции "S"')

time = 0
for index_x in range(1, len(x)): # заполнение таблицы
	for index_y in range(1, len(y)):
		table[index_x][index_y] = S(index_x,index_y)
		time += 1
		print(time)

print(f'S_table\n{np.array(table)}')
for i in transition_table:
	print(i)

def build_alignment(transition_table, x, y):
	Dna1_alignment = []
	Dna2_alignment = []
	first_coordinates = [len(x)-1, len(y)-1]
	second_coordinates = transition_table[len(x)-1][len(y)-1]
	time = 0
	while first_coordinates != [0, 0]:
		if first_coordinates[0] == second_coordinates[0] and first_coordinates[1] > second_coordinates[1]:
			Dna1_alignment.append('-')
			Dna2_alignment.append(y[first_coordinates[1]])

			
		elif first_coordinates[0] != second_coordinates[0] and first_coordinates[1] != second_coordinates[1]:
			Dna1_alignment.append(x[first_coordinates[0]])
			Dna2_alignment.append(y[first_coordinates[1]])

		elif first_coordinates[0] > second_coordinates[0] and first_coordinates[1] == second_coordinates[1]:
			Dna1_alignment.append(x[first_coordinates[0]])
			Dna2_alignment.append('-')
		else:
			print('Что-то пошло не так')

		first_coordinates = [second_coordinates[0], second_coordinates[1]]
		second_coordinates = transition_table[second_coordinates[0]][second_coordinates[1]]
		time += 1
		print(time)
	return [Dna1_alignment[::-1], Dna2_alignment[::-1]]
D = build_alignment(transition_table, x, y)
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

print(f'score: {table[len(x)-1][len(y)-1]}')

