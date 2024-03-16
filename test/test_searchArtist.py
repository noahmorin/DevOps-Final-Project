import unittest
import requests
import json
from auth import get_token, get_auth_headers
from searchArtist import search_for_artist, artist_results
# https://docs.python.org/3/library/unittest.html

class test_searchArtist(unittest.TestCase):

    def test_successful_search(self):
        result = artist_results("The Minions")

        # Check JSON response structure
        self.assertIsInstance(result, dict)
        self.assertIn("name", result)
        self.assertEqual(result["name"], "The Minions")
        self.assertEqual(result["external_urls"]["spotify"], "https://open.spotify.com/artist/3NVrWkcHOtmPbMSvgHmijZ")
        self.assertTrue(len(result) > 0)