from flask import request
from dotenv import load_dotenv
import requests
import os
import urllib
import random
import string

load_dotenv()

# https://shubham13596.medium.com/using-spotify-web-api-in-flask-c28bd4fd47b6


def check_login(startTime, currentTime):
  #Check if the user token is loaded and returns back login if it is token is not loaded
        if os.getenv('userToken') is None:
            return "login"
        elif (currentTime - startTime) >= (int(os.getenv('expireTime')) - 30):
           getTokenParams = {
            'grant_type': 'refresh_token',
            'refresh_token': os.getenv('refreshToken'),
            'client_id': os.getenv('CLIENT_ID'),
            'client_secret': os.getenv('CLIENT_SECRET'),
            'redirect_uri': os.getenv('REDIRECT_URI')
            }
           
           add_token(getTokenParams)
           return 'refresh'
           

# Creates the url query to allow user to log into spotify and sends the url
def spotify_login():
 state = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 16))
 
 authParams = {
 'response_type': 'code',
 'client_id': os.getenv('CLIENT_ID'),
 'redirect_uri': os.getenv('REDIRECT_URI'),
 'scope': 'user-read-email user-read-private user-top-read playlist-modify-public playlist-modify-private playlist-read-private',
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
  getTokenParams = {
    'grant_type': 'authorization_code',
    'code': authCode,
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('CLIENT_SECRET'),
    'redirect_uri': os.getenv('REDIRECT_URI')
    }
  
  add_token(getTokenParams)
  return


def add_token(getTokenParams):
  getTokenUrl = 'https://accounts.spotify.com/api/token/?'
  reqToken = requests.post(getTokenUrl, data = getTokenParams)

  #Checks to make sure that the request for user api token was successful
  if reqToken.status_code == 200:
     # Stores user token
     userTokenCreds = reqToken.json()
     os.environ['userToken'] = userTokenCreds['access_token']
     # !!! Added refresh token and expire time
     if os.getenv('refreshToken') is None:
        os.environ['refreshToken'] = userTokenCreds['refresh_token']
     os.environ['expireTime'] = str(userTokenCreds['expires_in'])
     return
  else:
    raise Exception(f"Status code {reqToken.status_code} and response: {reqToken.content} when pulling user profile.")


def log_out():
   if os.getenv('userToken') != None:
      os.environ.pop('userToken')
   if os.getenv('expireTime') != None:
      os.environ.pop('expireTime')
   if os.getenv('refreshToken') != None:
      os.environ.pop('refreshToken')
   return