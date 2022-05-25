#Zaplavnov 12.4
from scipy.stats import *
import pandas as pd
import numpy as np
df_FPKM = pd.read_csv('colon_cancer_tumor_vs_normal_unpaired_FPKM.tsv', sep="\t", index_col=0)
df_DESeq2 = pd.read_csv('DESeq2_results_unpaired.tsv', sep="\t", index_col=0)

df_FPKM['p-value'] = [ttest_ind(df_FPKM.loc[i].iloc[:5], df_FPKM.loc[i].iloc[5:10])[1] for i in df_FPKM.index]
df_FPKM['padj'] = np.minimum(df_FPKM['p-value']*len(df_FPKM), 1)
df_FPKM = df_FPKM.sort_values('padj')
df_DESeq2 = df_DESeq2.sort_values('padj')
print(df_DESeq2.head())
print(df_FPKM.head())