#Zaplavnov 14.2
from scipy.stats import * 
import numpy as np
N = 100000
for i in range(1000):
  x = list(norm(0, 1).rvs(99)) + [1000]
  e = norm(0, 5).rvs(100)
  y = [x[i] + e[i] for i in range(100)]
  if pearsonr(x, y)[0] > 0.9 and spearmanr(x, y)[0] < 0.1:
    print(pearsonr(x, y))
    print(spearmanr(x, y))
    sns.scatterplot(x,y)
    break
	