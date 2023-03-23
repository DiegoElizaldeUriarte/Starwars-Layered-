import requests

movie_url = "https://swapi.dev/api/films/"


def get_movies():
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]}
              for movie in data["results"]]
    movies = sorted(movies, key=lambda movie: movie["id"])
    return movies


def get_characters(movie_id):
    movie_characters_url = f"{movie_url}{movie_id}/"
    data = requests.get(movie_characters_url).json()
    characters = []
    for character_url in data["characters"]:
        character_data = requests.get(character_url).json()
        characters.append({
            "name": character_data["name"],


        })
    return characters
