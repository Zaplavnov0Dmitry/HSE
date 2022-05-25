#Zaplavnov_8.3
#X = '$' + input()
#S = list(map(int, input().split()))
X = '$' + 'ATATATTAG'
S = [10, 8, 1, 3, 5, 9, 7, 2, 4, 6]
def BWX(X, S):
	seq = ''
	for i in S:
		seq += X[(i-1)]
	return seq
print(BWX(X, S))

def C(X,a):
	sort_X = sorted(X)
	try:
		count = sort_X.index(a)
		return count
	except:
		print('Такого элемента нет в строке')
symbol = input('Введите $/A/C/G/T: ')
print(f'C(X, {symbol}) = {C(X, symbol)}')