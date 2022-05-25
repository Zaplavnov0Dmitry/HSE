#2.3 Zaplavnov
import math
n = int(input('Введите количество элементов в массиве: '))
max_element_list = - math.inf
second_max_element_list = - math.inf
third_max_element_list = - math.inf 

for i in range(n):
	element_list = float(input())
	if element_list > max_element_list:
		third_max_element_list = second_max_element_list
		second_max_element_list = max_element_list
		max_element_list = element_list
	elif element_list > second_max_element_list and element_list < max_element_list:
		third_max_element_list = second_max_element_list 
		second_max_element_list = element_list
	elif element_list > third_max_element_list and element_list < second_max_element_list:
		third_max_element_list = element_list


print(f'Третий по величине элемент в введенном массиве: {third_max_element_list}')