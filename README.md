# Project Description
Our project uses the Spotify Web API and allows the user to search for various information about artists, songs, albums, and more.

# Features
- Search for a Spotify artist, which displays different information about them, like their photo and style of music
- Displays an artists most popular songs, and displays which album they are part of and when that album was released
- ADD FEATURES AND ADD SHORT DESCRIPTION


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
* Create a file named **.env** in the root folder of the cloned repository
  - Add the lines
    ```
    CLIENT_ID="<client ID>"
    CLIENT_SECRET="<client secret>"
    REDIRECT_URI="http://127.0.0.1:5000/callback/"
    ```
  - Replace ```<Client ID>``` and ```<client secret>``` with the CLIENT_ID and CLIENT_SECRET from the app you created in the Spotify developer dashboard
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
* Navigate to ```http://127.0.0.1:5000``` in your browser
* next step... NOT FINISHED
