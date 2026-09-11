from src.data_quality import load_raw_dataset
from src.transform import transform_albums, transform_artists, transform_tracks


def main():
    artists_raw = load_raw_dataset("artists.csv")
    albums_raw = load_raw_dataset("albums.csv")
    tracks_raw = load_raw_dataset("tracks.csv")

    artists_processed = transform_artists(artists_raw)
    albums_processed = transform_albums(albums_raw)
    tracks_processed = transform_tracks(tracks_raw)

    print("\nARTISTS")
    print(f"Raw shape: {artists_raw.shape}")
    print(f"Processed shape: {artists_processed.shape}")
    print(f"Data changed: {not artists_raw.equals(artists_processed)}")

    print("\nALBUMS")
    print(f"Raw shape: {albums_raw.shape}")
    print(f"Processed shape: {albums_processed.shape}")
    print(f"Data changed: {not albums_raw.equals(albums_processed)}")

    print("\nTRACKS")
    print(f"Raw shape: {tracks_raw.shape}")
    print(f"Processed shape: {tracks_processed.shape}")
    print(f"Data changed: {not tracks_raw.equals(tracks_processed)}")


if __name__ == "__main__":
    main()