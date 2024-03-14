from flask import Flask, render_template, request
from searchArtist import artist_results

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/searchArtist', methods=['GET', 'POST'])
def search_artist_route():
    if request.method == 'POST':
        artistName = request.form['artist']  # Get the artist name from the form in the searchArtist.html template
        results = artist_results(artistName)
        return render_template('results.html', results=results)  # Render results.html and pass variables to the template
    else:
        return render_template('searchArtist.html')