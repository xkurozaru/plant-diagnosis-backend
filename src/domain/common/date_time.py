from datetime import datetime, timedelta


def date_time_now() -> datetime:
    return datetime.now()


def add_days_to_date_time(date_time: datetime, days: int) -> datetime:
    return date_time + timedelta(days=days)
