#Zaplavnov 15.3
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)

X = df.iloc[:, :-1].to_numpy()
model = PCA()
model.fit(X)

x = model.components_
xt = np.transpose(x)
A = np.around(np.dot(x, xt), 14)
I = np.identity(len(x)) 
print(f"{'ортонормированный базис' if np.all(np.equal(A, I)) else 'не ортонормированный базис'}")