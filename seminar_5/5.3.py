#Zaplavnov 5.3
from Bio import AlignIO
from Bio.Seq import Seq
align = AlignIO.read('SARS_CoV_2_Russia_aligned.fasta', 'fasta')
def coord (aln, local):
	non_gaps = 0
	for i in range(len(aln[0])):
		if aln[0][i] != '-':
			non_gaps += 1
		if non_gaps - 1 == local:
			return i

from SARS_CoV_2_genes import gene_coordinates
start = coord(align, gene_coordinates["Spike"][0] - 1)
end = coord(align, gene_coordinates["Spike"][1])

max_miss_counter = 0
a_now_miss_counter = 0
c_now_miss_counter = 0
t_now_miss_counter = 0
g_now_miss_counter = 0
max_miss_coordinates = 0
nuc = ''
time = 0
for j in range(start, end):
	for i in range(1, len(align)):
		if align[i, j] != align[0, j] and align[i, j] != '-' and align[i, j] == 'a':
			a_now_miss_counter += 1
		elif align[i, j] != align[0, j] and align[i, j] != '-' and align[i, j] == 'c':
			c_now_miss_counter += 1
		elif align[i, j] != align[0, j] and align[i, j] != '-' and align[i, j] == 't':
			t_now_miss_counter += 1
		elif align[i, j] != align[0, j] and align[i, j] != '-' and align[i, j] == 'g':
			g_now_miss_counter += 1
	time = time+ 1
	print(time)

	if a_now_miss_counter > max_miss_counter:
		max_miss_counter = a_now_miss_counter
		max_miss_coordinates = j
		nuc = 'a'
	elif c_now_miss_counter > max_miss_counter:
		max_miss_counter = c_now_miss_counter
		max_miss_coordinates = j
		nuc = 'c'
	elif t_now_miss_counter > max_miss_counter:
		max_miss_counter = t_now_miss_counter
		max_miss_coordinates = j
		nuc = 't'
	elif g_now_miss_counter > max_miss_counter:
		max_miss_counter = g_now_miss_counter
		max_miss_coordinates = j
		nuc = 'g'
	a_now_miss_counter = 0
	c_now_miss_counter = 0
	t_now_miss_counter = 0
	g_now_miss_counter = 0
print('-----')
print(f'{align[0, max_miss_coordinates]} -> {nuc}')
print(max_miss_counter)
print(max_miss_coordinates)


print(len(align[0, :max_miss_coordinates].seq.replace('-', '')))


do = len(align[0, :max_miss_coordinates].seq.replace('-', ''))//3
posle = len(align[0, :max_miss_coordinates].seq.replace('-', '')) % 3
dogol = coord(align, do)
cod = dogol + 3
print(align[0, dogol:cod].seq)


