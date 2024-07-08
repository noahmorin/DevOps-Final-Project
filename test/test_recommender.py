import unittest
from recommender import get_genre_seeds, get_recommendation

class test_recommender(unittest.TestCase):

    def test_get_available_seed_genres(self):
        result = get_genre_seeds()

        # Check JSON response structure of the get_genre_seeds function. Expected result is a dictionary with one key "genres", and a value of a list of genres
        self.assertIsInstance(result, dict)
        self.assertIn("genres", result)
        self.assertTrue(len(result) > 0)
    
    def test_get_recommendation(self):
        result = get_recommendation("classical&country")

        # Check JSON response structure of the get_recommendation function. Given a seed_genre (list of genres with & in between), return the name and information of a song. Expected output is an object containing different information
        self.assertTrue(len(result) > 0)
