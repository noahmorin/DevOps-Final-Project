import unittest
from userAuth import spotify_login, set_token, check_login, log_out
import requests
from app import app
import os

class test_userAuth(unittest.TestCase):
    # Test to see if user is redirected to login page if userToken not set
    def test_login_redirect(self):
        if os.getenv('userToken') != None:
            os.environ.pop('userToken')
        os.environ['expireTime'] = str(5000)
        testResult = check_login(1200, 3000)
        self.assertTrue('login' == testResult)
    
    # Tests to make sure that refresh token is used if time expired
    def test_refresh_token_call(self):
        if os.getenv('expireTime') != None:
            os.environ['expireTime'] = str(3600)
            os.environ['refreshToken'] = 'P7fUGrMk2ZzyEve6J90FbfoxHlT8b0MDzXyJZJmxahYHijqRJJiib45UvXeVJ0sT'
            os.environ['userToken'] = 'P7fUGrMk2ZzyEve6J90FbfoxHlT8b0MDzXyJZJmxahYHijqRJJiib45UvXeVJ0sT'

        with self.assertRaises(Exception) as context:
            check_login(1712589793.3340664, 1712593393.33)

        exceptionResult = '''Status code 400 and response: b'{"error":"invalid_grant","error_description":"Invalid refresh token"}' when pulling user profile.'''
        self.assertTrue(exceptionResult in str(context.exception))

    # Tests if link is returned from spotify_login()
    def test_link_return(self):
        self.assertTrue([]!=spotify_login())

    # Tests if link returned from spotify_login() can be successfully reached
    def test_link_status(self):
        testUrl = spotify_login()
        self.assertEqual(200, requests.get(testUrl).status_code)
    
    # Tests to make sure that link to set token is called
    def test_set_token(self):
        with app.test_request_context() as req:
            req.request.args = {'code': 'testCode'}
            with self.assertRaises(Exception) as context:
                set_token()

            exceptionResult = '''Status code 400 and response: b'{"error":"invalid_grant","error_description":"Invalid authorization code"}' when pulling user profile.'''
            self.assertTrue(exceptionResult in str(context.exception))
    
    # Test to check if logout removes tokens
    def test_log_out(self):
        if os.getenv('userToken') != None:
            os.environ['userToken'] = 'P7fUGrMk2ZzyEve6J90FbfoxHlT8b0MDzXyJZJmxahYHijqRJJiib45UvXeVJ0sT'
            os.environ['refreshToken'] = 'P7fUGrMk2ZzyEve6J90FbfoxHlT8b0MDzXyJZJmxahYHijqRJJiib45UvXeVJ0sT'
            os.environ['expireTime'] = str(3600)
        
        log_out()
        
        self.assertEqual(None,os.getenv('userToken'))
        self.assertEqual(None,os.getenv('refreshToken'))
        self.assertEqual(None,os.getenv('expireTime'))