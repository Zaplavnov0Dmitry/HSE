#open_table
import pandas as pd
df = pd.read_csv('DESeq2.tsv', sep = '\t')
gencode = pd.read_csv('gencode.v34.types.tsv', sep = '\t')
# добавили тип гена
df['Type'] = [None for i in range(len(df))]
for gene1,gene2 in zip(df['Gene'], gencode['Gene']):
  if gene1 == gene2:
    df['Type'] = gencode['Type']

df.to_csv('DESeq2_with_type.tsv', sep = '\t')