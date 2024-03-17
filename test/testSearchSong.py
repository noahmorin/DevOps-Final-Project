import unittest
import json
from flask import render_template

class test_searchSong(unittest.TestCase):
    def test_search_for_song(self): # Tests the api call and returns json data appropriately
        results = self.call_api()
        try:
            jsonResult = json.loads(results.content)["tracks"]["items"]
        except:
            jsonResult = []
        self.assertIsInstance(jsonResult, dict) # ensure that jsonResult is a dictionary
        return jsonResult

    def call_api(self): # Mock api call, just gets the test.json file
        with open('test.json', 'r') as f:
            return json.load(f)

    def test_song_results(self):
        results = self.test_search_for_song()
        if results == []:
            return render_template('noResults.html')
        allResults = []
        for result in results:
            allResults.append(result)
        self.assertIsInstance(allResults, list)
        return allResults

if __name__ == '__main__':
    unittest.main()