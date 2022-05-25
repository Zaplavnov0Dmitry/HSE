#Zaplavnov 14.3
from scipy.stats import *
import pandas as pd
df = pd.read_csv('healthy_breast.tsv', sep="\t", index_col=0)
list_cor = []
for i in df.index:
	cor_s = spearmanr(df.loc[i],df.loc['SPI1'])[0]
	if abs(cor_s) > 0.8 and i != 'SPI1':
		list_cor.append(i)
with open('SPI1_cor_genes.txt', 'w') as file:
	for gene in list_cor:
		file.write(gene) 
		file.write('\n')