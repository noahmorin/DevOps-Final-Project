import unittest
import json
from flask import render_template

class test_searchSong(unittest.TestCase):
    def test_search_for_song(self):
        results = self.call_api()
        try:
            jsonResult = json.loads(results.content)["tracks"]["items"]
        except:
            jsonResult = []
        self.assertIsInstance(jsonResult, dict)
        return jsonResult

    def call_api(self):
        with open('test.json', 'r') as f:
            return json.load(f)

    def test_song_results(self):
        results = self.test_search_for_song()
        if results == []:
            return render_template('noResults.html')
        all_results = []
        for result in results:
            all_results.append(result)
        self.assertIsInstance(all_results, list)
        return all_results

if __name__ == '__main__':
    unittest.main()