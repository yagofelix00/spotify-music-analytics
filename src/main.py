import pandas as pd

from src.extract import get_artist_albums, get_artist_by_name
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

    albums_data = []

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
            albums_data.append(
                {
                    "spotify_id": album["id"],
                    "name": album["name"],
                    "artist_id": artist["id"],
                    "artist_name": artist["name"],
                    "album_type": album["album_type"],
                    "total_tracks": album["total_tracks"],
                    "spotify_url": album["external_urls"]["spotify"],
                }
            )

    df = pd.DataFrame(albums_data)

    print(df)


if __name__ == "__main__":
    main()