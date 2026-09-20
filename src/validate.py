import pandas as pd


def validate_relationships(
    artists_df: pd.DataFrame,
    albums_df: pd.DataFrame,
    tracks_df: pd.DataFrame,
) -> dict[str, int]:
    artist_ids = set(artists_df["spotify_id"])
    album_ids = set(albums_df["spotify_id"])

    orphan_albums = (~albums_df["artist_id"].isin(artist_ids)).sum()

    orphan_tracks_by_artist = (
        ~tracks_df["artist_id"].isin(artist_ids)
    ).sum()

    orphan_tracks_by_album = (
        ~tracks_df["album_id"].isin(album_ids)
    ).sum()

    return {
        "orphan_albums": int(orphan_albums),
        "orphan_tracks_by_artist": int(orphan_tracks_by_artist),
        "orphan_tracks_by_album": int(orphan_tracks_by_album),
    }