import pandas as pd
import numpy as ny
import scipy.stats as stats

column = 'orcamento'
df = pd.read_csv("T2/Transform.csv")
skewness = stats.skew(df[column])
kurt = stats.kurtosis(df[column], fisher=True)

N = len(df)

SE_skew = ny.sqrt(6 / N)
SE_kurt = ny.sqrt(24 / N)

Z_skew = skewness/SE_skew
Z_kurt = (kurt)/SE_kurt
print(column)
print(f"Assimetria: {skewness}, Z-score Assimetria: {Z_skew}")
print(f"Curtose Excessiva: {kurt}, Z-score Curtose: {Z_kurt}")