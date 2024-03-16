import unittest
import requests
import json
from auth import get_token, get_auth_headers
from searchArtist import search_for_artist, artist_results
# https://docs.python.org/3/library/unittest.html

class test_searchArtist(unittest.TestCase):

    def get_token(self):
        self.get_token = get_token()

    def test_successful_search(self):
        result = search_for_artist(self.get_token, "Minions")

        # Check JSON response structure
        self.assertIsInstance(result, dict)
        self.assertIn("artists", result)
        self.assertIn("items", result["artists"])
        self.assertTrue(len(result["artists"]["items"]) > 0)
        self.assertEqual(result["artists"]["items"][0]["name"], "Minions")