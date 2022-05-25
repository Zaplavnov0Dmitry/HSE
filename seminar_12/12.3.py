#Zaplavnov 12.3
from scipy.stats import *
import pandas as pd
df = pd.read_csv('breast_cancer_1000_genes.tsv', sep="\t", index_col=0)
counter = 0
for gene in df.index:
	p = shapiro(df.loc[gene])[1]
	if p > 0.05:
		counter += 1
print(counter/len(df.index))