#3.4 Zaplavnov
'''list1 = list(map(float, input('Введите массив чисел через пробел: ').split()))
def dj(mass):
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [0]*len(a)
b[0], b[1] = a[0], a[1]
for i in range(2, len(a)):
  b[i] = min(b[i - 1], b[i - 2]) + a[i]
print(f'жадный поиск: {sum(a)}, динамический способ: {b[-1]}, отношение: {sum(a)/b[-1]}')