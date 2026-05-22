from pathlib import Path
from config import PROCESSED_DIR, OUTPUT_TABLES, OUTPUT_CHARTS
from load_data import load_all_data
from clean_features import clean_and_engineer
from analyze import (
    summarize_by_member, summarize_by_month, summarize_by_hour,
    summarize_by_day, summarize_by_bike, top_routes, year_over_year
)
from visualize import (
    save_bar_member, save_monthly_line, save_hourly_line, save_weekday_bar
)

def ensure_dirs():
    for p in [PROCESSED_DIR, OUTPUT_TABLES, OUTPUT_CHARTS]:
        p.mkdir(parents=True, exist_ok=True)

def main():
    ensure_dirs()

    raw_df = load_all_data()
    df = clean_and_engineer(raw_df)

    df.to_parquet(PROCESSED_DIR / "divvy_2024_2025_clean.parquet", index=False)

    by_member = summarize_by_member(df)
    by_month = summarize_by_month(df)
    by_hour = summarize_by_hour(df)
    by_day = summarize_by_day(df)
    by_bike = summarize_by_bike(df)
    routes = top_routes(df, top_n=20)
    yoy = year_over_year(df)

    by_member.to_csv(OUTPUT_TABLES / "by_member.csv", index=False)
    by_month.to_csv(OUTPUT_TABLES / "by_month.csv", index=False)
    by_hour.to_csv(OUTPUT_TABLES / "by_hour.csv", index=False)
    by_day.to_csv(OUTPUT_TABLES / "by_day.csv", index=False)
    by_bike.to_csv(OUTPUT_TABLES / "by_bike.csv", index=False)
    routes.to_csv(OUTPUT_TABLES / "top_routes.csv", index=False)
    yoy.to_csv(OUTPUT_TABLES / "year_over_year.csv", index=False)

    save_bar_member(by_member)
    save_monthly_line(by_month)
    save_hourly_line(by_hour)
    save_weekday_bar(by_day)

if __name__ == "__main__":
    main()