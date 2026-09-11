import pandas as pd

from src.transform import transform_albums, transform_artists, transform_tracks


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


def test_transform_tracks_strips_text_columns():
    df = pd.DataFrame(
        [
            {
                "spotify_id": " track123 ",
                "name": " Stan ",
                "album_id": " album123 ",
                "album_name": " The Marshall Mathers LP ",
                "artist_id": " artist123 ",
                "artist_name": " Eminem ",
                "disc_number": 1,
                "track_number": 3,
                "duration_ms": 404106,
                "explicit": True,
                "spotify_url": " https://open.spotify.com/track/track123 ",
            }
        ]
    )

    result = transform_tracks(df)

    assert result.loc[0, "spotify_id"] == "track123"
    assert result.loc[0, "name"] == "Stan"
    assert result.loc[0, "album_id"] == "album123"
    assert result.loc[0, "album_name"] == "The Marshall Mathers LP"
    assert result.loc[0, "artist_id"] == "artist123"
    assert result.loc[0, "artist_name"] == "Eminem"
    assert result.loc[0, "spotify_url"] == "https://open.spotify.com/track/track123"