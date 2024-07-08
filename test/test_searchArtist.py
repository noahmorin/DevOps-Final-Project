import unittest
import requests
import json
from auth import get_token, get_auth_headers
from searchArtist import search_for_artist, artist_results
# https://docs.python.org/3/library/unittest.html

class test_searchArtist(unittest.TestCase):

    def test_successful_search(self):
        result, imageKey = artist_results("The Minions")

        # Check JSON response structure and expected values
        self.assertIsInstance(result, dict)
        self.assertIn("name", result)
        self.assertEqual(result["name"], "The Minions")
        self.assertEqual(result["external_urls"]["spotify"], "https://open.spotify.com/artist/3NVrWkcHOtmPbMSvgHmijZ")
        self.assertTrue(len(result) > 0)

        # Check imageKey
        self.assertIsInstance(imageKey, str)
        self.assertIn(imageKey, ["minion1", "minion2", "minion3", "minion4", "minion5"])