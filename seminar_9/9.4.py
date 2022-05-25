#Zaplavnov 9.4
import pandas as pd

size_factors = [0.35219656, 0.39439086, 0.73057344, 1.66138079, 
1.60002838, 1.48313616, 1.28046971, 0.92434274, 1.59306799, 1.34997698] # посчитанные медианы

df = pd.read_csv("TCGA-COAD_cancer_normal.tsv", sep="\t", index_col=0).sort_index() # сортируем, чтобы при делении на длину генов строчки в таблицах совпадали
gl = pd.read_csv("gene_lengths.tsv", sep="\t", index_col=0).sort_index()

# Получение шкалы RPKM  и применение median of ratios
RPM = df.div(df.sum(axis=0), axis=1) * 1e+6 # про суммировали по всем строчкам для каждого столбца и поделила в каждом столбце на свое значение - номировка на глубину
DESeq2_RPM = RPM.div(size_factors, axis=1) #делим значения во всех образцах на соответсвующие множители median of ratios
DESeq2_RPKM = DESeq2_RPM.div(gl["Length"], axis=0) * 1000


col_all = DESeq2_RPKM.columns
for i in col_all:
  DESeq2_RPKM = DESeq2_RPKM.loc[DESeq2_RPKM[i] != 0] # удаляю все строки содержащие 0
DESeq2_RPKM['standard deviation'] = DESeq2_RPKM.std(axis=1) # добавляю столбец стандартного отклонения для строки
DESeq2_RPKM = DESeq2_RPKM.sort_values(by = "standard deviation") 
print(DESeq2_RPKM.iloc[:10])