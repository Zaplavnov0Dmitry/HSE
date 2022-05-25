from Bio import AlignIO
align = AlignIO.read("SARS_CoV_2_Russia_aligned.fasta", "fasta")
print(align)