#3.2 Zaplavnov
list1 = list(map(int, input('Введите отсортированный массив целых чисел через пробел: ').split()))
number = int(input('Введите искомое число: '))
def search(list1, item):
	low = 0 # нижняя граница индексов
	high = len(list1) - 1 # верхняя граница индексов
	while low <= high: 
		middle = int((low + high)/2) # находим средний элемент 
		element_list = list1[middle] # проверяем средний элемент
		if element_list == item:
			return print('Искомое число найдено')
		if element_list < item: # рассматриваем правый массив чисел от серединного индекса
			low = middle + 1
		elif element_list > item: # рассматриваем левый массив чисел от серединного индекса
			high  = middle - 1
		else:
			print('Что-то пошло не так')
	return print('Искомое число не принадлежит введенному массиву')

search(list1, number)
