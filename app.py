from flask import Flask, render_template, request, redirect, session
from userInfo import user_result, user_name, user_profile_image, user_playlist, user_top_artist, user_top_track, user_add_playlist, add_to_playlist
from userAuth import check_login, spotify_login, set_token, log_out
from searchArtist import artist_results, get_artist_albums
from artistTopTracks import get_artist_top_tracks
from getAlbum import album_results, get_album_tracks, get_album_by_id, get_album_tracks_by_id
# from getAlbumTracks import get_album_tracks
from searchSong import song_results, search_for_song_by_id
from recommender import get_genre_seeds, get_recommendation
from auth import get_token
from werkzeug.datastructures import ImmutableMultiDict
import time
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    session['returnPage'] = '/'
    session['checkCred'] = False
    return render_template('minioninifier.html')

@app.route('/home', methods=['GET', 'POST']) 
def home():
    session['returnPage'] = '/home'
    session['checkCred'] = False
    return render_template('home.html')

# Link to user profile
@app.route('/userInfo', methods=['GET', 'POST'])
def user_info_route():
    if session['checkCred'] != True:
        session['returnPage'] = '/userInfo'
        return redirect('/checkingCred')

    session['checkCred'] = False
    userProfileInfo = user_result()
    userName = user_name(userProfileInfo)
    userProfileImg = user_profile_image(userProfileInfo)
    userPlaylistInfo = user_playlist()
    userTopArtistInfo = user_top_artist()
    userTopTrackInfo = user_top_track()
    return render_template('userProfile.html', result = userName, img = userProfileImg, names = userPlaylistInfo, artists = userTopArtistInfo, tracks = userTopTrackInfo)

# Link to allow user to log into spotify account
@app.route('/login', methods=['GET', 'POST'])
def user_login():
   # Gets the link from spotify_login page and redirects to login link
   authUrl = spotify_login()
   return redirect(authUrl)

@app.route('/logOut', methods=['GET', 'POST'])
def user_log_out():
    log_out()
    session['checkCred'] = False
    return redirect('/')

@app.route('/callback/')
def call_back():
   # Set the token in the .env file and redirects back to previous page
   set_token()
   session['checkCred'] = True
   session['second'] = time.time()
   return redirect(session['returnPage'])


@app.route('/searchArtist', methods=['GET', 'POST'])
def search_artist_route():
    if request.method == 'POST':
        artistName = request.form['artist']  # Get the artist name from the form in the searchArtist.html template
        try:
            results, imageKey = artist_results(artistName)
            songs = get_artist_top_tracks(artistName)
            albums = get_artist_albums(artistName)
            userPlaylistInfo = user_add_playlist()

            return render_template('artistResults.html', results=results, songs=songs, albums=albums, imageKey=imageKey, query=artistName, addPlaylist = userPlaylistInfo)  # Render results.html and pass variables to the template
        except:
            return render_template('noResults.html')
    else:
        if session['checkCred'] != True:
            session['returnPage'] = '/searchArtist'
            return redirect('/checkingCred')

        session['checkCred'] = False

        return render_template('searchArtist.html')
    
@app.route('/searchAlbum', methods=['GET', 'POST'])
def search_album_route():
    if request.method == 'POST':
        albumName = request.form['album']  # Get the album name from the form in the searchAlbum.html template
        try:
            albumResult = album_results(albumName)
            tracks = get_album_tracks(albumName)
            userPlaylistInfo = user_add_playlist()
            return render_template('returnAlbum.html', results=albumResult, tracks=tracks, addPlaylist = userPlaylistInfo)  # Render results and pass variables to the template
        except:
            return render_template('noResults.html')
    else:
        if session['checkCred'] != True:
            session['returnPage'] = '/searchAlbum'
            return redirect('/checkingCred')

        session['checkCred'] = False
        return render_template('searchAlbum.html')

@app.route('/searchSong', methods=['GET', 'POST'])
def test_search_track_route():
    if request.method == 'POST':
        songName = request.form['track']
        try:
            allResults = song_results(songName)
            userPlaylistInfo = user_add_playlist()
            return render_template('songResults.html', all_results=allResults, addPlaylist = userPlaylistInfo)
        except:
            return render_template('noResults.html')
    else:
        if session['checkCred'] != True:
            session['returnPage'] = '/searchSong'
            return redirect('/checkingCred')

        session['checkCred'] = False
        return render_template('searchSong.html')

@app.route('/recommender', methods=['GET', 'POST'])
def recommender_route():
    if request.method == 'POST':
        seedGenres = ""
        genreDict = request.form.to_dict(flat=False) # Get the results from the HTML form (selecting genres) turn the immutible dictionary object into a dictionary
        if len(genreDict) > 0:
            for genre in genreDict: # Format list of genres into seed genres (i.e country&rock&rap)
                seedGenres += genre + "&"
            songRecommendation = get_recommendation(seedGenres)
        else:
            songRecommendation = "Please select at least 1 genre"

        userPlaylistInfo = user_add_playlist()
        return render_template('recommendation.html', results = songRecommendation, addPlaylist = userPlaylistInfo)
    else:
        if session['checkCred'] != True:
            session['returnPage'] = '/recommender'
            return redirect('/checkingCred')

        session['checkCred'] = False
        genres = get_genre_seeds()
        return render_template('recommender.html', genres=genres)
    

# For searching directly from searchArtist page. 
@app.route('/album/<albumID>', methods=['GET'])
def album_details_route(albumID):
    result = get_album_by_id(get_token(), albumID)
    tracks = get_album_tracks_by_id(get_token(), albumID)
    userPlaylistInfo = user_add_playlist()
    return render_template('albumDetails.html', result=result, tracks=tracks, addPlaylist = userPlaylistInfo)

@app.route('/song/<songID>', methods=['GET'])
def song_details_route(songID):
    result = search_for_song_by_id(get_token(), songID)
    return render_template('songDetails.html', result=result)

@app.route('/checkingCred', methods=['GET', 'POST'])
def checking_cred():
    if not session.get('second'):
        session['second'] = time.time()

    checkLogin = check_login(session['second'], time.time())

    if checkLogin == 'login':
       return redirect('/login')
    elif checkLogin == 'refresh':
        session['second'] = time.time()
        session['checkCred'] = True
        return redirect(session['returnPage'])
    else:
        session['checkCred'] = True
        return redirect(session['returnPage'])

@app.route('/addPlaylist', methods=['GET', 'POST'])
def add_playlist():
    urlPlaylist = request.form['urlPlaylist']
    add_to_playlist(urlPlaylist)
    return redirect(session['returnPage'])