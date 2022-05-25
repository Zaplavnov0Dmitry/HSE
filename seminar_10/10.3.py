#Zaplavnov 10.3
from scipy.stats import *
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
lambd = 17
n = 100
list_x = np.linspace(0, 10, num=100)
df = pd.DataFrame({
	'x': list_x,
	'pdf_x': [expon.pdf(x, loc=0, scale=1) for x in list_x]
	 })
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.barplot(x='x', y='pdf_x', data=df,ci=10, n_boot=100)
plt.savefig("PDF_10.3.jpg")

rv = expon(scale = 1/lambd) # cоздали случайную величину с фиксированной лямбдой
print(f'Матожидание: {rv.mean()}')
print(f'Дисперсия: {rv.var()}')