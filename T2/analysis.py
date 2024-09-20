import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew
import statsmodels.api as sm

def qqplot(data, title):
    sm.qqplot(data, line='s')
    plt.title(f'Q-Q Plot de {title}')
    plt.show()

column = 'avaliacao_da_critica'
df = pd.read_csv("T2/Transform.csv")
skewness = skew(df[column])
kurt = kurtosis(df[column], fisher=True)
title = f'{column} Curtose: {kurt:.4f}, Assimetria: {skewness:.4f}'
qqplot(df[column], title)