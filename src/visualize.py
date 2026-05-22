import matplotlib.pyplot as plt
import seaborn as sns
from config import OUTPUT_CHARTS

sns.set_theme(style="darkgrid")

def save_bar_member(summary_df):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=summary_df, x="member_casual", y="rides", hue="member_casual", legend=False)
    plt.title("Total Divvy Rides by User Type")
    plt.xlabel("User Type")
    plt.ylabel("Rides")
    plt.tight_layout()
    plt.savefig(OUTPUT_CHARTS / "rides_by_user_type.png", dpi=200)
    plt.close()

def save_monthly_line(month_df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=month_df, x="month", y="rides", hue="member_casual", marker="o")
    plt.title("Monthly Divvy Rides by User Type")
    plt.xlabel("Month")
    plt.ylabel("Rides")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_CHARTS / "monthly_rides_by_user_type.png", dpi=200)
    plt.close()

def save_hourly_line(hour_df):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=hour_df, x="hour", y="rides", hue="member_casual")
    plt.title("Hourly Divvy Usage by User Type")
    plt.xlabel("Hour of Day")
    plt.ylabel("Rides")
    plt.tight_layout()
    plt.savefig(OUTPUT_CHARTS / "hourly_usage.png", dpi=200)
    plt.close()

def save_weekday_bar(day_df):
    plt.figure(figsize=(10, 5))
    sns.barplot(data=day_df, x="day_of_week", y="rides", hue="member_casual")
    plt.title("Day-of-Week Usage by User Type")
    plt.xlabel("Day of Week")
    plt.ylabel("Rides")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(OUTPUT_CHARTS / "weekday_usage.png", dpi=200)
    plt.close()