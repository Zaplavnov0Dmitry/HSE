#Zaplavnov 19.4
import pandas as pd
import numpy as np

from sklearn.svm import SVC
from sklearn.metrics import *
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import *


df = pd.read_pickle("bc_data.pkl")
an = pd.read_pickle("bc_ann.pkl")

# мы используем True/False из датасета an, чтобы отсортировать датасет df
X_train = df.loc[an['Dataset type'] == 'Training'].to_numpy() # выборка для обучения модели
y_train = an.loc[an['Dataset type'] == 'Training', 'Class'].to_numpy()

X_test = df.loc[an['Dataset type'] == 'Validation'].to_numpy() # выборка для обучения модели
y_test = an.loc[an['Dataset type'] == 'Validation', 'Class'].to_numpy()

model = SVC(kernel="linear", class_weight="balanced")
model.fit(X_train, y_train)

print(balanced_accuracy_score(y_train, model.predict(X_train)))
print(balanced_accuracy_score(y_test, model.predict(X_test)))
genes = ['TRIP13', 'UBE2C', 'ZWINT', 'EPN3', 'KIF4A', 'ECHDC2', 'MTFR1', 'CX3CR1', 'SLC7A5', 'ABAT', 'CFAP69']
df = df[genes]
print(df)
# мы используем True/False из датасета an, чтобы отсортировать датасет df
X_train = df.loc[an['Dataset type'] == 'Training'].to_numpy() # выборка для обучения модели
y_train = an.loc[an['Dataset type'] == 'Training', 'Class'].to_numpy()

X_test = df.loc[an['Dataset type'] == 'Validation'].to_numpy() # выборка для обучения модели
y_test = an.loc[an['Dataset type'] == 'Validation', 'Class'].to_numpy()
model.fit(X_train, y_train)

print(balanced_accuracy_score(y_train, model.predict(X_train)))
print(balanced_accuracy_score(y_test, model.predict(X_test)))


