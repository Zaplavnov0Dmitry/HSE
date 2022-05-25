#Zaplavnov 15.4
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)
X = df.iloc[:, :-1].to_numpy()
matrix = df.iloc[:, :-1].to_numpy()
model = PCA()
model.fit(X)

X_pca = model.transform(X)
df.iloc[:, :-1] = X_pca

df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)
X = df.iloc[:, :-1].to_numpy()

matrix -= matrix.mean(axis=0)
cov_matrix = -np.cov(matrix.T)
values, vectors = np.linalg.eig(cov_matrix)
explained_variances = []
for i in range(len(values)):
    explained_variances.append(round(values[i] / np.sum(values), 7))

print(np.array(explained_variances))
print(model.explained_variance_ratio_)