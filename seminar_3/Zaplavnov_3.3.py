#3.3 Zaplavnov
list1 = input('Введите массив чисел через пробел: ').split()
list2 = list(map(int, list1))
number_digit = len(str(max(list2)))
bit_digit = []
for i in list1:
 if len(i) != number_digit:
 	number_zero = number_digit - len(i)
 	j = '0' * number_zero + i
 	bit_digit.append(j)
 elif len(i) == number_digit:
 	bit_digit.append(i)

def sort(input_arary, index):
	mass0 = []
	mass1 = []
	mass2 = []
	mass3 = []
	mass4 = []
	mass5 = []
	mass6 = []
	mass7 = []
	mass8 = []
	mass9 = []
	for i in input_arary:
		if int(i[index]) == 0:
			mass0.append(i)
		elif int(i[index]) == 1:
			mass1.append(i)
		elif int(i[index]) == 2:
			mass2.append(i)
		elif int(i[index]) == 3:
			mass3.append(i)
		elif int(i[index]) == 4:
			mass4.append(i)
		elif int(i[index]) == 5:
			mass5.append(i)
		elif int(i[index]) == 6:
			mass6.append(i)
		elif int(i[index]) == 7:
			mass7.append(i)
		elif int(i[index]) == 8:
			mass8.append(i)
		elif int(i[index]) == 9:
			mass9.append(i)
	gen_mass = mass0 + mass1 + mass2 + mass3 + mass4 + mass5 + mass6 + mass7 + mass8 + mass9
	return gen_mass
def radix_sort(input_arary, number_digit):
	for index in range(-1,-(number_digit)-1,-1):
		print(index)
		input_arary = sort(input_arary, index)
	print(input_arary)
		

radix_sort(bit_digit, number_digit)