from flask import Flask, render_template, request
from recommender import get_genre_seeds, get_recommendation
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

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