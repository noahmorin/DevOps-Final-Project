from auth import get_token, get_auth_headers
from requests import get, post, request
import json

def search_Album(token, albums):
    url = f"https://api.spotify.com/v1/search?q={albums}&type=album&limit=1"
    headers = get_auth_headers(token)

    albumResult = get(url, headers=headers)
    
    if albumResult.status_code == 200:
        try:
            jsonResult = json.loads(albumResult.content)
            if "albums" in jsonResult and "items" in jsonResult["albums"]:
                return jsonResult["album"]["items"][0]
        except ValueError:
            raise ValueError("Unexpected JSON response from Spotify API")
        else:
            raise Exception(f"Status Code {albumResult.status_code} and response: {albumResult.content}, while trying to search for album {albums}:")    
    return jsonResult[0]

def album_Results(albumName):
    token = get_token()
    result = search_Album(token, albumName)

    return result