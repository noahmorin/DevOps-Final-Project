import unittest
import requests
import json
from auth import get_token, get_auth_headers
from getAlbum import album_results, album_results, get_album_tracks
class test_searchAlbum(unittest.TestCase):

    def test_successful_album_search(self):
        result = album_results("Minions: The Rise Of Gru")

        # Check JSON response structure
        self.assertIsInstance(result, dict)
        self.assertIn("name", result)
        self.assertEqual(result["name"], "Minions: The Rise Of Gru")
        self.assertEqual(result["external_urls"]["spotify"], "https://api.spotify.com/v1/albums/4aawyAB9vmqN3uQ7FjRGTy")
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
# https://docs.python.org/3/library/unittest.html

