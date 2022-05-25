#Zaplavnov 5.4
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio import SeqIO
import numpy as np
import math

aligner = PairwiseAligner()
aligner.mode = "global"
aligner.substitution_matrix = substitution_matrices.load("NUC.4.4")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
cov_name = []
cov_seq = []
sequences = SeqIO.parse("task_4_refseq.fasta", "fasta")

for seq in sequences:
	cov_name.append(seq.id)
	cov_seq.append(str(seq.seq))

matrix_align = [[0 for t in range(len(cov_seq))] for m in range(len(cov_seq))]
start = 0
for i in range(len(cov_seq)):
	for j in range(start, len(cov_seq)):
		if i == j:
			continue
		matrix_align[i][j] = aligner.score(cov_seq[i], cov_seq[j])
	start += 1


print(np.array(matrix_align))

max_score = -math.inf
coord_max_score = []
min_score = math.inf
coord_min_score = []
start = 0
for i in range(len(cov_seq)):
	for j in range(start, len(cov_seq)):
		if i == j:
			continue
		if matrix_align[i][j] > max_score:
			max_score = matrix_align[i][j]
			coord_max_score = [i, j]
		if matrix_align[i][j] < min_score:
			min_score = matrix_align[i][j]
			coord_min_score = [i, j]
	start += 1

print(f'{cov_name[coord_max_score[0]]} and {cov_name[coord_max_score[1]]} have max score {max_score}')
print(f'{cov_name[coord_min_score[0]]} and {cov_name[coord_min_score[1]]} have min score {min_score}')
