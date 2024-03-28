from auth import get_token, get_auth_headers
from requests import get
import json

def get_genre_seeds():
    token = get_token()
    url = f"https://api.spotify.com/v1/recommendations/available-genre-seeds"
    headers = get_auth_headers(token)
    result = get(url, headers=headers)

    if result.status_code == 200:
        try:
            jsonResult = json.loads(result.content)

        except ValueError:
            raise ValueError("Unexpected JSON response from Spotify API")
    else:
        raise Exception(f"Status Code {result.status_code} and response: {result.content}, while trying to get the genre seeds.")
    
    return jsonResult

def recommendation_api_call(token, seedGenres):
    url = f"https://api.spotify.com/v1/recommendations?limit=5&seed_genres={seedGenres}"
    headers = get_auth_headers(token)
    result = get(url, headers=headers)

    if result.status_code == 200:
        try:
            # recommendedSong = json.loads(result.content)["tracks"][0]["name"]
            recommendedSong = json.loads(result.content)["tracks"]
            print(recommendedSong)

        except ValueError:
            raise ValueError("Unexpected JSON response from Spotify API")
    else:
        raise Exception(f"Status Code {result.status_code} and response: {result.content}, while trying to get the genre seeds.")

    return recommendedSong

def get_recommendation(seedGenres):
    token = get_token()
    songName = recommendation_api_call(token, seedGenres)
    return songName