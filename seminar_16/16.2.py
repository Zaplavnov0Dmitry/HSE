#Zaplavnov 16.2
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import math 

df = pd.read_csv("human_coronavirus_aln_scores.tsv", sep="\t", index_col=0)
print(df)
model_TSNE = TSNE(n_components=2, perplexity=15)
class_v = ['HCoV-HKU1'] *20 + ['MERS-CoV']*20 + ['SARS-CoV-2']*20 + ['HCoV-229E']*20 +  ['HCoV-NL63']*20 +  ['HCoV-OC43']*20 + ['SARS-CoV']*20
X_TSNE = model_TSNE.fit_transform(df)
df_TSNE = pd.DataFrame()
df_TSNE['t-SNE1'] = X_TSNE[:, 0]
df_TSNE['t-SNE2'] = X_TSNE[:, 1]
df_TSNE['class'] = class_v
sns.scatterplot(x='t-SNE1', y = 't-SNE2', hue = 'class', data = df_TSNE)
plt.savefig("16.2_df_TSNE.jpg")