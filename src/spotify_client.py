import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials


load_dotenv()


def get_spotify_client() -> spotipy.Spotify:
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise RuntimeError(
            "Spotify credentials were not found. "
            "Check SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET in the .env file."
        )

    auth_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret,
    )

    return spotipy.Spotify(auth_manager=auth_manager)