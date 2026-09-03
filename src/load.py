from pathlib import Path

import pandas as pd


RAW_DATA_DIR = Path("data/raw")


def save_dataframe(df: pd.DataFrame, filename: str) -> None:
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    file_path = RAW_DATA_DIR / filename

    df.to_csv(
        file_path,
        index=False,
        encoding="utf-8",
    )

    print(f"Saved {len(df)} rows to {file_path}")