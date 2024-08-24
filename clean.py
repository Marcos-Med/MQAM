import pandas as pd
import ast

def delete(all_results):
    for i in range(len(all_results) - 1, -1, -1):
        if all_results[i]['budget'] == 0 or all_results[i]['revenue'] == 0:
            del all_results[i]
  
def clean(all_results):
    for movie in all_results:
        dictionary = ast.literal_eval(movie['production_companies'])
        movie['production_companies'] = []
        for company in dictionary:
            movie['production_companies'].append(company['name'])
        dictionary = ast.literal_eval(movie['Ratings'])
        flag = False
        for value in dictionary:
            if(value['Source'] == 'Rotten Tomatoes'):
                movie['Ratings'] = value['Value']
                flag = True
                break
        if not flag:
            all_results.remove(movie)

def removeColumn(column, all_results):
    for movie in all_results:
        del movie[column]

def renameColumn(column, rename, all_results):
    for movie in all_results:
        movie[rename] = movie.pop(column, None)

def createCSV(data, filename):
    dataFrame = pd.DataFrame(data)
    dataFrame.to_csv(filename, index= False)

def main():
    df = pd.read_csv("Movies.csv")
    all_results = df.to_dict(orient='records')
    delete(all_results)
    clean(all_results)
    renames = [ 'popularidade','titulo', 'voto_popular', 'orcamento', 'produtoras', 'receita', 'duracao',
               'ano', 'genero', 'diretor', 'pais', 'avaliacao_da_critica']
    columns = ['popularity', 'title', 'vote_average', 'budget', 'production_companies', 'revenue', 'runtime',
               'Year', 'Genre', 'Director', 'Country', 'Ratings']
    removeColumn('imdb_id', all_results)
    removeColumn('Episode', all_results)
    for i in range(0, len(columns)):
        renameColumn(columns[i], renames[i], all_results)
    createCSV(all_results, "Teste2.csv")
    
    
if __name__ == "__main__":
    main()