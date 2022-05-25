#1.2 Zaplavnov
import numpy as np
list1 = input('Введите список чисел через запятую ').split(',')
#Делаем из строк числа
list1 = list(map(float,list1))
mean_list1 = np.mean(list1)
print(f'Среднее арифметическое = {mean_list1}')