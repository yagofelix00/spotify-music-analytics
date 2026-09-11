import pandas as pd


def clean_text_columns(
    df: pd.DataFrame,
    columns: list[str],
) -> pd.DataFrame:
    df = df.copy()

    for column in columns:
        df[column] = df[column].str.strip()

    return df


def transform_artists(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_text_columns(
        df,
        [
            "spotify_id",
            "name",
            "type",
            "spotify_url",
        ],
    )

    return df


def transform_albums(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_text_columns(
        df,
        [
            "spotify_id",
            "name",
            "artist_id",
            "artist_name",
            "album_type",
            "spotify_url",
        ],
    )

    return df

def transform_tracks(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_text_columns(
        df,
        [
            "spotify_id",
            "name",
            "album_id",
            "album_name",
            "artist_id",
            "artist_name",
            "spotify_url",
        ],
    )

    return df