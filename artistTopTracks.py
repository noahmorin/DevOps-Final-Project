from auth import get_token, get_auth_headers
from searchArtist import search_for_artist, artist_results
from requests import get, post, request
import json

def get_artist_top_tracks(artistName):

    token = get_token()
    artistID = artist_results(artistName)["id"]

    url = f"https://api.spotify.com/v1/artists/{artistID}/top-tracks?market=CA"
    headers = get_auth_headers(token)
    result = get(url, headers=headers)


    if result.status_code == 200:
        try:
            topTracks = json.loads(result.content)

            if "tracks" in topTracks:
                return [{
                    "name": track["name"],
                    "album": track["album"]["name"],
                    "release_date": track["album"]["release_date"],
                    "popularity": track["popularity"],
                    "id": track["id"],
                }
                for track in topTracks["tracks"]]
            
        except ValueError:
            raise ValueError("Received unexpected JSON response from Spotify API")

    else:
        raise Exception(f"Status Code {result.status_code} and response {result.content}, while trying to get top tracks for {artistName}.")