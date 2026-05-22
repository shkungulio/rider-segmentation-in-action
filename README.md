# Rider Segmentation in Action: Divvy Member vs Casual Usage Analytics

This project is an end-to-end analytics case study using 24 months of Divvy bike trip data from January 2024 through December 2025 to understand how members and casual riders use the system differently. The analysis is designed as a portfolio-ready project that moves beyond generic exploratory analysis by focusing on rider segmentation, behavioral patterns, and business implications.

## Objective

The objective of this project is to identify how Divvy members and casual riders differ in their usage behavior across a two-year period. The analysis focuses on differences in trip volume, ride duration, seasonality, day-of-week behavior, hour-of-day trends, route patterns, and bike-type preferences.

## Data

The dataset consists of 24 monthly Divvy trip files covering January 2024 to December 2025. Each trip record includes ride timestamps, station names and IDs, start and end coordinates, bike type, and rider classification through the `member_casual` field. The uploaded sample files show the core schema used in the project, including fields such as `ride_id`, `rideable_type`, `started_at`, `ended_at`, station information, coordinates, and `member_casual`.

## Methods

The analysis begins by combining all monthly CSV files into a unified dataset and standardizing field names and formats. Data cleaning removes invalid or unrealistic trips, such as negative durations, zero-length rides, and extreme outliers, while timestamp fields are converted into analysis-ready datetime variables.

Feature engineering adds variables such as ride length in minutes, year, month, day of week, hour of day, weekend indicator, route pairs, and round-trip flags. Aggregations are then created by rider type, month, hour, weekday, route, and bike type to compare member and casual usage patterns consistently across the full period.

## Analysis focus

The project is structured around a rider-segmentation lens rather than generic EDA. Key questions include when members and casual riders ride, how long they ride, which bike types they prefer, which station pairs they use most often, and how these behaviors changed from 2024 to 2025.

Primary comparison areas include:

- Total rides and ride share by rider type.
- Monthly seasonality and year-over-year changes.
- Weekday versus weekend behavior.
- Hourly riding patterns and commuter peaks.
- Ride duration differences.
- Bike-type preferences.
- Top origin-destination routes by rider segment.


## Findings

This section should present the final computed insights once the full pipeline is run on all 24 files. Expected examples include stronger weekday commute peaks among members, heavier weekend and leisure-oriented usage among casual riders, and different preferences in ride duration or electric-bike adoption across rider segments. Final findings should be supported with charts and summary tables generated from the cleaned dataset.

## Implications

The analysis is intended to translate rider behavior into operational and commercial implications for a bike-share system. Member and casual differences can inform pricing strategy, membership conversion campaigns, station rebalancing, and seasonal bike allocation decisions.

Potential implications include:

- Converting high-frequency casual riders into members through targeted offers.
- Increasing bike and dock availability near commuter corridors during weekdays.
- Adjusting station coverage and rebalancing near leisure and tourist destinations on weekends.
- Planning seasonal operations around summer demand spikes and winter usage drops.


## Business actions

This project is positioned as an analytics case study with business relevance, not only as a technical exercise. Recommended actions should connect the findings to measurable decisions such as improving retention, expanding member acquisition, optimizing station operations, and allocating bike types more efficiently by segment and season.

## Project structure

A recommended Python project structure for this analysis is shown below:

```text
divvy-user-analysis/
├── data/
│   ├── raw/
│   └── processed/
├── output/
│   ├── charts/
│   └── tables/
├── src/
│   ├── config.py
│   ├── load_data.py
│   ├── clean_features.py
│   ├── analyze.py
│   ├── visualize.py
│   └── main.py
├── requirements.txt
└── README.md
```


## Tools

Suggested Python tools for this project include pandas and NumPy for data processing, matplotlib or seaborn for visualization, and pyarrow for efficient storage of processed datasets. A script-based workflow in VS Code helps keep the pipeline modular, reproducible, and easy to rerun as additional files or metrics are added.

## Deliverables

A complete version of this project should include:

- A cleaned, analysis-ready dataset.
- Aggregated summary tables by rider segment.
- Visualizations for monthly, hourly, weekday, and bike-type patterns.
- Route-level analysis for top station pairs.
- A final summary of behavioral differences between members and casual riders.
- Business recommendations based on rider segmentation insights.


## Portfolio value

This project demonstrates an end-to-end analytics workflow using real trip-level transportation data. It highlights practical skills in data cleaning, feature engineering, segmentation analysis, time-series aggregation, visualization, and business storytelling, which makes it suitable for analytics, BI, and data analyst portfolios.

<div align="center">THE END</div>
