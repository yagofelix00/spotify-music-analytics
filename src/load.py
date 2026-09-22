from pathlib import Path

import pandas as pd


RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")


def save_dataframe(
    df: pd.DataFrame,
    filename: str,
    directory: Path,
) -> None:
    directory.mkdir(parents=True, exist_ok=True)

    file_path = directory / filename

    df.to_csv(
        file_path,
        index=False,
        encoding="utf-8",
    )

    print(f"Saved {len(df)} rows to {file_path}")


def save_raw_dataframe(df: pd.DataFrame, filename: str) -> None:
    save_dataframe(
        df,
        filename,
        RAW_DATA_DIR,
    )


def save_processed_dataframe(df: pd.DataFrame, filename: str) -> None:
    save_dataframe(
        df,
        filename,
        PROCESSED_DATA_DIR,
    )