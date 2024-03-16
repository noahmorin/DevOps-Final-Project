# from auth import get_token, get_auth_headers
# from requests import get, post, request
# import json
# import unittest
# import test
# from unittest.mock import patch, MagicMock


from auth import get_token, get_auth_headers
from requests import get, post, request
import json
from flask import render_template

class test_searchSong(unittest.TestCase):
    track = 'Killer Queen'
    token = get_token()
    def test_search_for_song(token, track):
        url = f"https://api.spotify.com/v1/search?q={track}&type=track&limit=5"
        headers = get_auth_headers(token)
        results = call_api(url, headers)
        try:
            jsonResult = json.loads(results.content)["tracks"]["items"]
        except:
            jsonResult = []
        return jsonResult

    def call_api(url, headers):
        return get(url, headers=headers)

    def test_song_results(songName):
        token = get_token()
        results = search_for_song(token, songName)
        if results == []:
            return render_template('noResults.html')
        all_results = []
        for result in results:
            all_results.append(result)
        return all_results


# class test_searchSong(unittest.TestCase):
#     def test_search_for_song(self):
#         track = 'Killer Queen'
#         url = f"https://api.spotify.com/v1/search?q={track}&type=track&limit=5"
#         headers = get_auth_headers(token)
#         with open('test.json', 'r') as f:
#             test_data = json.load(f)
#         mock_call_api.return_value = MagicMock(content=json.dumps(test_data))
#         results = test
#         try:
#             jsonResult = json.loads(results.content)["tracks"]["items"]
#         except:
#             jsonResult = []
#         return jsonResult