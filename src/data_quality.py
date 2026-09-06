from pathlib import Path

import pandas as pd


RAW_DATA_DIR = Path("data/raw")


def load_raw_dataset(filename: str) -> pd.DataFrame:
    file_path = RAW_DATA_DIR / filename

    return pd.read_csv(file_path)


def inspect_dataframe(df: pd.DataFrame, name: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"DATASET: {name}")
    print(f"{'=' * 60}")

    print(f"\nShape: {df.shape}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nEmpty strings:")
    for column in df.select_dtypes(include="str").columns:
        empty_count = df[column].str.strip().eq("").sum()
        print(f"{column}: {empty_count}")

    # Numeric validations
    if "total_tracks" in df.columns:
        print("\nInvalid total_tracks:")
        print((df["total_tracks"] <= 0).sum())

    if "duration_ms" in df.columns:
        print("\nInvalid duration_ms:")
        print((df["duration_ms"] <= 0).sum())

    if "track_number" in df.columns:
        print("\nInvalid track_number:")
        print((df["track_number"] <= 0).sum())

    if "disc_number" in df.columns:
        print("\nInvalid disc_number:")
        print((df["disc_number"] <= 0).sum())

    # Category validations
    if "type" in df.columns:
        print("\nUnique type values:")
        print(df["type"].value_counts(dropna=False))

    if "album_type" in df.columns:
        print("\nUnique album_type values:")
        print(df["album_type"].value_counts(dropna=False))
       
    print("\nFully duplicated rows:")
    print(df.duplicated().sum())

    if "spotify_id" in df.columns:
        print("\nDuplicated Spotify IDs:")
        print(df["spotify_id"].duplicated().sum())

    print("\nSample:")
    print(df.head())