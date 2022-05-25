#3.5
import math
list1 = list(map(float, input('Введите массив чисел через пробел: ').split()))

max_start = 0
max_end = 0
curr_sum = 0
new_sum = 0
max_sum = float(-math.inf)
start = 0
end = 0

for index in range(len(list1)):
	new_sum = curr_sum + list1[index]
	end = index
	if new_sum > max_sum:
		max_sum = new_sum
		max_start = start
		max_end = end
	 
	if new_sum < 0:
		curr_sum = 0
		start = index + 1
		end = index + 1
		continue
	
	curr_sum = new_sum

print(f"max_sum = {max_sum} \nmax_start = {max_start} \nmax_end = {max_end}")