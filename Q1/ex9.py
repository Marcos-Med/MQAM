import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew
import statsmodels.api as sm

def loadDataSet(fileCSV):
    dataFrame = pd.read_csv(fileCSV)
    return dataFrame

def isNormal(data):
    skewness = skew(data)
    kurt = kurtosis(data, fisher=True)
    print(f'Curtose: {kurt:.4f}, Assimetria: {skewness:.4f}')
    if abs(skewness) < 0.5 and abs(kurt) < 0.5:
        print("Distribuição próxima da normalidade")
    else:
        print("Distribuição provavelmente não normal")

def qq_plot(data, title):
    sm.qqplot(data, line='s')
    plt.title(f'Q-Q Plot de {title}')
    plt.show()

def main():
    data = loadDataSet("T1/Update.csv")
    columns = ['popularidade', 'voto_popular', 'orcamento', 'receita', 'duracao', 'avaliacao_da_critica']
    data['avaliacao_da_critica'] = data['avaliacao_da_critica'].str.rstrip('%').astype('float') / 100
    for coluna in columns:
         # Cálculo de assimetria e curtose
        skewness = skew(data[coluna])
        kurt = kurtosis(data[coluna], fisher=True)  # Fisher=True faz com que a curtose para distribuição normal seja 0

        # Criar uma nova figura para os gráficos
        fig, axs = plt.subplots(1, 2, figsize=(14, 6))

        # Plotar o histograma com KDE
        sns.histplot(data[coluna], kde=True, ax=axs[0])
        axs[0].set_title(f'{coluna} - Histograma\nAssimetria: {skewness:.2f}, Curtose: {kurt:.2f}')
    
        # Plotar o Q-Q Plot
        sm.qqplot(data[coluna], line='s', ax=axs[1])
        axs[1].set_title(f'{coluna} - Q-Q Plot')

        # Ajustar o layout da figura
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()