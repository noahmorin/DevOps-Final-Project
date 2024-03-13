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
        all_results = song_results(songName)
        return render_template('results.html', all_results=all_results)
    else:
        return render_template('searchSong.html')
