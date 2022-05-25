#1.4 Zaplavnov
n = int(input('n = '))
n_max = float(input())
for i in range(n-1): 
	n_new = float(input())
	if n_new > n_max:
		n_max = n_new
print(f'Максимальное число из списка = {n_max}')