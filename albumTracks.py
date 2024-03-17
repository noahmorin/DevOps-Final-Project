from auth import get_token, get_auth_headers
from searchArtist import search_for_artist, artist_results
from requests import get, post, request
import json

def get_artist_songs(artistName):

    artistID = artist_results(artistName)["id"]

    token = get_token()
    headers = get_auth_headers(token)
    url = f"https://api.spotify.com/v1/artists/{artistID}/top-tracks?market=CA"

    result = get(url, headers=headers)
    top_tracks = json.loads(result.content)["tracks"]

    return [track["name"] for track in top_tracks]