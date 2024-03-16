import unittest
import requests
import json
from auth import get_token, get_auth_headers
from recommender import get_genre_seeds, get_recommendation, recommendation_api_call

class test_recommender(unittest.TestCase):

    def test_get_available_seed_genres(self):
        result = get_genre_seeds()

        # Check JSON response structure
        self.assertIsInstance(result, dict)
        self.assertIn("genres", result)
        self.assertEqual(result["external_urls"]["spotify"], "https://api.spotify.com/v1/recommendations/available-genre-seeds")
        self.assertTrue(len(result) > 0)
    
    def test_get_recommendation(self):
        result = get_recommendation("classical%2Ccountry")

        # Check JSON response structure
        self.assertIsInstance(result, dict)
        self.assertIn("tracks", result)
        self.assertEqual(result["external_urls"]["spotify"], "https://api.spotify.com/v1/recommendations?seed_genres=classical%2Ccountry")
        self.assertTrue(len(result) > 0)