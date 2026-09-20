import pandas as pd

from src.validate import validate_relationships


def test_validate_relationships_with_valid_data():
    artists_df = pd.DataFrame(
        [
            {
                "spotify_id": "artist1",
            }
        ]
    )

    albums_df = pd.DataFrame(
        [
            {
                "spotify_id": "album1",
                "artist_id": "artist1",
            }
        ]
    )

    tracks_df = pd.DataFrame(
        [
            {
                "spotify_id": "track1",
                "artist_id": "artist1",
                "album_id": "album1",
            }
        ]
    )

    result = validate_relationships(
        artists_df,
        albums_df,
        tracks_df,
    )

    assert result["orphan_albums"] == 0
    assert result["orphan_tracks_by_artist"] == 0
    assert result["orphan_tracks_by_album"] == 0
    

def test_validate_relationships_detects_orphans():
    artists_df = pd.DataFrame(
        [
            {
                "spotify_id": "artist1",
            }
        ]
    )

    albums_df = pd.DataFrame(
        [
            {
                "spotify_id": "album1",
                "artist_id": "unknown_artist",
            }
        ]
    )

    tracks_df = pd.DataFrame(
        [
            {
                "spotify_id": "track1",
                "artist_id": "unknown_artist",
                "album_id": "unknown_album",
            }
        ]
    )

    result = validate_relationships(
        artists_df,
        albums_df,
        tracks_df,
    )

    assert result["orphan_albums"] == 1
    assert result["orphan_tracks_by_artist"] == 1
    assert result["orphan_tracks_by_album"] == 1
