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

@app.route('/spotify')
def spotify():
    token = spotipy.util.prompt_for_user_token(os.environ["SPOTIPY_USERNAME"], scope=scope, client_id=os.environ["SPOTIPY_CLIENT_ID"], client_secret=os.environ["SPOTIPY_CLIENT_SECRET"], redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"], cache_path=None)
    sp = spotipy.Spotify(auth=token)

    results = sp.current_user_playing_track()
    artists = []
    for artist in results["item"]["artists"]:
        artists.append(artist["name"])
    length = round((results["item"]["duration_ms"] / 60000), 2)
    current_position = round((results["progress_ms"] / 60000), 2)
    json_body = {
        "name": results["item"]["name"],
        "length": length,
        "current_position": current_position,
        "bar_state":  "%s%%" % ((current_position / length) * 100),
        "art": results["item"]["album"]["images"][0]["url"],
        "artists": ', '.join(artists)
    }
    try:
        return json_body
    except:
        return "None"

@app.route('/style.css')
def styling():
    file = open('./build/style.css',mode='r')
    css_styling = file.read()
    file.close()
    return css_styling

@app.route('/')
def main():
    file = open('./build/index.html',mode='r')
    index_html = file.read()
    file.close()
    return index_html


if __name__ == '__main__':
    app.run()