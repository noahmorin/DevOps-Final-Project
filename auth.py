from dotenv import load_dotenv
from requests import post, get, request
import json
import base64
import os

load_dotenv()

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

def get_token():
    
    # Combine clientID and clientSecret into a string, encode them to utf-8, then decode it to utf-8

    url = "https://accounts.spotify.com/api/token"
    authHeader = base64.b64encode(f"{clientID}:{clientSecret}".encode('utf-8')).decode('utf-8')

    headers = {
        "Authorization": "Basic " + authHeader,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = post(url, headers=headers, data=data)

    if response.status_code == 200:
        token = response.json()["access_token"]
        return token
    else:
        raise Exception(f"Status code {response.status_code} and response: {response.text}, while trying to get token.")

def get_auth_headers(token):
    return {"Authorization": "Bearer " + token}

# get_token() # test if the function works