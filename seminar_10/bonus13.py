#bonus13
import numpy as np
import seaborn as sns
counts_mut = 100
tests = 100
len_kmer = 20
len_reads = 100
np.random.seed(42)
list_probability_right_kmer = []
right_kmer = 0
counts_kmers = len_reads - len_kmer + 1
for mut in range(counts_mut):
	probability_right_kmer = 0
	for i in range(tests):
		read = list(range(len_reads))
		for mistake_index in np.random.randint(0, len_reads, mut):
			# учитывается, что две мутации могут произойти в одном и том же месте
			read[mistake_index] = 'x'
			start_index = 0
			end_inex = len_kmer
			right_kmer = 0
			counts_kmers = len_reads - len_kmer + 1
			for iter_kmers in range(counts_kmers):
				k_mer = read[start_index:end_inex]
				if 'x' not in k_mer:
					right_kmer += 1
				start_index += 1
				end_inex += 1
		probability_right_kmer += right_kmer/counts_kmers
	list_probability_right_kmer.append(probability_right_kmer/tests)

sns.barplot(x=list(range(1, counts_mut+1)), y=list_probability_right_kmer)