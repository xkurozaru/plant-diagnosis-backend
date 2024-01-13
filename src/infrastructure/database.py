from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from src import config

ENGINE = create_engine(config.DB_URL)
session = scoped_session(sessionmaker(bind=ENGINE))


def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()
