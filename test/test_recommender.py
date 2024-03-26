import unittest
import requests
import json
from auth import get_token, get_auth_headers
from final-project-group-3.recommender import get_genre_seeds, get_recommendation, recommendation_api_call

class test_recommender(unittest.TestCase):

    def test_get_available_seed_genres(self):
        result = get_genre_seeds()

        # Check JSON response structure of the get_genre_seeds function. Expected result is a dictionary with one key "genres", and a value of a list of genres
        self.assertIsInstance(result, dict)
        self.assertIn("genres", result)
        self.assertEqual(result["external_urls"]["spotify"], "https://api.spotify.com/v1/recommendations/available-genre-seeds")
        self.assertTrue(len(result) > 0)
    
    def test_get_recommendation(self):
        result = get_recommendation("classical&country")

        # Check JSON response structure of the get_recommendation function. Given a seed_genre (list of genres with & in between), return the name of a song. Expected output is the name of a song as a string
        self.assertIsInstance(result, dict)
        self.assertIn("tracks", result)
        self.assertEqual(result["external_urls"]["spotify"], "https://api.spotify.com/v1/recommendations?seed_genres=classical%2Ccountry")
        self.assertTrue(len(result) > 0)
