#Zaplavnov 8
import numpy  as np
#BWT = list(input())
BWT = list('GT$TTATAAA')
first_part = sorted(BWT)
time = 0
for i in range(len(BWT)-1):
	for j in range(len(BWT)):
		first_part[j] = BWT[j] + first_part[j]

	first_part.sort()

for i in first_part:
	print(i)
