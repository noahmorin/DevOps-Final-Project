from auth import get_token, get_auth_headers
from requests import get, post, request
import json

def search_for_song(token, track):
    url = f"https://api.spotify.com/v1/search?q={track}&type=track&limit=1"
    headers = get_auth_headers(token)

    result = get(url, headers=headers)
    jsonResult = json.loads(result.content)["track"]["items"]
    return jsonResult[0]

def song_results(songName):
    token = get_token()
    result = search_for_song(token, songName)
    return result
