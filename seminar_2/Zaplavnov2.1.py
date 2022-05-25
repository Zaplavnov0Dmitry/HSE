#2.1 Zaplavnov
x = float(input('Введите искомое число: '))
counter_x = 0
for i in range(int(input('Введите количество элементов в массиве: '))):
	element_list = float(input())
	if element_list == x:
		counter_x += 1
	
print(f'Число вхождений в заданный массив: {counter_x}')