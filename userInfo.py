from dotenv import load_dotenv
import os
from requests import get

load_dotenv()

# Gets user information
def user_result():
    try:
        #Check if the user token is loaded and returns back login if it is token is not loaded
        if os.getenv('userToken') is None:
            return "login"

        # Calls the spotify api to get user data
        userProfileUrl = 'https://api.spotify.com/v1/me?'
        headers = {'Authorization': f'Bearer {os.getenv("userToken")}'}
        userProfileResult = get(userProfileUrl, headers=headers)
        
        # Checks to make sure that call was successful and return user data
        if userProfileResult.status_code == 200:
            return userProfileResult.json()
        else:
           raise Exception(f"Status code {userProfileResult.status_code} and response: {userProfileResult.content} when pulling user profile.")
    except Exception as error:
        raise Exception("Unexpected Error: {}".format(error))

# Checks if username exists
def user_name(userInfo):
    try:
        userName = userInfo['display_name']

        # If username does not exist return username as Anonymous 
        if userName is None:
            return "Anonymous"
        else:
            return userName
    except Exception as error:
        raise Exception("Unexpected Error: {}".format(error))

# Checks if user profile picture exists
def user_profile_image(userInfo):
    try:
        userProfileImg = userInfo['images']

        # If user profile picture does not exist return a minion picture
        if not userProfileImg:
            return "https://lh3.googleusercontent.com/proxy/M8xO2b1I7K0EwAa9EGdgnGuMSN-Uh56bZRJlPvdPk5whCL67YRrMKW4PEIdIlm6PVZvKJondQ0E3YO9TPcMH6jqqW3NBW7OSAjy3zTBvZVlYtJ5fh5MB__OemkT8D4o"
        else:
            return userProfileImg[1]['url']
    except Exception as error:
        raise Exception("Unexpected Error: {}".format(error))

# Get user playlist
def user_playlist():
    # Calls the spotify api to get user playlist
    userPlaylistUrl = 'https://api.spotify.com/v1/me/playlists?limit=20'
    headers = {'Authorization': f'Bearer {os.getenv("userToken")}'}
    playlistResult = get(userPlaylistUrl, headers=headers)

    # Checks to make sure that call was successful and return user playlist as a dictionary
    if playlistResult.status_code == 200:
        userAllPlaylist = playlistResult.json()
        allPlaylist = userAllPlaylist['items']
        userPlaylistInfo = {}

        for playlist in allPlaylist:
            # Checks if each playlist has an image and if not it adds a minion album picture
            try:
                temp = playlist['images'][0]['url']
            except IndexError:
                temp = 'https://pyxis.nymag.com/v1/imgs/5b9/efd/75a07fbd5b20c0478d4dbdb062ea8d315d-minions-soundtrack.2x.rsocial.w600.jpg'
            except Exception as error:
                raise Exception("Unexpected Error: {}".format(error))
            
            userPlaylistInfo[playlist['name']] = temp
        
        # If there are no playlist then returns a message to add playlist with a minion image
        if not userPlaylistInfo:
            userPlaylistInfo["Empty! Please add playlists."] = "https://sc0.blr1.cdn.digitaloceanspaces.com/book/176463-lcxhejvdxy-1656534581.jpg"
        
        return userPlaylistInfo
    else:
        raise Exception(f"Status code {playlistResult.status_code} and response: {playlistResult.content} when pulling user profile.")
    