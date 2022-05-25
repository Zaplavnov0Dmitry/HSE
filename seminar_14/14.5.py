#Zaplavnov 14.5
import networkx as nx
from scipy.stats import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('healthy_breast.tsv', sep="\t", index_col=0)
df = df.sample(n=1000, axis = 0)
# посчитали матрицу корреляции
r_s = spearmanr(df, axis=1)[0]
df_corr = pd.DataFrame(r_s, index = df.index, columns = df.index)
# построили сеть коэкспрессии
graph = nx.Graph()
for i in df_corr.index:
	for j in df_corr.index:
		if i == j:
			continue
		if abs(df_corr.loc[i, j]) > 0.8:
			graph.add_edge(i, j)
x = [np.log2(len(graph.edges(i))+1) for i in df_corr.index]
plt.hist(x)