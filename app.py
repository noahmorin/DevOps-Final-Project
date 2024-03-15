from flask import Flask, render_template, request
from searchArtist import artist_results
from artistTracks import get_artist_songs
from getAlbum import album_Results
from albumTracks import get_album_tracks

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/home', methods=['GET', 'POST']) 
def home():
    return render_template('home.html')

@app.route('/searchArtist', methods=['GET', 'POST'])
def search_artist_route():
    if request.method == 'POST':
        artistName = request.form['artist']  # Get the artist name from the form in the searchArtist.html template
        results = artist_results(artistName)
        songs = get_artist_songs(artistName)
        return render_template('results.html', results=results, songs=songs)  # Render results.html and pass variables to the template
    else:
        return render_template('searchArtist.html')

@app.route('/searchAlbum', methods=['GET', 'POST'])
def searchAlbum_route():
    if request.method == 'POST':
        albumName = request.form['album']  # Get the album name from the form in the searchAlbum.html template
        albumResult = album_Results(albumName)
        tracks = get_album_tracks(albumName)
        return render_template('returnAlbum.html', results=albumResult, tracks=tracks)  # Render results and pass variables to the template
    else:
        return render_template('searchAlbum.html')



if __name__ == "__main__":
    app.run(host="localhost",port=7575)