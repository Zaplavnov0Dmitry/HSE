#Zaplavnov bonus_6
from Bio import SeqIO
from Bio import AlignIO
import numpy as np
from itertools import *
import re
k_mer = 10
k_mer_all = set()
for i in product('ATGC', repeat = k_mer):
    k_mer_all.add(''.join(list(i)))

sequences = SeqIO.parse("GRCh38_latest_genomic.fna", "fasta")

def set_k_mer(seq, k):
    import re
    has_special = re.compile("|".join(map(re.escape, "NMR"))).search
    if len(seq) % 2 != 0 or len(seq) <= 2*k:
        start_left = 0
        end_left = k
        start_right = len(seq) - k
        end_right = len(seq)
        set_k = set()
        for iteration in range(len(seq) - k + 1):
            subsequence_left = seq[start_left: end_left]
            subsequence_right = seq[start_right: end_right]
            if not bool(has_special(subsequence_left)):
                set_k.add(subsequence_left)
            if not bool(has_special(subsequence_right)):
                set_k.add(subsequence_right)
            if start_left >= start_right and end_left >= end_right:
                break
            start_left += 1
            end_left += 1
            start_right -= 1
            end_right -= 1
        return set_k
    start_seq1 = 0
    end_seq1 = int(len(seq) / 2)
    start_seq2 = int(len(seq) / 2)
    end_seq2 = len(seq)
    seq1 = seq[start_seq1: end_seq1]
    seq2 = seq[start_seq2: end_seq2]
    set_seq1 = set_k_mer(seq1, k)
    set_seq2 = set_k_mer(seq2, k)
    comm_set = set_seq1 | set_seq2
    middle_start_left = end_seq1 - (k-1)
    middle_end_left = end_seq1 + 1
    middle_start_right = end_seq1 - 1
    middle_end_right = end_seq1 + (k-1)
    for i in range(k-1):
        middle_subseq_left = seq[middle_start_left: middle_end_left]
        middle_subseq_right = seq[middle_start_right: middle_end_right]
        comm_set.add(middle_subseq_left)
        comm_set.add(middle_subseq_right)
        if middle_start_left >= middle_start_right and middle_end_left >= middle_end_right:
            break
        middle_start_left += 1
        middle_end_left += 1
        middle_start_right -= 1
        middle_end_right -= 1
    return comm_set
comm_kmers_set = set()
inter = 0
for i in sequences:
    seqq = str(i.seq).upper()
    print(f'len(seqq): {len(seqq)}')
    setkmerss = set_k_mer(seqq, k_mer)
    comm_kmers_set = comm_kmers_set.union(setkmerss)
    if len(k_mer_all - comm_kmers_set) == 0:
        print('YYYYYEEESSSSS')
        break
    print(f'len(comm_kmers_set): {len(comm_kmers_set)}')
    print(f'len(k_mer_all): {len(k_mer_all)}')
    inter += 1
    print(f'iter: {inter}')
vv = k_mer_all - comm_kmers_set
print(f'len(vv): {len(vv)}')
print(f'len(comm_kmers_set): {len(comm_kmers_set)}')
f = open('k_mers_10_not.txt', 'w')
for item in vv:
    s = item + '\n'
    f.write(s)
f.close()