from datetime import datetime, timedelta

from pytz import timezone


def date_time_now() -> datetime:
    return datetime.now(timezone("Asia/Tokyo"))


def add_days_to_date_time(date_time: datetime, days: int) -> datetime:
    return date_time + timedelta(days=days)
