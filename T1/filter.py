import pandas as pd

def delete(all_results):
    for i in range(len(all_results) - 1, -1, -1):
        if 2020 <= all_results[i]['ano'] <= 2024:
            del all_results[i]

def createCSV(data, filename):
    dataframe = pd.DataFrame(data)
    dataframe.to_csv(filename, index= False)

def main():
    df = pd.read_csv("Final.csv")
    all_results = df.to_dict(orient='records')
    delete(all_results)
    createCSV(all_results, "Update.csv")

if __name__ == "__main__":
    main()