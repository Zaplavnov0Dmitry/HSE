#Zaplavnov 16.1
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import math 

N = 10000
primes = [2]
for i in range(3,N,2):
	prime_digits = True
	for j in range(2, int(np.sqrt(i)) + 1):
		if i % j == 0:
			prime_digits = False
			break
	if prime_digits:
		primes.append(i)
y_class = []
vector_numbers = []
for i in range(2, N):
	y_class.append(1 if i in primes else 0)
	vector = []
	for p in primes:
		if i % p ==0:
			for j in list(range(int(np.sqrt(i)) + 1))[::-1]:
				if i % p**j ==0:
					vector.append(j)
					break
		else:
			vector.append(0)
	vector_numbers.append(vector)

model_PCA = PCA(n_components=2)
model_TSNE = TSNE(n_components=2, perplexity=50)

X_PCA = model_PCA.fit_transform(vector_numbers)
df_PCA = pd.DataFrame()
df_PCA['Axis1'] = X_PCA[:, 0]
df_PCA['Axis2'] = X_PCA[:, 1]
df_PCA['primes'] = y_class
sns.scatterplot(x='Axis1', y = 'Axis2', hue = 'primes', data = df_PCA)
plt.savefig("16.1_df_PCA.jpg")
plt.close()


X_TSNE = model_TSNE.fit_transform(vector_numbers)
df_TSNE = pd.DataFrame()
df_TSNE['t-SNE1'] = X_TSNE[:, 0]
df_TSNE['t-SNE2'] = X_TSNE[:, 1]
df_TSNE['primes'] = y_class
sns.scatterplot(x='t-SNE1', y = 't-SNE2', hue = 'primes', data = df_TSNE)
plt.savefig("16.1_df_TSNE.jpg")