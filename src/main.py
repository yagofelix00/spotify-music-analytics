import pandas as pd

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

    artists_data = []

    for artist_name in ARTIST_NAMES:
        results = spotify.search(
            q=artist_name,
            type="artist",
            limit=1,
        )

        artists = results["artists"]["items"]

        if not artists:
            print(f"Artist not found: {artist_name}")
            continue

        artist = artists[0]

        artists_data.append(
            {
                "spotify_id": artist["id"],
                "name": artist["name"],
                "type": artist["type"],
                "spotify_url": artist["external_urls"]["spotify"],
            }
        )

    df = pd.DataFrame(artists_data)

    print(df)


if __name__ == "__main__":
    main()