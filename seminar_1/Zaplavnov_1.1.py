#1.1
a = float(input('Введите a = '))
b = float(input('Введите b = '))
c = float(input('Введите c = '))

if a == 0:
	print(f'{𝑏}*x+{𝑐}= 0')
	x = -c/b
	print(f'x = {x}')
else:
	print(f'{𝑎}*x^2+{𝑏}*x+{𝑐}= 0')
	D = b**2 - 4*a*c
	if D > 0:
		x1 = (-b+(D)**(1/2))/(2*a)
		x2 = (-b-(D)**(1/2))/(2*a)
		print(f'x1 = {x1} \nx2 = {x2}')
	elif D == 0:
		x = -b/(2*a)
		print(f'x = {x}')
	elif D < 0:
		print('Нет корней в действительных числах')
	else:
		print('Что-то пошло не так')