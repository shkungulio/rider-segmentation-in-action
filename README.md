# Rider Segmentation in Action:  
**Divvy Member vs Casual Usage Analytics**

This project is an end-to-end analytics case study that applies the CRISP-DM framework to 24 months of Divvy trip data from January 2024 through December 2025. The goal is to understand how members and casual riders use Divvy differently and to translate those behavioral differences into actionable business recommendations for shared micromobility operations, marketing, and rider conversion.

## CRISP-DM overview

CRISP-DM structures the project into six phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment. This README uses that framework to organize the work as a portfolio-ready analytics case study rather than a generic exploratory analysis exercise.

## 1. Business understanding

The central business problem is to determine how Divvy members and casual riders differ in their behavior and how those differences can support better operational and commercial decisions. The analysis is designed to answer questions about trip frequency, ride duration, seasonality, commuting behavior, station usage, and bike-type preferences across rider segments.

### Business objectives

- Identify key behavioral differences between member and casual riders.
- Understand when and where each segment uses Divvy most often.
- Support recommendations for membership conversion, station balancing, and seasonal bike allocation.
- Present the work as an end-to-end analytics case study suitable for a data analytics portfolio.

### Key business questions

- Do members and casual riders show different weekday, weekend, and hourly usage patterns?
- Are casual riders more concentrated in leisure or tourist-oriented trips while members exhibit commuter behavior?
- Which bike types are more popular with each rider segment?
- How did rider behavior change between 2024 and 2025?

## 2. Data understanding

The dataset consists of 24 monthly Divvy trip files covering January 2024 through December 2025. Each trip record contains ride timestamps, bike type, rider class, station information, and trip coordinates, which support both temporal and route-based analysis.

### Available fields

The Divvy files show the core schema used throughout the project, including the following columns:

- `ride_id`
- `rideable_type`
- `started_at`, `ended_at`
- `start_station_name`, `start_station_id`
- `end_station_name`, `end_station_id`
- `start_lat`, `start_lng`, `end_lat`, `end_lng`
- `member_casual`

### Data understanding goals

- Confirm consistent schema across all monthly files.
- Check for null or inconsistent station values, especially for certain bike trips.
- Understand the distribution of ride durations and detect invalid trips.
- Verify that `member_casual` can be used reliably for rider segmentation.

## 3. Data preparation

The preparation phase combines all monthly files into one analysis-ready dataset and creates the features needed for rider-segmentation analysis. This phase forms the foundation of the project because the quality of the behavioral comparisons depends on consistent timestamps, valid trip durations, and standardized rider and bike-type values.

### Cleaning steps

- Combine all 24 monthly CSV files into one unified dataset.
- Standardize column names and data types.
- Convert `started_at` and `ended_at` into datetime fields.
- Remove invalid rides, such as negative durations, zero-length trips, and unrealistic outliers.
- Standardize `member_casual` and `rideable_type` values for consistent grouping.

### Feature engineering

- `ride_length_min`: trip duration in minutes.
- `year` and `month`: for year-over-year and seasonal analysis.
- `day_of_week` and `hour`: for weekly and hourly behavior analysis.
- `weekend`: indicator to separate leisure-oriented behavior from weekday usage.
- `route`: start-station to end-station pair for route analysis.
- `round_trip`: indicator for rides that start and end at the same station.

### Prepared outputs

- Cleaned analysis dataset.
- Aggregated summary tables by rider type, month, hour, weekday, bike type, and route.
- Visualization-ready datasets saved to the `output/` directory.

## 4. Modeling

The project uses descriptive and segmentation-focused analytics rather than predictive machine learning. In the CRISP-DM context, the modeling phase centers on aggregation logic, behavioral comparison, and pattern detection across the member and casual rider segments.

### Analytical approach

The analysis compares members and casual riders across multiple behavioral dimensions:

- Total ride volume and ride share.
- Monthly seasonality and year-over-year changes.
- Day-of-week and hour-of-day usage patterns.
- Ride duration differences.
- Bike-type preferences.
- Top origin-destination routes by rider segment.

### Planned analysis artifacts

- Bar charts for total rides and bike-type preferences.
- Line charts for monthly and hourly usage trends.
- Weekday comparison charts for member versus casual behavior.
- Route-level summary tables to distinguish commuting and leisure patterns.

## 5. Evaluation

The evaluation phase determines whether the analysis answers the business questions clearly and credibly. Success is measured not by model accuracy, but by whether the results reveal distinct rider-segment behaviors that can support business decisions.

### Evaluation criteria

- Whether the results clearly distinguish member and casual usage patterns.
- Whether the observed patterns are consistent across multiple views, such as month, day, hour, and route.
- Whether the cleaning and feature-engineering steps are transparent and reproducible.
- Whether the findings lead to practical recommendations for marketing and operations.

### Expected findings

This section should be updated once the full analysis is complete. Likely findings include stronger weekday commute peaks among members, heavier weekend and leisure-oriented riding among casual users, and segment-level differences in trip duration or electric-bike usage.

## 6. Deployment

The deployment phase focuses on presenting the analysis in a reproducible, portfolio-ready format that can be reviewed by recruiters, hiring managers, or stakeholders. The project is designed for a Python script workflow in VS Code so the full pipeline can be rerun from raw data through cleaned outputs, tables, and charts.

### Deliverables

- A modular Python project with reusable scripts.
- A cleaned, analysis-ready dataset.
- Aggregated summary tables.
- Charts highlighting rider-segment behavior.
- A final README with business context, methods, findings, and recommendations.

### Recommended project structure

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



## Business actions

The final business recommendations are expected to connect rider-segmentation findings to operational and growth opportunities. Potential actions include converting high-frequency casual users into members, improving weekday dock availability near commuter corridors, increasing weekend capacity near leisure destinations, and aligning bike allocation with seasonal demand shifts.

## Tools

Suggested tools for this project include pandas and NumPy for data preparation, matplotlib or seaborn for visualization, and pyarrow for efficient storage of processed outputs. A script-based VS Code workflow keeps the project modular, reproducible, and easy to maintain as the analysis evolves.

## Portfolio value

This project demonstrates an end-to-end analytics workflow using real trip-level mobility data and a recognized industry methodology. Organizing the work with CRISP-DM makes the project easier to explain to recruiters because it shows business framing, structured analysis, reproducible preparation, and clear decision-oriented outcomes.