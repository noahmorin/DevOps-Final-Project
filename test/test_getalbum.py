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
        self.assertEqual(result["name"], "Minions: The Rise Of Gru (Original Motion Picture Soundtrack)")
        self.assertEqual(result["total_tracks"], 19)
        self.assertEqual(result["external_urls"]["spotify"], "https://open.spotify.com/album/6Kc0f1PCbWZLOmZNOyXYGN")
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()


