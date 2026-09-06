from src.data_quality import inspect_dataframe, load_raw_dataset


DATASETS = [
    "artists.csv",
    "albums.csv",
    "tracks.csv",
]


def main():
    for filename in DATASETS:
        df = load_raw_dataset(filename)

        inspect_dataframe(
            df,
            filename,
        )


if __name__ == "__main__":
    main()