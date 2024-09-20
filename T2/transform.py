import pandas as pd
import numpy as ny

def transform(data):
    data['popularidade'] = ny.log(data['popularidade'])

def createCSV(data, filename):
    data.to_csv(filename, index=False)

df = pd.read_csv("T1/Final.csv")
transform(df)
filename = "Transform.csv"
createCSV(df, filename)
