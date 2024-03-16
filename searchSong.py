from auth import get_token, get_auth_headers
from requests import get
import json
from flask import render_template

def search_for_song(token, track): # This song will format the url and header for the api call, using auth data and what user put for song name
    url = f"https://api.spotify.com/v1/search?q={track}&type=track&limit=5"
    headers = get_auth_headers(token)
    results = call_api(url, headers)
    try: # Parses json data from api call, if it fails, it will return an empty list
        jsonResult = json.loads(results.content)["tracks"]["items"]
    except:
        jsonResult = []
    return jsonResult

def call_api(url, headers):
    return get(url, headers=headers)

def song_results(songName): # Get the results from the api call, split up the 5 songs into the allResults list
    token = get_token()
    results = search_for_song(token, songName)
    if results == []: # if jsonResult is empty from error checking earlier, it will return a noResults.html page
        return render_template('noResults.html')
    allResults = []
    for result in results:
        allResults.append(result)
    return allResults
