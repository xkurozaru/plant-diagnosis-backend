from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), "JST")


def date_time_now() -> datetime:
    return datetime.now(JST)


def add_days_to_date_time(date_time: datetime, days: int) -> datetime:
    return date_time + timedelta(days=days)
