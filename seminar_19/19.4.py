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

y_pred = model.predict(X_test)
M = confusion_matrix(y_test, y_pred)
TP = M[1, 1]
TN = M[0, 0]
FN = M[1, 0]
FP = M[0, 1]
TPR = TP / (TP + FN)
TNR = TN / (TN + FP)
print(f'TPR: {TPR}\nTNR: {TNR}\n')

plot_roc_curve(model, X_test, y_test)
plt.plot([0, 1], [0, 1], color="navy", linestyle="--")
plt.plot(1 - TNR, TPR, "x", c="red")
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.savefig("ROC1.png")

genes = ['TRIP13', 'UBE2C', 'ZWINT', 'EPN3', 'KIF4A', 'ECHDC2', 'MTFR1', 'CX3CR1', 'SLC7A5', 'ABAT', 'CFAP69']
df = df[genes]
# мы используем True/False из датасета an, чтобы отсортировать датасет df
X_train = df.loc[an['Dataset type'] == 'Training'].to_numpy() # выборка для обучения модели
y_train = an.loc[an['Dataset type'] == 'Training', 'Class'].to_numpy()

X_test = df.loc[an['Dataset type'] == 'Validation'].to_numpy() # выборка для обучения модели
y_test = an.loc[an['Dataset type'] == 'Validation', 'Class'].to_numpy()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

M = confusion_matrix(y_test, y_pred)
TP = M[1, 1]
TN = M[0, 0]
FN = M[1, 0]
FP = M[0, 1]
TPR = TP / (TP + FN)
TNR = TN / (TN + FP)
print(f'TPR: {TPR}\nTNR: {TNR}\n')

plot_roc_curve(model, X_test, y_test)
plt.plot([0, 1], [0, 1], color="navy", linestyle="--")
plt.plot(1 - TNR, TPR, "x", c="red")
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.savefig("ROC2.png")

