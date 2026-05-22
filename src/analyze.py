import pandas as pd
from config import DAY_ORDER

def summarize_by_member(df):
    out = df.groupby("member_casual").agg(
        rides=("ride_id", "count"),
        avg_duration_min=("ride_length_min", "mean"),
        median_duration_min=("ride_length_min", "median")
    ).reset_index()
    out["ride_share_pct"] = 100 * out["rides"] / out["rides"].sum()
    return out

def summarize_by_month(df):
    return df.groupby(["month", "member_casual"]).agg(
        rides=("ride_id", "count"),
        avg_duration_min=("ride_length_min", "mean")
    ).reset_index()

def summarize_by_hour(df):
    return df.groupby(["hour", "member_casual"]).agg(
        rides=("ride_id", "count"),
        avg_duration_min=("ride_length_min", "mean")
    ).reset_index()

def summarize_by_day(df):
    out = df.groupby(["day_of_week", "member_casual"]).agg(
        rides=("ride_id", "count"),
        avg_duration_min=("ride_length_min", "mean")
    ).reset_index()
    out["day_of_week"] = pd.Categorical(out["day_of_week"], categories=DAY_ORDER, ordered=True)
    return out.sort_values(["day_of_week", "member_casual"])

def summarize_by_bike(df):
    return df.groupby(["rideable_type", "member_casual"]).agg(
        rides=("ride_id", "count"),
        avg_duration_min=("ride_length_min", "mean")
    ).reset_index()

def top_routes(df, top_n=15):
    return (
        df.groupby(["member_casual", "route"])
        .agg(rides=("ride_id", "count"))
        .reset_index()
        .sort_values(["member_casual", "rides"], ascending=[True, False])
        .groupby("member_casual")
        .head(top_n)
    )

def year_over_year(df):
    out = df.groupby(["year", "member_casual"]).agg(
        rides=("ride_id", "count"),
        avg_duration_min=("ride_length_min", "mean")
    ).reset_index()
    return out