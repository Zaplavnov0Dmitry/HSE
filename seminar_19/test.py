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
df = pd.read_csv('BRCA_pam50.tsv', sep = '\t', index_col = 0)

X = df.iloc[:, :-1].to_numpy()
y = df["Subtype"].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    stratify=y, 
                                                    random_state=17)
model = RandomForestClassifier()
params = {'max_depth': range(1, 10, 2)}
clf = GridSearchCV(model, param_grid = params,  cv = RepeatedStratifiedKFold(n_repeats=10))
clf.fit(X_train, y_train)

print(clf.best_params_)
print(balanced_accuracy_score(y_test, clf.predict(X_test)))