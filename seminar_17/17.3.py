#Zaplavnov 17.3
import pandas as pd
import numpy as np


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestCentroid

from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score


df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)
X = df.iloc[:, :-1].to_numpy()
y = df["Subtype"].to_numpy()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=17
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classfication", NearestCentroid())
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print('общая точность', accuracy_score(y_pred, y_test))
df = pd.DataFrame()
df['y_test'] = y_test
df['y_pred'] = y_pred
uniq = df['y_test'].unique()
for subtype in uniq:
	df_sub = df.loc[df['y_test']==subtype]
	print(subtype)
	print(accuracy_score(df_sub['y_pred'], df_sub['y_test']))