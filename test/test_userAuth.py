import unittest
from userAuth import spotify_login, set_token
import requests

class test_userAuth(unittest.TestCase):
    # A link is returned from spotify_login()
    def test_link_return(self):
        self.assertTrue([]!=spotify_login())
    # The link returned from spotify_login() can be successfully reached
    def test_link_status(self):
        testUrl = spotify_login()
        self.assertEqual(200, requests.get(testUrl).status_code)