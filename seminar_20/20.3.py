#Zaplavnov 20.3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import *

df = pd.read_csv('sgn.csv')
model = LassoCV() # метод наименьших квадратов
N = 1000
x = df['x'][:N].to_numpy()
y = df['y'][:N].to_numpy()
X = np.hstack([np.hstack([np.array([np.sin(m*x)]).T,np.array([np.cos(m*x)]).T]) for m in range(1,N+1)])
model.fit(X,y)
print(f'm={N} коэффицент:{model.coef_}')
print(f'm={N} b0:{model.intercept_}')
y_pred = model.predict(X)
sns.lineplot(x=x,y=y_pred)
sns.scatterplot(x=x, y=y)
plt.savefig(f'LassoCV m={N}.jpg')