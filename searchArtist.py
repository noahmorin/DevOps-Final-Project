from auth import get_token, get_auth_headers
from requests import get, post, request
import json

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

    return result