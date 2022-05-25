#bonus 10

import numpy as np
import pandas as pd
TCGA = pd.read_csv("TCGA-COAD_cancer_normal.tsv", sep="\t", index_col=0)
TCGA = np.log2(TCGA + 1) # логарифмировали значения
col_all = TCGA.columns
for i in col_all:
  TCGA = TCGA.loc[TCGA[i] != 0]# убрал гены, которые в образцах содержат ноль
sum_rows = TCGA.sum(axis=1) # посчитали сумму ридов(логарифмированную) для гена во всех образцах
TCGA['Pseudo'] = sum_rows / len(col_all) # добавили псевдообразец 