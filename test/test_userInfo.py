import unittest
from unittest.mock import Mock, patch 
from userInfo import user_result, user_name, user_profile_image, user_playlist, user_top_artist, user_top_track
from auth import get_token
import os
import requests
from http import HTTPStatus

class test_userInfo(unittest.TestCase):
    @patch('userInfo.user_result', return_value={'display_name': 'Lathushan Pavalavelauthan', 'external_urls': {'spotify': 'https://open.spotify.com/user/31usnyvxlegvmuy4rayvt7wszxs4'}, 'href': 'https://api.spotify.com/v1/users/31usnyvxlegvmuy4rayvt7wszxs4', 'id': '31usnyvxlegvmuy4rayvt7wszxs4', 'images': [], 'type': 'user', 'uri': 'spotify:user:31usnyvxlegvmuy4rayvt7wszxs4', 'followers': {'href': None, 'total': 0}, 'country': 'CA', 'product': 'free', 'explicit_content': {'filter_enabled': False, 'filter_locked': False}, 'email': 'lathushan.pavalavelauthan@ontariotechu.net'})
    # Test to make sure dict is returned from user_result
    def test_user_result_return(self, user_result):
        #fakeUserInfo = {'display_name': 'lathush5', 'external_urls': {'spotify': 'https://open.spotify.com/user/lathush5'}, 'href': 'https://api.spotify.com/v1/users/lathush5', 'id': 'lathush5', 'images': [{'url': 'https://i.scdn.co/image/ab67757000003b82ec28f8e246317f0c5e07baf5', 'height': 64, 'width': 64}, {'url': 'https://i.scdn.co/image/ab6775700000ee85ec28f8e246317f0c5e07baf5', 'height': 300, 'width': 300}], 'type': 'user', 'uri': 'spotify:user:lathush5', 'followers': {'href': None, 'total': 3}, 'country': 'CA', 'product': 'premium', 'explicit_content': {'filter_enabled': False, 'filter_locked': False}, 'email': 'lathush5@gmail.com'}
        self.reqInfo = user_result()
        self.assertIsInstance(self.reqInfo, dict)

    @patch('userInfo.user_result', return_value={'display_name': 'Lathushan Pavalavelauthan', 'external_urls': {'spotify': 'https://open.spotify.com/user/31usnyvxlegvmuy4rayvt7wszxs4'}, 'href': 'https://api.spotify.com/v1/users/31usnyvxlegvmuy4rayvt7wszxs4', 'id': '31usnyvxlegvmuy4rayvt7wszxs4', 'images': [], 'type': 'user', 'uri': 'spotify:user:31usnyvxlegvmuy4rayvt7wszxs4', 'followers': {'href': None, 'total': 0}, 'country': 'CA', 'product': 'free', 'explicit_content': {'filter_enabled': False, 'filter_locked': False}, 'email': 'lathushan.pavalavelauthan@ontariotechu.net'})
    # Test to make sure username is returned
    def test_username_return(self, user_result):
        self.reqInfo = user_result()
        testUserName = user_name(self.reqInfo)

        self.assertTrue([]!= testUserName)
        self.assertIsInstance(testUserName, str)

    @patch('userInfo.user_result', return_value={'display_name': 'Lathushan Pavalavelauthan', 'external_urls': {'spotify': 'https://open.spotify.com/user/31usnyvxlegvmuy4rayvt7wszxs4'}, 'href': 'https://api.spotify.com/v1/users/31usnyvxlegvmuy4rayvt7wszxs4', 'id': '31usnyvxlegvmuy4rayvt7wszxs4', 'images': [], 'type': 'user', 'uri': 'spotify:user:31usnyvxlegvmuy4rayvt7wszxs4', 'followers': {'href': None, 'total': 0}, 'country': 'CA', 'product': 'free', 'explicit_content': {'filter_enabled': False, 'filter_locked': False}, 'email': 'lathushan.pavalavelauthan@ontariotechu.net'})
    # Test to make sure profile image link is returned
    def test_user_image_return(self, user_result):
        self.reqInfo = user_result()
        testUserImage = user_profile_image(self.reqInfo)

        self.assertTrue([]!= testUserImage)
        self.assertEqual(200, requests.get(testUserImage).status_code)
    
    @patch('userInfo.user_playlist', return_value={'My Vibe': 'https://mosaic.scdn.co/640/ab67616d00001e022fc69bfe8b9b60dfb17a2589ab67616d00001e02b61ce47d00308209e80c8e1dab67616d00001e02d357e53838d5290f2e127ae0ab67616d00001e02ea46af6d8136150aca318f90', 'S Padalkal': 'https://mosaic.scdn.co/640/ab67616d00001e021d95a687101bd4cd802c83a1ab67616d00001e0278bcf30ba04b540f427bc597ab67616d00001e02b6a4ebf1227384b8870f5b31ab67616d00001e02d496b47f528e298bdaacae30', 'Body (Remix) [feat. ArrDee, E1 (3x3), ZT (3x3), Bugzy Malone, Buni, Fivio Foreign & Darkoo]': 'https://mosaic.scdn.co/640/ab67616d00001e021fd5708808ff9959d72f5c57ab67616d00001e0226847a635b96c96fee81d838ab67616d00001e0226fb3e777b7a962396173e93ab67616d00001e02e3a09a9ae3f1fa102c110e60', 'Beat Mix': 'https://image-cdn-ak.spotifycdn.com/image/ab67706c0000da84745d9ae772084f1107654a15', 'Nilo': 'https://mosaic.scdn.co/640/ab67616d00001e0224f3ca794c241a2673b8c9a2ab67616d00001e0234b1bdfeeb594c3295a2c17fab67616d00001e028bda34105de5623bae6bf02eab67616d00001e029bc51a34623888d284150721', 'Bgm': 'https://mosaic.scdn.co/640/ab67616d00001e023e738ca40d1372dda203a41dab67616d00001e027bbef42d34fd25b14b2a54eaab67616d00001e02ab86c3cceb2d7226b9cd8bc5ab67616d00001e02c007c43b3278af55cfccad2d', "Vithy's": 'https://mosaic.scdn.co/640/ab67616d00001e0212b3ae6c663db6a888374985ab67616d00001e0232f43d2b7862589792370786ab67616d00001e025553b3d07de7325715dea32bab67616d00001e02d6e24628df97e9dc817e625d', 'My Playlist #11': 'https://pyxis.nymag.com/v1/imgs/5b9/efd/75a07fbd5b20c0478d4dbdb062ea8d315d-minions-soundtrack.2x.rsocial.w600.jpg', 'Songs ': 'https://mosaic.scdn.co/640/ab67616d00001e022eafab74725e28b1d69c12f7ab67616d00001e0234b1bdfeeb594c3295a2c17fab67616d00001e0235e00bf518c28471731ee55cab67616d00001e02eaedf9bbb9a4e12f534d52e2', 'Eminem – Music To Be Murdered By': 'https://i.scdn.co/image/ab67616d00001e022f44aec83b20e40f3baef73c'})

    # Test to make sure playlists are returned
    def test_user_playlist_return(self, user_playlist):
        testUserPlaylist = user_playlist()

        self.assertTrue([]!= testUserPlaylist)
        self.assertIsInstance(testUserPlaylist, dict)
    
    @patch('userInfo.user_top_artist', return_value={'User1': 'https://i.scdn.co/image/ab6761610000e5ebfc7c542c04b5f7dc8f1b1c16', 'User2': 'https://i.scdn.co/image/ab6761610000e5ebb19af0ea736c6228d6eb539c', 'User3': 'https://i.scdn.co/image/ab6761610000e5ebe60d7a790ebea50d205bda93', 'User4': 'https://i.scdn.co/image/ab6761610000e5eb0a5c692089af5c0f9cf839f3', 'User5': 'https://i.scdn.co/image/ab6761610000e5eba52538772891f66547e1ebc3', 'User6': 'https://i.scdn.co/image/ab6761610000e5eb859ef7414772b7d07526d40a', 'User7': 'https://i.scdn.co/image/ab6761610000e5eb42389d59e94635ebcbda35dd', 'Jack Harlow': 'https://i.scdn.co/image/ab6761610000e5eb2aab40ce03f3fa86163f78bb', 'Harris Jayaraj': 'https://i.scdn.co/image/ab6761610000e5eb5bd97947f146486aee1fb0b1', 'Drake': 'https://i.scdn.co/image/ab6761610000e5eb4293385d324db8558179afd9'})

    # Test to make sure top artists are returned
    def test_user_artist_return(self, user_top_artist):
        testUserArtist = user_top_artist()

        self.assertTrue([]!= testUserArtist)
        self.assertIsInstance(testUserArtist, dict)
    
    @patch('userInfo.user_top_track', return_value={'Song11': 'https://i.scdn.co/image/ab67616d0000b2733ae7f8e461c8a09b9128bbea', 'Song16': 'https://i.scdn.co/image/ab67616d0000b273673ab538ce01ec876ea0bc31', 'Song66': 'https://i.scdn.co/image/ab67616d0000b273673ab538ce01ec876ea0bc31', 'Song55': 'https://i.scdn.co/image/ab67616d0000b27344781fed7555fc6764c3ee26', 'Song15': 'https://i.scdn.co/image/ab67616d0000b273673ab538ce01ec876ea0bc31', 'Song33': 'https://i.scdn.co/image/ab67616d0000b27368b8c8c50d959902e9e0cb89', 'Song2': 'https://i.scdn.co/image/ab67616d0000b2738675676b9d8ccffb37cb28d9', 'Seventeen': 'https://i.scdn.co/image/ab67616d0000b2732fc69bfe8b9b60dfb17a2589', 'No Role Modelz': 'https://i.scdn.co/image/ab67616d0000b273c6e0948bbb0681ff29cdbae8', 'Song4': 'https://i.scdn.co/image/ab67616d0000b273ddb5d6a3fcace864168e8920'})

    # Test to make sure top tracks are returned
    def test_user_track_return(self, user_top_track):
        testUserTrack = user_top_track()

        self.assertTrue([]!= testUserTrack)
        self.assertIsInstance(testUserTrack, dict)
    
    @patch('userInfo.user_add_playlist', return_value={'My Vibe': '45lMDmAEBk7B9KFK71W6kJ', 'Playlist1': '73L18vX7rbOB4syBD5kUED', 'Body (Remix) [feat. ArrDee, E1 (3x3), ZT (3x3), Bugzy Malone, Buni, Fivio Foreign & Darkoo]': '3k3DlcgbqoCUqPPtm69teq', 'Beat Mix': '3Q1KmdrkBvlKUtl7pMyLRH', 'Drake': '5KxhrpAOVrqIkFmTD9UEg0', 'Bgm': '4REcgFn9hWYeYC8btCp03E', "Play5": '1JjWp7lOEDdRoYidTOcWAc', 'My Playlist #11': '0gHSJJhgCCAcWMfC6bfERu', 'Songs ': '2TpeYV4bCalLUWkPeMJ2U1', 'Eminem – Music To Be Murdered By': '5BCsdSdhgXl6kcTTawjOt8'})
    
    # Test to make sure a list of playlist and its id
    def test_add_playlist_return(self, user_add_playlist):
        testAddUserPlaylist = user_add_playlist()

        self.assertTrue([]!= testAddUserPlaylist)
        self.assertIsInstance(testAddUserPlaylist, dict)