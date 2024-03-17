import unittest
from userInfo import user_result, user_name, user_profile_image, userPlaylist
from auth import get_token
from dotenv import load_dotenv
import os
import requests

class test_userInfo(unittest.TestCase):
    # Uses developer token to check if a username is not empty and is in string format
    def username_not_empty(self):
        load_dotenv()
        os.environ['userToken'] = get_token()
        testUserName = user_name(user_result())

        self.assertTrue([]!= testUserName)
        self.assertIsInstance(testUserName, str)

    # Uses developer token to check if a user profile image is not empty and the url to image can be reached 
    def user_image_not_empty(self):
        load_dotenv()
        os.environ['userToken'] = get_token()
        testUserImage = user_profile_image(user_result())

        self.assertTrue([]!= testUserImage)
        self.assertEqual(200, requests.get(testUserImage).status_code)

    # Uses developer token to check if a user playlist is not empty and is in dictionary format
    def user_image_not_empty(self):
        load_dotenv()
        os.environ['userToken'] = get_token()
        testUserPlaylist = user_profile_image(user_result())

        self.assertTrue([]!= testUserPlaylist)
        self.assertIsInstance(testUserPlaylist, dict)