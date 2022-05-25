#Zaplavnov 12.2
from scipy.stats import *
N = 1000
n = 6
for i in range(N):
  x = norm(0, 1).rvs(n)
  y = norm(0, 1).rvs(n)
  if ttest_rel(x, y)[1] > 0.1 and ttest_ind(x, y)[1] < 0.05:
    print(f'x = {x}, y = {y}')
    break