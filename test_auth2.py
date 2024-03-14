# https://docs.python.org/3/library/unittest.mock.html
# https://docs.python.org/3/library/unittest.html

import unittest
from unittest.mock import patch, Mock, MagicMock
from auth import get_token, get_auth_headers
import json

class Test_Auth(unittest.TestCase):

    @patch('requests.post') 
    def test_get_token_success(self, mockGetToken):

        mockResponse = MagicMock()
        mockResponse.status_code = 200
        mockResponse.text = '{"access_token": "sample token"}'
        mockResponse.json.return_value = json.loads(mockResponse.text)

        mockGetToken.return_value = mockResponse

        token = get_token()

        self.assertEqual(token, 'sample token')

if __name__ == "__main__":
    unittest.main()
