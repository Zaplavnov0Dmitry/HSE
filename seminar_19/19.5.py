#Zaplavnov 19.5
import pandas as pd
import numpy as np

from scipy.stats import *


df = pd.read_pickle("bc_data.pkl")
an = pd.read_pickle("bc_ann.pkl")
genes = 0
# мы используем True/False из датасета an, чтобы отсортировать датасет df
X_train = df.loc[an['Dataset type'] == 'Training'] # выборка для обучения модели
X_test = df.loc[an['Dataset type'] == 'Validation'] # выборка для обучения модели
for col in df.loc[an['Dataset type'] == 'Training'].columns:
	t = ttest_ind(X_train[col], X_test[col])
	if t[1] < 0.05:
		genes += 1
print(genes)
print(genes/len(df.loc[an['Dataset type'] == 'Training'].columns))