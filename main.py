import sys
sys.path.append("./dependencies")
import os
import json
from flask import Flask, request, jsonify
import spotipy
import datetime
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

scope = 'user-read-currently-playing'
token = spotipy.util.prompt_for_user_token(os.environ["SPOTIPY_USERNAME"], scope=scope, client_id=os.environ["SPOTIPY_CLIENT_ID"], client_secret=os.environ["SPOTIPY_CLIENT_SECRET"], redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"], cache_path=None)

sp = spotipy.Spotify(auth=token)

# print("Now Playing - {}".format(results["item"]["name"]))
# print("---")
# print(results)

@app.route('/spotify')
def spotify():
    results = sp.current_user_playing_track()
    return "Now Playing - {}".format(results["item"]["name"])

@app.route('/')
def main():

    body = """<html>
    <body>

    <h2>The XMLHttpRequest Object</h2>

    <p id="demo"></p>

    <script>
    function loadDoc() {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            document.getElementById("demo").innerHTML = this.responseText;
        };
        xhttp.open("GET", "http://localhost:5000/spotify", true);
        xhttp.send();
    }
    window.setInterval(function(){
        loadDoc();
    }, 5000);
    </script>

    </body>
    </html>"""
    return body


if __name__ == '__main__':
    app.run()