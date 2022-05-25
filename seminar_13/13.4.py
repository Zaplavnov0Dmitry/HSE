#Zaplavnov 13.4
list1 = []
with open('all_genes.txt') as f:
	for i in f:
		list1.append(i.replace('\n', ''))
import random
list1 = random.sample(list1, 1000)

with open('1000_genes.txt', 'w') as file:
	for gene in list1:
		file.write(gene) 
		file.write('\n')
