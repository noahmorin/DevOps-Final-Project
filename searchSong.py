from auth import get_token, get_auth_headers
from requests import get, post, request
import json
from flask import render_template

def search_for_song(token, track):
    url = f"https://api.spotify.com/v1/search?q={track}&type=track&limit=5"
    headers = get_auth_headers(token)
    results = call_api(url, headers)
    try:
        jsonResult = json.loads(results.content)["tracks"]["items"]
    except:
        jsonResult = []
    return jsonResult

def call_api(url, headers):
    return get(url, headers=headers)

def song_results(songName):
    token = get_token()
    results = search_for_song(token, songName)
    if results == []:
        return render_template('noResults.html')
    all_results = []
    for result in results:
        all_results.append(result)
    return all_results
