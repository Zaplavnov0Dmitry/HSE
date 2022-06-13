#Zaplavnov 20.5
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import *
from sklearn.linear_model import *
from sklearn.metrics import *
from scipy.stats import *

N = 20
M = 10000
count = 0
np.random.seed(17)
for i in range(M):
  X = np.random.normal(loc=0, size=(N, 2))
  y = ['1']*10 + ['0']*10
  X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=17)
  model = LogisticRegression(penalty="none")

  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)

  if balanced_accuracy_score(y_test, y_pred) == 1:
    count += 1

print(count)
print(count/M)