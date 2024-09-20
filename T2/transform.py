import pandas as pd
from scipy.stats import boxcox
from scipy.stats import yeojohnson
import numpy

def transform(data):
    data['popularidade'], lamb1 = boxcox(data['popularidade'])
    removeOutliers(data,'orcamento')
    data['avaliacao_da_critica'] = data['avaliacao_da_critica'].str.rstrip('%').astype('float') / 100
    print(lamb1)
    data = data.dropna()

def removeOutliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    mask = (data[column] >= lower_bound) & (data[column] <= upper_bound)
    data[column] = data[column].where(mask)

def createCSV(data, filename):
    data.to_csv(filename, index=False)

df = pd.read_csv("T1/Final.csv")
transform(df)
filename = "Transform.csv"
createCSV(df, filename)
