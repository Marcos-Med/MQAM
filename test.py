import requests

def getMovieOMDB(keyAPI, ID):
    try:
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer {}".format(keyAPI)
        }
        url = "http://www.omdbapi.com/?i={}&plot=full&apikey={}".format(ID, keyAPI)
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        print("Error fetching data")
    except json.decoder.JSONDecodeError:
        print("Errod decoding JSON")
    except KeyError:
        print("keyError 2")

keyOMDB = "a031058c"

result = getMovieOMDB(keyOMDB, "tt0137523")
print(result)
print(result['Ratings'][1]['Value'])