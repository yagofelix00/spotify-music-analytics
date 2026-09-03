import pandas as pd

from src.extract import get_album_tracks, get_artist_albums, get_artist_by_name
from src.spotify_client import get_spotify_client


ARTIST_NAMES = [
    "Eminem",
    "Linkin Park",
    "Pink Floyd",
    "Dire Straits",
    "Eagles",
]


def main():
    spotify = get_spotify_client()

    tracks_data = []

    for artist_name in ARTIST_NAMES:
        artist = get_artist_by_name(spotify, artist_name)

        if not artist:
            print(f"Artist not found: {artist_name}")
            continue

        albums = get_artist_albums(
            spotify,
            artist["id"],
        )

        for album in albums:
            tracks = get_album_tracks(
                spotify,
                album["id"],
            )

            for track in tracks:
                tracks_data.append(
                    {
                        "spotify_id": track["id"],
                        "name": track["name"],
                        "album_id": album["id"],
                        "album_name": album["name"],
                        "artist_id": artist["id"],
                        "artist_name": artist["name"],
                        "disc_number": track["disc_number"],
                        "track_number": track["track_number"],
                        "duration_ms": track["duration_ms"],
                        "explicit": track["explicit"],
                        "spotify_url": track["external_urls"]["spotify"],
                    }
                )

    df = pd.DataFrame(tracks_data)

    print(df)


if __name__ == "__main__":
    main()