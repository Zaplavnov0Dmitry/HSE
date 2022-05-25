#1.5 Zaplavnov
n = int(input('n = '))
counter = 0
for i in range(n):
	n_new = float(input())
	if (n_new >= 2 and
		n_new % 2 == 0 and
		n_new % 17 == 0):
		counter += 1
print(f'Количество кратных 17 четных положительных чисел из списка = {counter}')
