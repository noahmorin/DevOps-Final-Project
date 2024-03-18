from flask import Flask, render_template, request, redirect
from userInfo import user_result, user_name, user_profile_image, user_playlist
from userAuth import spotify_login, set_token
from searchArtist import artist_results, get_artist_albums
from artistTopTracks import get_artist_top_tracks
from getAlbum import album_results, get_album_tracks
# from getAlbumTracks import get_album_tracks
from searchSong import song_results
from recommender import get_genre_seeds, get_recommendation
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('minioninifier.html')

@app.route('/home', methods=['GET', 'POST']) 
def home():
    return render_template('home.html')

# Link to user profile
@app.route('/userInfo', methods=['GET', 'POST'])
def user_info_route():
    userProfileInfo = user_result()

    #If users token has not been loaded sends to login page then gets the data from userInfo and loads into page
    if userProfileInfo == "login":
       return redirect('/login')
    else:
       userName = user_name(userProfileInfo)
       userProfileImg = user_profile_image(userProfileInfo)
       userPlaylistInfo = user_playlist()
       return render_template('userProfile.html', result = userName, img = userProfileImg, names = userPlaylistInfo)

# Link to allow user to log into spotify account
@app.route('/login', methods=['GET', 'POST'])
def user_login():
   # Gets the link from spotify_login page and redirects to login link
   authUrl = spotify_login()
   return redirect(authUrl)

@app.route('/callback/')
def call_back():
   # Set the token in the .env file and redirects back to user profile page
   set_token()
   return redirect('/userInfo')

@app.route('/searchArtist', methods=['GET', 'POST'])
def search_artist_route():
    if request.method == 'POST':
        artistName = request.form['artist']  # Get the artist name from the form in the searchArtist.html template
        results = artist_results(artistName)
        songs = get_artist_top_tracks(artistName)
        albums = get_artist_albums(artistName)
        return render_template('artistResults.html', results=results, songs=songs, albums=albums)  # Render results.html and pass variables to the template
    else:
        return render_template('searchArtist.html')
    
@app.route('/searchAlbum', methods=['GET', 'POST'])
def search_album_route():
    if request.method == 'POST':
        albumName = request.form['album']  # Get the album name from the form in the searchAlbum.html template
        albumResult = album_results(albumName)
        tracks = get_album_tracks(albumName)
        return render_template('returnAlbum.html', results=albumResult, tracks=tracks)  # Render results and pass variables to the template
    else:
        return render_template('searchAlbum.html')

@app.route('/searchSong', methods=['GET', 'POST'])
def test_search_track_route():
    if request.method == 'POST':
        songName = request.form['track']
        allResults = song_results(songName)
        return render_template('songResults.html', all_results=allResults)
    else:
        return render_template('searchSong.html')

@app.route('/recommender', methods=['GET', 'POST'])
def recommender_route():
    if request.method == 'POST':
        seedGenres = ""
        genreDict = request.form.to_dict(flat=False) # Get the results from the HTML form (selecting genres) turn the immutible dictionary object into a dictionary
        for genre in genreDict: # Format list of genres into seed genres (i.e country&rock&rap)
            seedGenres += genre + "&"
        songRecommendation = get_recommendation(seedGenres)

        return render_template('recommendation.html', results = songRecommendation)
    else:
        genres = get_genre_seeds()
        return render_template('recommender.html', genres=genres)
    

# For searching directly from searchArtist page. 
@app.route('/album/<albumName>', methods=['GET'])
def album_details_route(albumName):
    albumResult = album_results(albumName)
    tracks = get_album_tracks(albumName)
    return render_template('albumDetails.html', result=albumResult, tracks=tracks)

@app.route('/song/<songName>', methods=['GET'])
def song_details_route(songName):
    allResults = song_results(songName)
    firstResult = allResults[0]
    return render_template('songDetails.html', result=firstResult)