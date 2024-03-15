from auth import get_token, get_auth_headers
from requests import get, post, request
import json

def searchAlbum(token, albums):
    url = f"https://api.spotify.com/v1/search?q={albums}&type=album&limit=1"
    headers = get_auth_headers(token)
    #query = f"?q={albums}&type=album&limit=1"
    
    #queryURL = url + query
    albumResult = get(url, headers=headers)
    jsonResult = json.loads(albumResult.content) ["albums"]["items"]
    print(jsonResult)
    return jsonResult[0]

def album_Results(albumName):
    token = get_token()
    result = searchAlbum(token, albumName)

    # albumID = result["id"]

    print(result)
    return result