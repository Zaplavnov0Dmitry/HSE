#Zaplavnov 13.2
from scipy.stats import *
contr_health = 5200
contr_nohealth = 4800
exp_health = 5000
exp_nohealth = 5000
cont_table = [
[contr_health, contr_nohealth],
[exp_health, exp_nohealth]]
print(fisher_exact(cont_table))
