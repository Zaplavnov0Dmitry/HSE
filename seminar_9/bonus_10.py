#bonus 10
import numpy as np
import pandas as pd
TCGA = pd.read_csv("TCGA-COAD_cancer_normal.tsv", sep="\t", index_col=0)

# проверка
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import Formula
from rpy2.robjects import pandas2ri
pandas2ri.activate()
from rpy2.robjects.packages import importr
edgeR = importr("edgeR")
counts = pd.read_csv("TCGA-COAD_cancer_normal.tsv", sep="\t", index_col=0)# чтение нужного файла
# Technical requirement, never mind
groups = pd.DataFrame({"smth1": ["smth2"] * len(counts.columns)}, index = counts.columns)
# Calculate normalization factors
dds = edgeR.DESeqDataSetFromMatrix(countData=counts, colData=groups, design=Formula("~ 1"))
dds = edgeR.estimateSizeFactors_DESeqDataSet(dds)
size_factors = edgeR.sizeFactors_DESeqDataSet(dds)
print('тутт')
print(size_factors)

# ---




TCGA = np.log2(TCGA + 1) # логарифмировали значения
col_all = TCGA.columns
for i in col_all:
  TCGA = TCGA.loc[TCGA[i] != 0]# убрал гены, которые в образцах 

sum_rows = TCGA.sum(axis=1) # посчитали сумму ридов(логарифмированную) для гена во всех образцах
TCGA['Pseudo'] = sum_rows / len(col_all) # добавили псевдообразец 