#4.4 Zaplvnov
import numpy as np
#Dna_1 = input('enter the first DNA sequence: ')
#Dna_2 = input('enter the second DNA sequence: ')

Dna_1 = 'CTGTCTCCTG'
Dna_2 = 'ATGAGTCTCT'

x = '-' + Dna_1 # добавляю прочерк, чтобы легче обращаться по индексу во время вызова функции "replacement_matrix"
y = '-' + Dna_2

table = [[0 for j in range(len(Dna_2)+1)] for i in range(len(Dna_1)+1)] # создаем с массив с n подмассивами, в которых m нулей
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
	return max(step1, step2, step3)
time = 0
for index_x in range(1, len(x)):
	for index_y in range(1, len(y)):
		table[index_x][index_y] = S(index_x,index_y)
		time += 1
		print(time)


print(np.array(table))
print(f'score: {table[len(x)-1][len(y)-1]}')
