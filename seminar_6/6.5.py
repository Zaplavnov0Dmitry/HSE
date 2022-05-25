#Zaplavnov 6.5
#Дан целочисленный массив 𝑛, вывести границы всех его подмассивов с нулевой суммой. Ограничение по времени —𝑂(𝑛2).
#Дописать программу, чтобы она обрабатывала массив только из нулей
mass = list(map(float, input().split()))
#mass = [1, 2, -3, 6, 1, 2, -1, 3, -11, 5]
#mass = [1, 2, 3, 4, 5, -3, -6, 7]
coordinates = []
dic = {}
sum_mass = 0
for i in range(len(mass)):
	sum_mass += mass[i]
	if mass[i] == 0: # если прибавляемое значение равно
		coordinates.append([i, i])
	elif sum_mass in dic: # проверяю есть ли такая сумма уже в словаре
		if [dic[sum_mass] + 1, i] not in coordinates:
			coordinates.append([dic[sum_mass] + 1, i])
	if sum_mass == 0:
		if [0, i] not in coordinates:
			coordinates.append([0, i])
	dic[sum_mass] = i
print(coordinates)

