import pandas as pd
import numpy as np

def clean_and_engineer(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = [c.strip().lower() for c in df.columns]

    df["started_at"] = pd.to_datetime(df["started_at"], errors="coerce")
    df["ended_at"] = pd.to_datetime(df["ended_at"], errors="coerce")

    df["member_casual"] = df["member_casual"].astype(str).str.strip().str.lower()
    df["rideable_type"] = (
        df["rideable_type"]
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace("bike", "_bike", regex=False)
        .str.replace("__", "_", regex=False)
    )

    df["ride_length_min"] = (df["ended_at"] - df["started_at"]).dt.total_seconds() / 60

    df = df.dropna(subset=["started_at", "ended_at", "member_casual"])
    df = df[df["member_casual"].isin(["member", "casual"])]
    df = df[(df["ride_length_min"] > 1) & (df["ride_length_min"] < 1440)]

    df["year"] = df["started_at"].dt.year
    df["month"] = df["started_at"].dt.to_period("M").astype(str)
    df["month_num"] = df["started_at"].dt.month
    df["day_of_week"] = df["started_at"].dt.day_name()
    df["hour"] = df["started_at"].dt.hour
    df["weekend"] = df["day_of_week"].isin(["Saturday", "Sunday"])

    df["route"] = (
        df["start_station_name"].fillna("Unknown Start")
        + " → " +
        df["end_station_name"].fillna("Unknown End")
    )

    df["round_trip"] = df["start_station_id"].astype(str) == df["end_station_id"].astype(str)

    return df