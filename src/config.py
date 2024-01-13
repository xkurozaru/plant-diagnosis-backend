import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

HOST = os.getenv("DATABASE_HOST")
USER = os.getenv("DATABASE_USERNAME")
PASSWD = os.getenv("DATABASE_PASSWORD")
DB = os.getenv("DATABASE")
DB_URL = f"mysql://{USER}:{PASSWD}@{HOST}/{DB}"

SALT = os.environ.get("HASH_SALT")
ITER = os.environ.get("HASH_ITER_NUM")

SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
