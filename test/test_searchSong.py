import unittest
from searchSong import song_results

class test_searchSong(unittest.TestCase):

    def test_song_results(self):
        results = song_results("Killer Queen")
        result = results[0]
        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], "Killer Queen - Remastered 2011")
        self.assertEqual(result["external_urls"]["spotify"], "https://open.spotify.com/track/7GqWnsKhMtEW0nzki5o0d8")
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()