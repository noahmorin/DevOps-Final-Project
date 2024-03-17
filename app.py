from flask import Flask, render_template, request, redirect
from userInfo import user_result, user_name, user_profile_image, userPlaylist
from userAuth import spotify_login, set_token

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# Link to user profile
@app.route('/userInfo', methods=['GET', 'POST'])
def user_info_route():
    userProfileInfo = user_result()

    #If users token has not been loaded sends to login page then gets the data from userInfo and loads into page
    if userProfileInfo == "login":
       return redirect('/login')
    else:
       userName = user_name(userProfileInfo)
       userProfileImg = user_profile_image(userProfileInfo)
       userPlaylistInfo = userPlaylist()
       return render_template('userProfile.html', result = userName, img = userProfileImg, names = userPlaylistInfo)

# Link to allow user to log into spotify account
@app.route('/login', methods=['GET', 'POST'])
def userLogin():
   # Gets the link from spotify_login page and redirects to login link
   authUrl = spotify_login()
   return redirect(authUrl)

@app.route('/callback/')
def callBack():
   # Set the token in the .env file and redirects back to user profile page
   set_token()
   return redirect('/userInfo')