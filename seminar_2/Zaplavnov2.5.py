#2.5 Zaplavnov
x = [9,8,1]
y = [7,1]
score = 0
sum_x_y = []

if len(x) >= len(y):
	min_length_number = len(y)
	max_number = x
elif len(x) <= len(y):
	min_length_number = len(x)
	max_number = y


for i in range(min_length_number):
	
	counts = x[i] + y[i] + score

	counts = str(counts)
	if len(counts) == 1:
		score = 0
		sum_x_y.append(counts)
	elif len(counts) == 2:
		score = int(counts[0])
		sum_x_y.append(counts[-1])
	else:
		print('Что-то не так')
if len(x) != len(y):
	sum_x_y.append(max_number[-1] + score)
elif score != 0:
	sum_x_y.append(score)
print(sum_x_y)