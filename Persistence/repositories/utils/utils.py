from datetime import datetime

def detect_date_type(date_str: str):
    formats = {
        "%Y": "year",
        "%Y-%m": "month",
        "%Y-%m-%d": "day",
    }
    for fmt, label in formats.items():
        try:
            datetime.strptime(date_str, fmt)
            return label
        except ValueError:
            continue
    raise ValueError("Invalid date format")