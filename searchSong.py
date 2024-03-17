from auth import get_token, get_auth_headers
from requests import get
import json
from flask import render_template

def search_for_song(token, track): # This song will format the url and header for the api call, using auth data and what user put for song name
    url = f"https://api.spotify.com/v1/search?q={track}&type=track&limit=5"
    headers = get_auth_headers(token)
    results = call_api(url, headers)
    if results.status_code == 200:
        try: # Parses json data from api call, if it fails, it will return the ValueError message
            jsonResult = json.loads(results.content)["tracks"]["items"]
        except ValueError:
            return ValueError("Unexpected JSON response")
    else:
        raise Exception(f"Status code {results.status_code} and response: {results.text}, while trying to search for {track}.")
    return jsonResult

def call_api(url, headers): # API call to get the song data
    return get(url, headers=headers)

def song_results(songName): # Get the results from the api call, split up the 5 songs into the allResults list
    token = get_token()
    results = search_for_song(token, songName)
    allResults = []
    for result in results:
        allResults.append(result)
    if len(allResults) == 0:
        return render_template('noResults.html')
    return allResults
