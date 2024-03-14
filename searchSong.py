from auth import get_token, get_auth_headers
from requests import get, post, request
import json

def search_for_song(token, track):
    url = f"https://api.spotify.com/v1/search?q={track}&type=track&limit=5"
    headers = get_auth_headers(token)

    results = get(url, headers=headers)
    jsonResult = json.loads(results.content)["tracks"]["items"]
    return jsonResult

def song_results(songName):
    token = get_token()
    results = search_for_song(token, songName)
    all_results = []
    for result in results:
        all_results.append(result)
    return all_results
