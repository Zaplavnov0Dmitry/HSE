#Zaplavnov 6.4
from Bio import SeqIO
k = int(input('Введиет k: '))
sequences = SeqIO.read("SARS-CoV-2.fasta", "fasta")
sequences = str(sequences.seq)
start = 0
end = k
dic = {}
time = 0
for i in range(len(sequences) - k + 1):
	subsequence = sequences[start: end]
	if subsequence not in dic:
		dic[subsequence] = []
	dic[subsequence].append([start, end])
	start += 1
	end += 1
	time += 1
	print(time)

print(f'len {len(dic)}')
for i in dic:
	if len(dic[i]) != 1:
		print('blinb')
		break
#При 𝑘 = 33 каждому фрагменту соответствует ровно одна позиция