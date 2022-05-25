#4.1 Zaplavnov
DNA = input('enter the DNA sequence: ')

def complementary_sequence(DNA_seq):
	DNA_seq = DNA_seq.upper()
	New_Dna = []
	for i in DNA_seq:
		if i == 'T':
			New_Dna.append('A')
		if i == 'A':
			New_Dna.append('T')
		if i == 'C':
			New_Dna.append('G')
		if i == 'G':
			New_Dna.append('C')   
	print(f"DNA: 3'-{''.join(New_Dna)}-5'")


complementary_sequence(DNA)