#Zaplavnov 9.1
import pandas as pd
import numpy as np

df_GNG4 = pd.read_csv("GNG4_exons.tsv", sep="\t", names=['chr', 'что-то', 'exon', 'start', 'end', '.', '-', '..1', 'лхм'])
df_SPRR4 = pd.read_csv("SPRR4_exons.tsv", sep="\t", names=['chr', 'что-то', 'exon', 'start', 'end', '.', '-', '..1', 'лхм'])

# считаем длину для GNG4
exon = []
start = df_GNG4['start']
end = df_GNG4['end']
for i, j in zip(start, end): # сделали список списков range по длине последовательности
  exon.append(set(range(i, j+1)))
exon_new = []
chet = 0
for i in exon:
	for j in exon:
		if i == j:
			continue
		if len(i & j) != 0:
			chet += 1
			if (i | j) not in exon_new:
				exon_new.append(i | j)
	if chet == 0:
		exon_new.append(i)
	chet = 0
set_exon_new = set()
for i in exon_new:
	set_exon_new = set_exon_new | i
len_GNG4 = len(set_exon_new)


# считаем длину для SPRR4
exon = []
for i, j in zip(df_SPRR4['start'], df_SPRR4['end']): # сделали список списков range по длине последовательности
  exon.append(set(range(i, j+1)))
exon_new = []
chet = 0
for i in exon:
	for j in exon:
		if i == j:
			continue
		if len(i & j) != 0:
			chet += 1
			if (i | j) not in exon_new:
				exon_new.append(i | j)
	if chet == 0:
		exon_new.append(i)
	chet = 0
set_exon_new = set()
for i in exon_new:
	set_exon_new = set_exon_new | i
len_SPRR4 = len(set_exon_new)

print(f'len_SPRR4: {len_SPRR4}')
print(f'len_GNG4: {len_GNG4}')