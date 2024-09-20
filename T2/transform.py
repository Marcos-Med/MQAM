import pandas as pd
from scipy.stats import boxcox

def transform(data):
    data['popularidade'], lamb1 = boxcox(data['popularidade'])
    data['orcamento'], lamb2 = boxcox(data['orcamento'])
    data['receita'], lamb3 = boxcox(data['receita'])
    data['duracao'], lamb4 = boxcox(data['duracao'])
    data['avaliacao_da_critica'] = data['avaliacao_da_critica'].str.rstrip('%').astype('float') / 100
    print(lamb1)
    print(lamb2)
    print(lamb3)
    print(lamb4)

def createCSV(data, filename):
    data.to_csv(filename, index=False)

df = pd.read_csv("T1/Final.csv")
transform(df)
filename = "Transform.csv"
createCSV(df, filename)
