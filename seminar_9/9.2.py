#Zaplavnov 9.2
import numpy as np
import pandas as pd
TCGA = pd.read_csv("TCGA-COAD_cancer_normal.tsv", sep="\t", index_col=0)
TCGA = np.log2(TCGA + 1) # логарифмировали значения
col_all = TCGA.columns
for i in col_all:
  TCGA = TCGA.loc[TCGA[i] != 0]# убрал гены, которые в образцах содержат ноль
sum_rows = TCGA.sum(axis=1) # посчитали сумму ридов(логарифмированную) для гена во всех образцах
TCGA['Pseudo'] = sum_rows / len(col_all) # добавили псевдообразец
for i in col_all:
  TCGA[i] = TCGA[i] - TCGA['Pseudo'] # вычли псевдообразец - вычеслили отношения всех значений к псевдообразцу
all_col_median = list(TCGA.median())[:len(col_all)] # получили логарифмированные значения медиан по образцам(столбцам)
for i, j in zip(col_all, all_col_median):
	print(i, ': ', 2**j) # вывели множители(медианы) в обыной шкале