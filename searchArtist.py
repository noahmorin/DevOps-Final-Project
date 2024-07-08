from auth import get_token, get_auth_headers
from requests import get, post, request
import json
import flask

def search_for_artist(token, artist):
    url = f"https://api.spotify.com/v1/search?q={artist}&type=artist&limit=1"
    headers = get_auth_headers(token)
    result = get(url, headers=headers)

    if result.status_code == 200:
        try:
            jsonResult = json.loads(result.content)
            if "artists" in jsonResult and "items" in jsonResult["artists"]:
                return jsonResult["artists"]["items"][0]
            
        except ValueError:
            raise ValueError("Unexpected JSON response from Spotify API")
    
    else: 
        raise Exception(f"Status Code {result.status_code} and response: {result.content}, while trying to search for artist {artist}.")

def artist_results(artistName):    
    token = get_token()
    result = search_for_artist(token, artistName)

    if len(result) == 0:
        return flask.render_template('noResults.html')
    
    popularity = result["popularity"]
    imageKey = None

    # check popularity for 0-20, 21-40, 41-60, 61-80, 81-100
    if popularity < 20:
        imageKey = 'minion5'
    elif popularity < 40:
        imageKey = 'minion4'
    elif popularity < 60:
        imageKey = 'minion3'
    elif popularity < 80:
        imageKey = 'minion2'
    else:
        imageKey = 'minion1'

    return result, imageKey

# Is an additional function that was added after phase 1. Test for this function does not exist, but the function is used in the app.
def get_artist_albums(artistName):
    token = get_token()

    artistResult, _ = artist_results(artistName)
    artistID = artistResult["id"]

    url = f"https://api.spotify.com/v1/artists/{artistID}/albums"
    headers = get_auth_headers(token)
    result = get(url, headers=headers)

    if result.status_code == 200:
        try:
            artistAlbums = json.loads(result.content)
            
            if "items" in artistAlbums:
                return [{
                    "name": album["name"],
                    "release_date": album["release_date"],
                    "total_tracks": album["total_tracks"],
                    "id": album["id"],
                }
                for album in artistAlbums["items"]]
        
        except ValueError:
            raise ValueError("Received unexpected JSON response from Spotify API")

    else:
        raise Exception(f"Status Code {result.status_code} and response {result.content}, while trying to get albums for {artistName}.")