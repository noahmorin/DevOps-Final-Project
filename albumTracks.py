from auth import get_token, get_auth_headers
from getAlbum import searchAlbum, album_Results
from requests import get, post, request
import json

def get_album_tracks(albumName):

    albumID = album_Results(albumName)["id"]

    token = get_token()
    headers = get_auth_headers(token)
    url = f"https://api.spotify.com/v1/albums/{albumID}/tracks?"

    result = get(url, headers=headers)
    trackData = json.loads(result.content)
    # albumTracks = json.loads(result.content)["total_tracks"]["name"]["images"]["release_date"]

    return [track["name"] for track in trackData["items"]]