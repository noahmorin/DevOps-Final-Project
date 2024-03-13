from flask import Flask, render_template, request
from searchSong import song_results

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/searchSong', methods=['GET', 'POST'])
def search_track_route():
    if request.method == 'POST':
        songName = request.form['track']
        results = song_results(songName)
        return render_template('results.html', results=results)
    else:
        return render_template('searchSong.html')

# @app.route('/searchTrack', methods=['GET', 'POST'])
# def search_track_route():
#     if request.method == 'POST':
#         songName = request.form['track']  # Get the artist name from the form in the searchArtist.html template
#         results = song_results(trackName)
#         # songs = get_artist_songs(artistName)
#         return render_template('results.html', results=results, songs=songs)  # Render results.html and pass variables to the template
#     else:
#         return render_template('searchArtist.html')