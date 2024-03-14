# https://docs.python.org/3/library/unittest.mock.html
# https://docs.python.org/3/library/unittest.html

import unittest
from unittest.mock import patch, Mock
import requests
from dotenv import load_dotenv
import os
from auth import get_token, get_auth_headers
import base64

# load_dotenv()

# clientID = os.getenv("CLIENT_ID")
# clientSecret = os.getenv("CLIENT_SECRET")

class Test_Auth(unittest.TestCase):
    @patch('auth.post') 
    def test_get_token_success(self, mock_post):
        mock_post.return_value.status_code = 200
        # represents the JSON response that the code would expect. Does not actually print JSON response.
        mock_post.return_value.json.return_value = {"access_token": "sample_token"} 

        print("Mock Post:", mock_post)

        token = get_token()
        
        print(token)
        print("Mock Token:", token) 

        self.assertEqual(token, "sample_token") 

    @patch('auth.post')
    def test_get_token_failure(self, mock_post):

        expectedStatusCode = 400
        expectedResponse = "Bad Request"

        mock_post.return_value.status_code = expectedStatusCode
        mock_post.return_value.text = expectedResponse

        # Checks to make sure that the function raises an exception when the status code is not 200
        with self.assertRaises(Exception) as context:
            get_token()

        # Checks to make sure that the exception message matches the actual exception message from the get_token function
        self.assertEqual(str(context.exception), f"Status code {expectedStatusCode} and response: {expectedResponse}, while trying to get token.")

    def test_get_auth_headers(self):
        token = "sample_token"
        headers = get_auth_headers(token)
        self.assertEqual(headers, {"Authorization": "Bearer " + token})

if __name__ == "__main__":
    unittest.main()
