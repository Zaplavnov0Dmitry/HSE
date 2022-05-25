#Zaplavnov 10.2
from scipy.stats import *
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
s = 0
for k in range(1, 1001):
	s += 1/(k**3)
c = 1/s
print(f'Сумма ряда: {s}')
print(f'Номировочная константа: {c}')
df = pd.DataFrame({
	'x': list(range(1, 11)),
	'PMF_x': [x *c*(1/(x**3)) for x in list(range(1, 11))]
	 })
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.barplot(x='x', y='PMF_x', data=df,ci=10, n_boot=100)
plt.savefig("PMF_10.2.jpg")
