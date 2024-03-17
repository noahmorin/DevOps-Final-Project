from auth import get_token, get_auth_headers
from getAlbum import search_album, album_results
from requests import get, post, request
import json

def get_album_tracks(albumName):

    albumID = album_results(albumName)["id"]

    token = get_token()
    headers = get_auth_headers(token)
    url = f"https://api.spotify.com/v1/albums/{albumID}/tracks?"

    result = get(url, headers=headers)
    trackData = json.loads(result.content)
    return [track["name"] for track in trackData["items"]]