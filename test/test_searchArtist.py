import unittest
import requests
import json
from auth import get_token, get_auth_headers
from searchArtist import search_for_artist, artist_results
# https://docs.python.org/3/library/unittest.html

class test_searchArtist(unittest.TestCase):

    def test_successful_search(self):
        token = get_token()
        result = search_for_artist(token, "The Minions")

        # Check JSON response structure
        self.assertIsInstance(result, dict)
        self.assertIn("artists", result)
        self.assertIn("items", result["artists"])
        self.assertTrue(len(result["artists"]["items"]) > 0)
        self.assertEqual(result["artists"]["items"][0]["name"], "The Minions")