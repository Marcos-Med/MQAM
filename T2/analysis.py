import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew
import statsmodels.api as sm

def plot(data, column):
    skewness = skew(df[column])
    kurt = kurtosis(df[column], fisher=True)
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    sns.histplot(data[column], kde=True, ax=axs[0])
    axs[0].set_title(f'{column} - Histograma\nAssimetria: {skewness:.2f}, Curtose: {kurt:.2f}')
    sm.qqplot(data[column], line='s', ax=axs[1])
    axs[1].set_title(f'{column} - Q-Q Plot')
    plt.tight_layout()
    plt.show()

column = 'avaliacao_da_critica'
df = pd.read_csv("T2/Transform.csv")
plot(df, column)