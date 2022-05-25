#Zaplavnov 9.5
import pandas as pd
import numpy as np
size_factors = [0.35219656, 0.39439086, 0.73057344, 1.66138079, 
1.60002838, 1.48313616, 1.28046971, 0.92434274, 1.59306799, 1.34997698] # посчитанные медианы

df = pd.read_csv("TCGA-COAD_cancer_normal.tsv", sep="\t", index_col=0).sort_index() # сортируем, чтобы при делении на длину генов строчки в таблицах совпадали
gl = pd.read_csv("gene_lengths.tsv", sep="\t", index_col=0).sort_index()

# Получение шкалы RPKM  и применение median of ratios
RPM = df.div(df.sum(axis=0), axis=1) * 1e+6 # про суммировали по всем строчкам для каждого столбца и поделила в каждом столбце на свое значение - номировка на глубину
DESeq2_RPM = RPM.div(size_factors, axis=1) #делим значения во всех образцах на соответсвующие множители median of ratios
DESeq2_RPKM = RPM.div(gl["Length"], axis=0) * 1000

col_all = DESeq2_RPKM.columns
for i in col_all:
  DESeq2_RPKM = DESeq2_RPKM.loc[DESeq2_RPKM[i] != 0] # удаляю все строки содержащие 0

DESeq2_RPKM_tumor = DESeq2_RPKM.iloc[:, :5].mean(axis=1) # посчитали сумму ридов для здоровых клеток
DESeq2_RPKM_healthy = DESeq2_RPKM.iloc[:, 5:].mean(axis=1) # посчитали сумму ридов для опухолевых клеток
DESeq2_RPKM['ratio_of_healthy_cells_to_tumor'] = DESeq2_RPKM_tumor / DESeq2_RPKM_healthy # во сколько раз выше экспрессия в опухолевых клетках
DESeq2_RPKM['ratio_of_tumor_cells_to_healthy'] = DESeq2_RPKM_healthy / DESeq2_RPKM_tumor # во сколько раз выше экспрессия в здоровых клетках
DESeq2_RPKM['max_ratio'] = np.maximum(DESeq2_RPKM['ratio_of_healthy_cells_to_tumor'], DESeq2_RPKM['ratio_of_tumor_cells_to_healthy'])
# Если значение в строке положительное, значит экспрессия  этого гена в опухолевых клетках выше, чем в нормальных

DESeq2_RPKM = DESeq2_RPKM.sort_values(by = 'max_ratio', ascending = False) # сортируем по модулю разницы
print(DESeq2_RPKM.iloc[:10])