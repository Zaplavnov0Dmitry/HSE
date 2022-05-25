#Zaplavnov bonus6_mod4
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import math 

from sklearn.datasets import *

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV
df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)
X = df.iloc[:, :-1].to_numpy()
y = df["Subtype"].to_numpy()

# получаем компонентны для PCA
model_PCA = PCA(n_components=2)
X_PCA = model_PCA.fit_transform(X)
df_PCA = pd.DataFrame()
df_PCA['Axis1'] = X_PCA[:, 0]
df_PCA['Axis2'] = X_PCA[:, 1]
df_PCA['class'] = y
sns.scatterplot(x='Axis1', y = 'Axis2', hue = 'class', data = df_PCA)
plt.savefig("bonus6_mod4_PCA.jpg")
plt.close()

# получаем компонентны для TSNE
model_TSNE = TSNE(n_components=2)
X_TSNE = model_TSNE.fit_transform(X)
df_TSNE = pd.DataFrame()
df_TSNE['t-SNE1'] = X_TSNE[:, 0]
df_TSNE['t-SNE2'] = X_TSNE[:, 1]
df_TSNE['class'] = y
sns.scatterplot(x='t-SNE1', y = 't-SNE2', hue = 'class', data = df_TSNE)
plt.savefig("bonus6_mod4_TSNE.jpg")

# модель
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classfication", KNeighborsClassifier())
])
params = {
    "classfication__n_neighbors": [1, 3, 5, 7],
    "classfication__weights": ["uniform", "distance"],
    "classfication__p": [1, 2]
}

model = GridSearchCV(
    model, params,
    scoring=make_scorer(accuracy_score),
    cv=RepeatedStratifiedKFold(n_splits=5, n_repeats=10, random_state=17)
)

# делаем модель на основе PCA
X = df_PCA.iloc[:, :-1].to_numpy()
y = df_PCA["class"].to_numpy()
model.fit(X, y)
print(f'лучшие параметры для PCA:', model.best_params_)
print(f'лучшее качество PCA:', model.best_score_)

# делаем модель на основе TSE
X = df_TSNE.iloc[:, :-1].to_numpy()
y = df_TSNE["class"].to_numpy()
model.fit(X, y)
print(f'лучшие параметры для t-SNE:', model.best_params_)
print(f'лучшее качество t-SNE:', model.best_score_)
