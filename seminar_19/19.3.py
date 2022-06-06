#Zaplavnov 19.3
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.tree import *
from sklearn.ensemble import *
from sklearn.metrics import *
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import train_test_split

df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)
X = df.iloc[:, :-1].to_numpy()
y = df["Subtype"].to_numpy()

model = RandomForestClassifier()
params = {'max_depth': range(1, 10, 2)}
model = GridSearchCV(
	model, params,
	scoring=make_scorer(balanced_accuracy_score),
	cv = RepeatedStratifiedKFold(n_repeats=10, random_state=17)
)
model.fit(X, y)

print(f'лучший параметр:', model.best_params_)
print(f'лучшее качество:', model.best_score_)
