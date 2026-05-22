from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
OUTPUT_TABLES = BASE_DIR / "output" / "tables"
OUTPUT_CHARTS = BASE_DIR / "output" / "charts"

VALID_MEMBER_TYPES = {"member", "casual"}
DAY_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]