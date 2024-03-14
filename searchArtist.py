from auth import get_token, get_auth_headers
from requests import get, post, request
import json

def search_for_artist(token, artist):
    url = f"https://api.spotify.com/v1/search?q={artist}&type=artist&limit=1"
    headers = get_auth_headers(token)

    result = get(url, headers=headers)
    jsonResult = json.loads(result.content)["artists"]["items"]

    # TODO - error handling for when the artist is not found
    # try-except-else-finally
    return jsonResult[0]

def artist_results(artistName):
    token = get_token()
    result = search_for_artist(token, artistName)

    # artistID = result["id"]

    return result