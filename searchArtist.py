from flask import Flask
from dotenv import load_dotenv
from requests import post, get, request
import json
import base64
import os

load_dotenv()

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

def get_token():
    # Combine clientID and clientSecret into a string, then encode it to base64, then decode it to utf-8
    encodedCredentials = base64.b64encode(f"{clientID}:{clientSecret}".encode()).decode('utf-8')

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + encodedCredentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    result = post(url, headers=headers, data=data) #returns a response object. Useful for debugging/unit testing(?)

    # use json.loads to convert the result.content to a dictionary. Use .json() when converting python objects to json
    jsonResult = json.loads(result.content)
    # could also do result.json() instead of json.loads(result.content). Unsure which is better and/or correct(?)
    token = jsonResult["access_token"]
    return token

def get_auth_headers(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist):
    url = f"https://api.spotify.com/v1/search?q={artist}&type=artist&limit=1"
    headers = get_auth_headers(token)

    result = get(url, headers=headers)
    jsonResult = json.loads(result.content)["artists"]["items"]
    if len(jsonResult) == 0:
        print("No artist found")
        return None
    
    return jsonResult[0]

token = get_token()

artistName = input("Enter artist name: ")
result = search_for_artist(token, artistName)

# Get artist ID
artistID = result["id"]
print(artistID)

# Can now use artistID to get more information about the artist, such as their top tracks, albums, etc.

# Flask example for web app testing. Still need to figure out how to search for things from the web app/GUI.

# app = Flask(__name__)

# @app.route('/')
# def test():
#     return 'Test!'