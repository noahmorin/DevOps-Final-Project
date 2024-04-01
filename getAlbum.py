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
                print(jsonResult["albums"]["items"][0])
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

def get_album_tracks(albumName):

    albumID = album_results(albumName)["id"]

    token = get_token()
    headers = get_auth_headers(token)
    url = f"https://api.spotify.com/v1/albums/{albumID}/tracks?"

    result = get(url, headers=headers)
    trackData = json.loads(result.content)
    return [track["name"] for track in trackData["items"]]

def get_album_by_id(token, albumID):
    url = f"https://api.spotify.com/v1/albums/{albumID}"
    headers = get_auth_headers(token)
    result = get(url, headers=headers)

    if result.status_code == 200:
        try:
            albumData = json.loads(result.content)
        except ValueError:
            raise ValueError("Unexpected JSON response from Spotify API")
    else:
        raise Exception(f"Status Code {result.status_code} and response: {result.content}, while trying to get album by ID {albumID}")
    
    return albumData     

def get_album_tracks_by_id(token, albumID):

    token = get_token()
    url = f"https://api.spotify.com/v1/albums/{albumID}/tracks"
    headers = get_auth_headers(token)

    result = get(url, headers=headers)
    trackData = json.loads(result.content)

    if result.status_code == 200:
        try:
            trackData = json.loads(result.content)

            if "items" in trackData:
                return [{'name': track["name"], 'id': track["id"]} for track in trackData["items"]]
            
        except ValueError:
            raise ValueError("Received unexpected JSON response from Spotify API")
        
    else:
        raise Exception(f"Status Code {result.status_code} and response: {result.content}, while trying to get tracks for album {albumID}")



