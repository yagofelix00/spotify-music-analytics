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

    print("\nFully duplicated rows:")
    print(df.duplicated().sum())

    if "spotify_id" in df.columns:
        print("\nDuplicated Spotify IDs:")
        print(df["spotify_id"].duplicated().sum())

    print("\nSample:")
    print(df.head())