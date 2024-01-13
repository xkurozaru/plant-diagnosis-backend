from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from src import config
from src.domain.common import date_time

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/sign-in")


def authorize(token: str = Depends(oauth2_scheme)) -> str:
    try:
        user_id = decode_token(token)
    except Exception:
        raise Exception("Invalid token")
    return user_id


def generate_token(user_id: str) -> str:
    data = {
        "user_id": user_id,
        "exp": date_time.add_days_to_date_time(date_time.date_time_now(), 1),
    }
    token = jwt.encode(data, config.SECRET_KEY, algorithm="HS256")

    return token


def decode_token(token: str) -> str:
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
    except Exception:
        raise Exception("Invalid token")
    return payload.get("user_id")
