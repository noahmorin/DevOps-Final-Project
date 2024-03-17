import unittest
from artistTopTracks import get_artist_top_tracks

class test_artistTopTracks(unittest.TestCase):
    def test_successful_top_tracks(self):
        result = get_artist_top_tracks("The Minions")

        # Check if response is a list of songs, and that it is not empty
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

        # Check structure of first result in the list
        firstSong = result[0]
        self.assertIn("name", firstSong)
        self.assertIn("album", firstSong)
        self.assertIn("release_date", firstSong)
        self.assertIn("popularity", firstSong)