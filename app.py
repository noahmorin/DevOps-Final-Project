from flask import Flask, render_template, request
from searchSong import song_results

app = Flask(__name__)

@app.route('/')
def test_index():
    return render_template('home.html')

@app.route('/searchSong', methods=['GET', 'POST'])
def test_search_track_route():
    if request.method == 'POST':
        songName = request.form['track']
        allResults = song_results(songName)
        return render_template('songResults.html', all_results=allResults)
    else:
        return render_template('searchSong.html')
