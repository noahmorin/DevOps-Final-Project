from flask import Flask, render_template, request
from searchSong import song_results
from recommender import get_genre_seeds, get_recommendation
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/searchSong', methods=['GET', 'POST'])
def search_track_route():
    if request.method == 'POST':
        songName = request.form['track']
        all_results = song_results(songName)
        return render_template('results.html', all_results=all_results)
    else:
        return render_template('searchSongs.html')
    
@app.route('/recommender', methods=['GET', 'POST'])
def recommender_route():
    if request.method == 'POST':
        seedGenres = ""
        genreDict = request.form.to_dict(flat=False)
        for genre in genreDict:
            seedGenres += genre + "&"
        songRecommendation = get_recommendation(seedGenres)
        return render_template('recommendation.html', results = songRecommendation)
    else:
        genres = get_genre_seeds()
        return render_template('recommender.html', genres=genres)
    
# @app.route('/searchTrack', methods=['GET', 'POST'])
# def search_track_route():
#     if request.method == 'POST':
#         songName = request.form['track']  # Get the artist name from the form in the searchArtist.html template
#         results = song_results(trackName)
#         # songs = get_artist_songs(artistName)
#         return render_template('results.html', results=results, songs=songs)  # Render results.html and pass variables to the template
#     else:
#         return render_template('searchArtist.html')