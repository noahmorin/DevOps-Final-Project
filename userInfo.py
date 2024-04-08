from dotenv import load_dotenv
import os
from requests import get

load_dotenv()

# Gets user information
def user_result():
    try:
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
            return "https://i.pinimg.com/originals/9c/ac/dc/9cacdc207e8997bf90a3daf9c8aaca80.jpg"
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
            if not playlist['images']:
                temp = 'https://pyxis.nymag.com/v1/imgs/5b9/efd/75a07fbd5b20c0478d4dbdb062ea8d315d-minions-soundtrack.2x.rsocial.w600.jpg'
            else:
                temp = playlist['images'][0]['url']

            userPlaylistInfo[playlist['name']] = temp
        
        # If there are no playlist then returns a message to add playlist with a minion image
        if not userPlaylistInfo:
            userPlaylistInfo["Empty! Please add playlists."] = "https://sc0.blr1.cdn.digitaloceanspaces.com/book/176463-lcxhejvdxy-1656534581.jpg"
        
        return userPlaylistInfo
    else:
        raise Exception(f"Status code {playlistResult.status_code} and response: {playlistResult.content} when pulling user profile.")
    
# Get user top artists
def user_top_artist():
    # Calls the spotify api to get user top artists
    userTopArtistUrl = 'https://api.spotify.com/v1/me/top/artists?time_range=medium_term&limit=10'
    headers = {'Authorization': f'Bearer {os.getenv("userToken")}'}
    topArtistResult = get(userTopArtistUrl, headers=headers)
    
    # Checks to make sure that call was successful and return user top artists as a dictionary
    if topArtistResult.status_code == 200:
        topArtistStore = topArtistResult.json()
        topArtistInfo = topArtistStore['items']
        topArtist = {}

        for artist in topArtistInfo:
            # Checks if each artist has an image and if not it adds a minion profile picture
            if not artist['images']:
                tempArtist = 'https://i.ytimg.com/vi/2pFuprTphvs/maxresdefault.jpg'
            else:
                tempArtist = artist['images'][0]['url']
            
            topArtist[artist['name']] = tempArtist
        
        if not topArtist:
            # If there no top artists can be found then returns a message informing user
            topArtist["Not enough information! You have to listen to more songs."] = "https://i.ytimg.com/vi/2pFuprTphvs/maxresdefault.jpg"

        return topArtist
    else:
        raise Exception(f"Status code {topArtistResult.status_code} and response: {topArtistResult.content} when pulling user profile.")

# Get user top track
def user_top_track():
    # Calls the spotify api to get user top tracks
    userTopTrackUrl = 'https://api.spotify.com/v1/me/top/tracks?time_range=medium_term&limit=10'
    headers = {'Authorization': f'Bearer {os.getenv("userToken")}'}
    topTrackResult = get(userTopTrackUrl, headers=headers)
    
    # Checks to make sure that call was successful and return user top track as a dictionary
    if topTrackResult.status_code == 200:
        topTrackStore = topTrackResult.json()
        topTrackInfo = topTrackStore['items']
        topTrack = {}

        for track in topTrackInfo:
            # Checks if each track has an album image and if not it adds a minion album picture
            trackAlbum = track['album']
             
            if not trackAlbum['images']:
                tempTrack = 'https://i.ytimg.com/vi/2pFuprTphvs/maxresdefault.jpg'
            else:
                tempTrack = trackAlbum['images'][0]['url']
            
            topTrack[track['name']] = tempTrack
        
        if not topTrack:
            # If there no top tracks can be found then returns a message informing user
            topTrack["Not enough information! You have to listen to more songs."] = "https://i.ytimg.com/vi/3CgWPddfJ7k/maxresdefault.jpg"

        return topTrack
    else:
        raise Exception(f"Status code {topTrackResult.status_code} and response: {topTrackResult.content} when pulling user profile.")
    