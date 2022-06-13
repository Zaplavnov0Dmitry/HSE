#Zaplavnov 20.4
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import *
from sklearn.linear_model import *
from sklearn.svm import SVC
from sklearn.metrics import *

df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)
df = df.loc[df["Subtype"].isin(["Luminal A", "Luminal B"])]

X = df.iloc[:, :-1].to_numpy()
y = df["Subtype"].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=17)
# SVC
model_SVC = SVC(kernel="linear", class_weight="balanced")
model_SVC.fit(X_train, y_train)
y_pred = model_SVC.predict(X_test)
print('SVC', balanced_accuracy_score(y_test, y_pred))
k = model_SVC.coef_[0] # коэффициенты перед кажддым геном
k_sort = np.argsort(np.abs(k))[::-1][:2] # получим список индексов генов отсортированный по их коэффициентам 
genes = df.columns[k_sort].to_list()

# Logistic
model_log = LogisticRegression(class_weight='balanced', C=0.01, penalty='l1', solver='liblinear')
model_log.fit(X_train, y_train)
y_pred = model_log.predict(X_test)
print('log: ',balanced_accuracy_score(y_test, y_pred))

# SVC 2 genes
df = df.loc[df["Subtype"].isin(["Luminal A", "Luminal B"]), genes + ['Subtype']]

X = df.iloc[:, :-1].to_numpy()
y = df["Subtype"].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=17)
# SVC
model_SVC = SVC(kernel="linear", class_weight="balanced")
model_SVC.fit(X_train, y_train)
y_pred = model_SVC.predict(X_test)
print('SVC 2 genes', balanced_accuracy_score(y_test, y_pred))