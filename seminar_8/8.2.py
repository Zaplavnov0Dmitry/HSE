#Zaplavnov_8.2
#X = input() + '$'
X = 'ATATATTAG' + '$'
mass = []
start = 0
for i in range(len(X)):
	mass.append(X[start :])
	start += 1
mass.sort()
print(mass)
mass_suf = []
for i in mass:
	mass_suf.append(len(X)-len(i) + 1)
print(mass_suf)
