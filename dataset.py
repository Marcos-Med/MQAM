import requests
import pandas
import json

keyTMDB = "3f6b73f8a76ccf049e994634a5a2b273"
keyOMDB = "d29535f4"
tokenTMDB = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZjZiNzNmOGE3NmNjZjA0OWU5OTQ2MzRhNWEyYjI3MyIsIm5iZiI6MTcyNDM4MzY5OC4wNzE4NjEsInN1YiI6IjY2YzYxN2YzNTk2MWNlZTg3ZTY5ZWQzYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ogQ7duMdbP16GPUyGSB5E200SjzropEXsuZUvgxxVzs"

def getDetailsMovie(token, ID):
    try:
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer {}".format(token)
        }
        url = "https://api.themoviedb.org/3/movie/{}?language=pt-BR".format(ID)
        response = requests.get(url, headers=headers)
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        print("Error fetching data 1")
    except json.decoder.JSONDecodeError:
        print("Error decoding JSON")
    except KeyError:
        print("keyError 1")

def getMovieOMDB(keyAPI, ID):
    try:
        url = "http://www.omdbapi.com/?i={}&plot=full&apikey={}".format(ID,keyAPI)
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        print("Error fetching data 2")
    except json.decoder.JSONDecodeError:
        print("Errod decoding JSON")
    except KeyError:
        print("keyError 2")

def getDirectorMovie(token, ID):
    try:
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer {}".format(token)
        }
        url = "https://api.themoviedb.org/3/movie/{}/credits?language=pt-BR".format(ID)
        response = requests.get(url, headers=headers)
        data = response.json()
        data = data['results']['crew']
        listDirector = []
        for person in data:
            if(person['job'] == 'Director'):
                listDirector.extend(person)
        return listDirector 
    except requests.exceptions.RequestException:
        print("Error fetching data 3")
    except json.decoder.JSONDecodeError:
        print("Error decoding JSON")
    except KeyError:
        print("KeyError")

def getPopularMovies(token, page):
    try:
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer {}".format(token)
        }
        url = "https://api.themoviedb.org/3/movie/popular?language=pt-BR&page={}".format(page)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['results']
    except requests.exceptions.RequestException:
        print("Error fetching data 4")
    except json.decoder.JSONDecodeError:
        print("Error decoding JSON")
    except KeyError:
        print("keyError")

def createCSV(data, filename):
    dataFrame = pandas.DataFrame(data)
    dataFrame.to_csv(filename, index= False)


def main():
    filename = "Movies2.csv"
    all_results = []
    columns = ['adult', 'backdrop_path', 'original_language', 'original_title',
               'overview', 'poster_path', 'video', 'vote_count', 'genre_ids',
               'release_date']
    total = 0
    page = 1
    print("Init - Extract Data TMDB\n")
    while total < 1000:
        results = getPopularMovies(tokenTMDB, page)
        if results:
            for movie in results:
                for column in columns:
                    movie.pop(column, None)
            all_results.extend(results)
            total += len(results)
        else:
            print("Error in page {}".format(page))
            break
        page += 1
    columns = ['adult', 'backdrop_path', 'belongs_to_collection', 'homepage',
               'id', 'original_language', 'original_title', 'overview', 'popularity',
               'poster_path', 'production_countries', 'release_date', 'spoken_languages',
               'status', 'tagline', 'title', 'video', 'vote_average', 'vote_count', 'genres', 'original-country',
               'seriesID']
    for movie in all_results:
        result = getDetailsMovie(tokenTMDB, movie['id'])
        if result:
          for column in columns:
                result.pop(column, None)
          movie.update(result)
    columns = ['Title','Rated','Released', 'Runtime', 'Writer', 'Actors',
               'Plot', 'Language', 'Awards', 'Poster', 'Metascore', 'imdbRating',
               'imdbVotes', 'imdbID', 'Type', 'DVD', 'BoxOffice', 'Production',
               'Website', 'Response', 'Episode', 'Season', 'Error']
    for movie in all_results:
        result = getMovieOMDB(keyOMDB, movie['imdb_id'])
        if result:
            for column in columns:
                result.pop(column, None)
            movie.update(result)
    createCSV(all_results, filename)
    print("Finished - Extract Data TMDB\n")
    
if __name__ == "__main__":
    main()