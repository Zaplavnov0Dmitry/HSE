#2.2 Zalavnov
import math
n = int(input('Введите количество элементов в массиве: '))
max_element_list = - math.inf

for i in range(n):
	element_list = float(input())
	if element_list > max_element_list:
		second_max_element_list = max_element_list
		max_element_list = element_list
	elif element_list > second_max_element_list and element_list < max_element_list:
		second_max_element_list = element_list

print(f'Второй по величине элемент в введенном массиве: {second_max_element_list}')