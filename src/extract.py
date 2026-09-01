def get_artist_by_name(spotify, artist_name: str):
    results = spotify.search(
        q=artist_name,
        type="artist",
        limit=1,
    )

    artists = results["artists"]["items"]

    if not artists:
        return None

    return artists[0]


def get_artist_albums(spotify, artist_id: str):
    results = spotify.artist_albums(
        artist_id,
        album_type="album",
        limit=10,
    )

    return results["items"]

