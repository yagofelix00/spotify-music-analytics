import pandas as pd

from src.transform import transform_albums, transform_artists


def test_transform_artists_strips_text_columns():
    df = pd.DataFrame(
        [
            {
                "spotify_id": " 123 ",
                "name": " Eminem ",
                "type": " artist ",
                "spotify_url": " https://open.spotify.com/artist/123 ",
            }
        ]
    )

    result = transform_artists(df)

    assert result.loc[0, "spotify_id"] == "123"
    assert result.loc[0, "name"] == "Eminem"
    assert result.loc[0, "type"] == "artist"
    assert result.loc[0, "spotify_url"] == "https://open.spotify.com/artist/123"


def test_transform_albums_strips_text_columns():
    df = pd.DataFrame(
        [
            {
                "spotify_id": " abc ",
                "name": " Recovery ",
                "artist_id": " 123 ",
                "artist_name": " Eminem ",
                "album_type": " album ",
                "total_tracks": 17,
                "spotify_url": " https://open.spotify.com/album/abc ",
            }
        ]
    )

    result = transform_albums(df)

    assert result.loc[0, "spotify_id"] == "abc"
    assert result.loc[0, "name"] == "Recovery"
    assert result.loc[0, "artist_id"] == "123"
    assert result.loc[0, "artist_name"] == "Eminem"
    assert result.loc[0, "album_type"] == "album"