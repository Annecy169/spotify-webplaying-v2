import sys
sys.path.append("./dependencies")
import os
import json
from flask import Flask, request, jsonify
import spotipy
import datetime
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

os.environ["SPOTIPY_USERNAME"] = 'Annecy48'
os.environ["SPOTIPY_CLIENT_ID"] = '4ebcec8e3cc5497c8f920cd8d5db1aca'
os.environ["SPOTIPY_CLIENT_SECRET"] = '6dbbd33acbfa4df08f216b0bca0e8006'
os.environ["SPOTIPY_REDIRECT_URI"] ='http://localhost'

scope = 'user-read-currently-playing'
token = spotipy.util.prompt_for_user_token(os.environ["SPOTIPY_USERNAME"], scope=scope, client_id=os.environ["SPOTIPY_CLIENT_ID"], client_secret=os.environ["SPOTIPY_CLIENT_SECRET"], redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"], cache_path=None)

sp = spotipy.Spotify(auth=token)
results = sp.current_user_playing_track()

print("Now Playing - {}".format(results["item"]["name"]))
print("---")
print(results)