#2.4 Zaplavnov
import sys
x = input('Введите количество элементов в массиве: ')
index_end_element = -1 
if len(x) == 0:
	print('Вы не ввели число')
	sys.exit(0)
if len(x) == 1:
	print('не палиндром')
	sys.exit(0)


if len(x)%2 == 0:
	for i in range(int(len(x)/2)):
		if x[i] != x[index_end_element]:
			print('не палиндром')
			sys.exit(0)
		index_end_element -= 1
	print('палиндром')
elif len(x)%2 != 0:
	for i in range(int((len(x)+1)/2 -1)):
		if x[i] != x[index_end_element]:
			print('не палиндром')
			sys.exit(0)
		index_end_element -= 1
	print('палиндром')