from src.spotify_client import get_spotify_client


def main():
    spotify = get_spotify_client()

    results = spotify.search(
        q="Eminem",
        type="artist",
        limit=1,
    )

    artists = results["artists"]["items"]

    if not artists:
        print("Artist not found.")
        return

    artist = artists[0]

    print(f"Name: {artist['name']}")
    print(f"Spotify ID: {artist['id']}")
    print(f"Type: {artist['type']}")
    print(f"Spotify URL: {artist['external_urls']['spotify']}")


if __name__ == "__main__":
    main()