#Zaplavnov 5.2
import time
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
#Spike
from SARS_CoV_2_genes import gene_coordinates
start = coord(align, gene_coordinates["Spike"][0] - 1)
end = coord(align, gene_coordinates["Spike"][1])
len_spike = end - start
spike_now_miss_counter = 0

for j in range(start, end):
	for i in range(1, len(align)):
		if align[i, j] != align[0, j] and align[i, j] != '-':
			spike_now_miss_counter += 1
#NSP12
from SARS_CoV_2_genes import gene_coordinates
start = coord(align, gene_coordinates['NSP12'][0] - 1)
end = coord(align, gene_coordinates["NSP12"][1])
len_nsp12 = end - start
nsp12_now_miss_counter = 0

for j in range(start, end):
	for i in range(1, len(align)):
		if align[i, j] != align[0, j] and align[i, j] != '-':
			nsp12_now_miss_counter += 1
	

print(f'Число мутаций в Spike {spike_now_miss_counter}')
print(f'Число мутаций в NSP12 {nsp12_now_miss_counter}')
print(f'Длина белка Spike {len_spike}')
print(f'Длина белка NSP12 {len_nsp12}')
print(f'Среднее число мутаций в белке Spike\n{spike_now_miss_counter/(len(align) * len_spike)}')
print(f'Среднее число мутаций в белке NSP12\n{nsp12_now_miss_counter/(len(align) * len_nsp12)}')



