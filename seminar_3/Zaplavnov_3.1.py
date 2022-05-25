#3.1 Zaplavnov
list1 = list(map(float, input('Введите массив чисел через пробел: ').split()))
index_start_item = 0

for j in list1:
	start_item = list1[index_start_item]
	min_item = start_item
	index_min_item = index_start_item
	for index in range(index_start_item,len(list1)):
		new_item = list1[index]
		if new_item < min_item:
			index_min_item = index
			min_item = new_item
	list1[index_start_item] = min_item
	list1[index_min_item] = start_item

	index_start_item += 1
print(list1)