from flask import Flask, render_template, request
# from searchSong import song_results

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# @app.route('/searchSong', methods=['GET', 'POST'])
# def search_song_route():
#     if request.method == 'POST':
#         songName = request.form['song']  # Get the artist name from the form in the searchArtist.html template
#         results = song_results(songName)
#         # songs = get_artist_songs(artistName)
#         return render_template('results.html', results=results, songs=songs)  # Render results.html and pass variables to the template
#     else:
#         return render_template('searchArtist.html')
