#Zaplavnov 14.1
from scipy.stats import * 
import seaborn as sns
x = list(range(0, 100))
y = [100**i for i in x]
print(pearsonr(x, y))
print(spearmanr(x, y))
