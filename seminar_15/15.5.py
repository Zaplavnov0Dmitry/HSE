#Zaplavnov 15.5
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)

gene_list = ['ESR1', 'PGR', 'ERBB2', 'MKI67']
expr_list = []
subtypes = []
genes = []
for gene in gene_list:
    expr_list += list(df[gene])
    subtypes += list(df['Subtype'])
    for j in range(len(df[gene])):
        genes.append(gene)

pic_df = pd.DataFrame({'Expression': expr_list, 'Gene': genes, 'Subtype': subtypes})

fig = plt.gcf()
fig.set_size_inches(25, 10)
pic = sns.boxplot(x='Subtype', y='Expression', hue='Gene', data=pic_df)
plt.savefig('boxplot1.pdf')
plt.clf()

