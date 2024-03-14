from dotenv import load_dotenv
from requests import post, get, request
import json
import base64
import os

load_dotenv()

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")


def get_token():
    
    # Combine clientID and clientSecret into a string, then encode to base64, then decode it to utf-8
    auth_string = clientID + ":" + clientSecret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8)")
    #encodedCredentials = base64.b64encode(f"{clientID}:{clientSecret}".encode()).decode('utf-8')

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    result = post(url, headers=headers, data=data) #returns a response object. Useful for debugging/unit testing(?)

    # Use json.loads to convert the result.content to a dictionary. Use .json() when converting python objects to json
    jsonResult = json.loads(result.content)

    # Could also do result.json() instead of json.loads(result.content). Unsure which is better and/or correct(?)
    token = jsonResult["access_token"]
    
    return token

def get_auth_headers(token):
    return {"Authorization": "Bearer " + token}

