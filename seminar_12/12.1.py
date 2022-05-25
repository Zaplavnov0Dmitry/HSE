#Zaplavnov 12.1
import pandas as pd
from scipy.stats import *
N = 1000
n = 6
for i in range(N):
  x = norm(0, 1).rvs(n)
  y = norm(0, 1).rvs(n)
  if ttest_rel(x, y)[1] < 0.05 and ttest_ind(x, y)[1] > 0.1:
    print(f'x = {x}, y = {y}')
    break
