from auth import get_token, get_auth_headers
from requests import get, post, request
import json
import flask

def search_album(token, albums):
    url = f"https://api.spotify.com/v1/search?q={albums}&type=album&limit=1"
    headers = get_auth_headers(token)

    albumResult = get(url, headers=headers)
    
    if albumResult.status_code == 200:
        try:
            jsonResult = json.loads(albumResult.content)
            if "albums" in jsonResult and "items" in jsonResult["albums"]:
                return jsonResult["albums"]["items"][0]
            else:
                raise ValueError("No albums found in Spotify API response")
        except ValueError:
            raise ValueError("Unexpected JSON response from Spotify API")
    else:
        raise Exception(f"Status Code {albumResult.status_code} and response: {albumResult.content}, while trying to search for album {albums}")

def album_results(albumName):
    token = get_token()
    result = search_album(token, albumName)
    if len(result) == 0:
        return flask.render_template('noResults.html')
    return result