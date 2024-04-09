# Project Description
Our project uses the Spotify Web API and allows the user to search for various information about artists, songs, albums, and more.

# Features
- Search for a Spotify artist, which displays different information about them, like their photo and style of music. Below that you can also see the artists top songs, with a link to a webpage dedicated with info related to that song. Also, below the artist top songs are all the artist's albums with a link to a page dedicated to that as well.
- Displays an artists most popular songs, and displays which album they are part of and when that album was released.
- With the Search Song feature, users have the ability to search the Spotify API for the 5 most relevant songs to your search. The results display the ID, Artist, Album and Album art for the songs.
- With the Get album feature users can search for an album with the spotify API. This will provide the album that matches userinput the most. It will include the album tracks, total tracks and artist name.
- Song Recommender feature that accepts up to 5 genres to be selected and recommends a song to the user. Displays 5 recommendations, showing their title, artist, album, and album art.
- User Profile feature allows users to log in with their Spotify account to view their profile information. This includes their username, profile image, playlists, top artists and top songs.
- With the manage playlist feature, which can only be used if logged in, can allow the user to add features to a private or public playlist associated with your account using the results from our other features.


# How to install
* Clone the repository
  - ```git clone https://github.com/Ontario-Tech-NITS/final-project-group-3.git```
* Go to https://developer.spotify.com/ and create an account or sign in
  - Go to https://developer.spotify.com/dashboard and create an app
    - 'App name' can be anything
    - 'App description' can be anything
    - 'Website' can be left blank
    - Set 'Redirect URI' to ```http://127.0.0.1:5000/callback/```
  - Click on your new app, and click settings, and remember your CLIENT_ID and CLIENT_SECRET for the next step
  - To test with Spotify accounts other than the developer account, select the User Management option in settings and add the user's name and email connected to the Spotify account.
* Create a file named **.env** in the root folder of the cloned repository
  - Add the lines
    ```
    CLIENT_ID="<client ID>"
    CLIENT_SECRET="<client secret>"
    REDIRECT_URI="http://127.0.0.1:5000/callback/"
    SECRET_KEY="development key"
    ```
  - Replace ```<Client ID>``` and ```<client secret>``` with the CLIENT_ID and CLIENT_SECRET from the app you created in the Spotify developer dashboard
  - The secret key value can be any string. It shouldn't matter for the purposes of testing locally.
* Create a new python virtual environment for this project (the examples assume you're using windows)
 - This can be done either in the project root folder or in a dedicated virtual environments folder if you have one.
   - Create virtual environment in project root folder
     - Navigate to the project folder you cloned earlier
       - ex: ```cd \path\to\clonedfolder```
     - Run the command ```python venv <name of virtual environment```
       - ex: ```C:\code\DevOpsProject> python -m venv testenv```
     - Activate the new virtual environment
       - ex: ```C:\code\DevOpsProject> .\testenv\Scripts\activate```
     - Install the required packages
       - ```(testenv) PS C:\code\DevOpsProject> pip install -r .\requirements.txt```
  - Create virtual environment in a dedicated folder
    - Navigate to the folder you want to create the virtual environment in
      - ex: ```cd \path\to\virtualenvironmentsfolder```
    - Run the command ```python -m venv <name of virtual environment>```
      - ex: ```C:\code\DevOpsProject> python -m venv testenv```
    - Activate the new virtual environment
      - ex: ```C:\code\DevOpsProject> .\testenv\Scripts\activate```
    - Install the required packages
      - ```(testenv) PS C:\code\DevOpsProject> pip install -r .\requirements.txt```

# How to run/use
* Activate the virtual environment you made previously then use the command ```flask run```
* Navigate to http://127.0.0.1:5000 in your browser
* Use the navigation bar to navigate to the different features of the website
* To use the search features, enter the name of the artist, song, or album you want to search for in the search bar and click the search button.
* To use the song recommender feature, select the 'Recommender' navigation menu, then select up to 5 music genres and click the submit button. You will be given a song recommendations based on the genres you selected.
* To use the user profile feature, click the 'User Profile' navigation menu and log in with your Spotify account. You will be able to view your profile information.
* For manage playlist, the user must be logged in, then for the results of one of our other features you can add songs into your private or public playlists using a dropdown.
