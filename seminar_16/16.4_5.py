#Zaplavnov 16.4
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import math 

def list_str(title):
	title = title.split()
	title_new = []
	symbole = [',', '/', '.', ':', '!', '?', '[', ']', ';', '"', '"', '(', ')']
	for i in title:
		for sym in symbole:
			i = i.replace(sym, '').lower()
		title_new.append(i)
	title_new2 = []
	for ind in range(len(title_new)):
		if len(title_new[ind]) != 1 and len(title_new[ind]) != 2:
			title_new2.append(title_new[ind])
	return title_new2

def jac(title1, title2):
	set1 = set(title1)
	set2 = set(title2)
	jaccard = len(set1 & set2) / len(set1 | set2)
	return 1 - jaccard

df_cancer = pd.read_csv("cancer-set.csv")
df_virus = pd.read_csv("virus-set.csv")

'''
title_list = []
for can, vir in zip(list(df_cancer['Title'])[:1000], list(df_virus['Title'])[:1000]):
	words_can = list_str(can)
	words_vir = list_str(vir)
	title_list.append(words_can)
	title_list.append(words_vir)

df_words = pd.DataFrame()
df_words['title'] = title_list

num = 0
for i in title_list:
	jac_tit = []
	for j in title_list:
		jac_tit.append(jac(i, j))
	num+=1
	df_words[' '.join(i)] = jac_tit
'''
title_list = list(df_cancer['Title'])[:1000] +  list(df_virus['Title'])[:1000]

df_words = pd.DataFrame()
df_words['title'] = title_list
X = []
num = 0
for i in tqdm(title_list):
	jac_tit = []
	for j in title_list:
		jac_tit.append(jac(list_str(i), list_str(j)))
	num+=1
	X.append(jac_tit)



class_title = []
for i in title_list:
	if 'virus' in i:
		class_title.append('virus')
	elif 'cancer' in i:
		class_title.append('cancer')
	else:
		class_title.append('None')

df_words['class_title'] = class_title
print(f'num: {num}')
#X = df_words.iloc[:,1:-1]
#print(df_words.columns)
#print(len(df_words.columns))

#print(set(df_words['title']) - set(df_words.columns)) 
model_TSNE = TSNE(n_components=2, metric="precomputed")
X_TSNE = model_TSNE.fit_transform(X)
df_TSNE = pd.DataFrame()
df_TSNE['t-SNE1'] = X_TSNE[:, 0]
df_TSNE['t-SNE2'] = X_TSNE[:, 1]
df_TSNE['class'] = class_title
sns.scatterplot(x='t-SNE1', y = 't-SNE2', hue = 'class', data = df_TSNE)
plt.savefig("16.4_5_df_TSNE.jpg")
plt.close()

model_PCA = PCA(n_components=2)
X_PCA = model_PCA.fit_transform(X)
df_PCA = pd.DataFrame()
df_PCA['Axis1'] = X_PCA[:, 0]
df_PCA['Axis2'] = X_PCA[:, 1]
df_PCA['class'] = class_title
sns.scatterplot(x='Axis1', y = 'Axis2', hue = 'class', data = df_PCA)
plt.savefig("16.4_5_df_PCA.jpg")