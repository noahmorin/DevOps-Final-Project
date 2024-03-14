from auth import get_token, get_auth_headers
from requests import get
import json
from searchSong import song_results

def get_genre_seeds():
    token = get_token()
    url = f"https://api.spotify.com/v1/recommendations/available-genre-seeds"
    headers = get_auth_headers(token)

    result = get(url, headers=headers)
    jsonResult = json.loads(result.content)
    return jsonResult

def recommendation_api_call(token, seedGenres):
    url = f"https://api.spotify.com/v1/recommendations?limit=1&seed_genres={seedGenres}"
    headers = get_auth_headers(token)

    result = get(url, headers=headers)
    recommendedSong = json.loads(result.content)["tracks"][0]["name"]
    print(recommendedSong)
    return recommendedSong

def get_recommendation(seedGenres):
    token = get_token()
    songName = recommendation_api_call(token, seedGenres)
    # result = song_results(songName)

    return songName