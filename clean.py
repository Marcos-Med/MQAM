import pandas as pd

def delete(all_results):
    all_results = [movie for movie in all_results if movie['budget'] != 0 and movie['revenue'] != 0]

##def delete(all_results):
    ##for movie in all_results:
        ##if movie['budget'] == 0 or movie['revenue'] == 0:
            ##all_results.remove(movie)
            ##continue
        ##flag = False
        ##for a in movie['Ratings']:
            ##if a[0] == 'Rotten Tomatoes':
                ##flag = True
                ##break
        ##if not flag:
            ##all_results.remove(movie)
  
def clean(all_results):
    for movie in all_results:
        movie['production_companies'] = [{'name': company[2]} for company in movie['production_companies']]
        for a in movie['Ratings']:
            if a[0] == 'Rotten Tomatoes':
                movie['Ratings'] = a

def createCSV(data, filename):
    dataFrame = pd.DataFrame(data)
    dataFrame.to_csv(filename, index= False)

def main():
    df = pd.read_csv("Movies.csv")
    all_results = df.to_dict(orient='records')
    delete(all_results)
    ##clean(all_results)
    createCSV(all_results, "Teste.csv")
    
    
if __name__ == "__main__":
    main()