from src.data_quality import load_raw_dataset
from src.transform import (
    transform_albums, 
    transform_artists, 
    transform_tracks, 
    add_track_features
    )
from src.validate import validate_relationships

def main():
    artists_raw = load_raw_dataset("artists.csv")
    albums_raw = load_raw_dataset("albums.csv")
    tracks_raw = load_raw_dataset("tracks.csv")

    artists_processed = transform_artists(artists_raw)
    albums_processed = transform_albums(albums_raw)
    tracks_processed = transform_tracks(tracks_raw)
    tracks_processed = add_track_features(tracks_processed)
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

    validation = validate_relationships(
        artists_processed,
        albums_processed,
        tracks_processed,
    )

    print("\nRELATIONSHIP VALIDATION")

    for key, value in validation.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()