from flask import request
from dotenv import load_dotenv
import requests
import os
import urllib
import random
import string

load_dotenv()

# https://shubham13596.medium.com/using-spotify-web-api-in-flask-c28bd4fd47b6
# Creates the url query to allow user to log into spotify and sends the url
def spotify_login():
 state = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 16))
 
 authParams = {
 'response_type': 'code',
 'client_id': os.getenv('CLIENT_ID'),
 'redirect_uri': os.getenv('REDIRECT_URI'),
 'scope': 'user-read-email user-read-private user-top-read',
 'state': state,
 'show_dialog': 'true'
 }
 authUrl = 'https://accounts.spotify.com/authorize/?' + urllib.parse.urlencode(authParams)
 return authUrl


# Parses the user token from the response and stores the token
def set_token():
  # Gets the code required to request user token
  authCode = request.args.get('code')
  # Requests user token from spotify
  getTokenUrl = 'https://accounts.spotify.com/api/token/?'
  getTokenParams = {
    'grant_type': 'authorization_code',
    'code': authCode,
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('CLIENT_SECRET'),
    'redirect_uri': os.getenv('REDIRECT_URI')
    }
 
  reqToken = requests.post(getTokenUrl, data = getTokenParams)

  #Checks to make sure that the request for user api token was successful
  if reqToken.status_code == 200:
     # Stores user token
     userTokenCreds = reqToken.json()
     os.environ['userToken'] = userTokenCreds['access_token']
     return
  else:
    raise Exception(f"Status code {reqToken.status_code} and response: {reqToken.content} when pulling user profile.")