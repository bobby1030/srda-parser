import os

from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database

db_url = URL.create(
    "postgresql+psycopg2",
    host=os.environ["POSTGRES_HOST"],
    port=os.environ["POSTGRES_PORT"],
    username=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
    database=os.environ["POSTGRES_DB"],
)


def check_db_exist():
    return database_exists(db_url)


def get_db_engine():
    if not check_db_exist():
        create_database(db_url)

    return create_engine(db_url)


engine = get_db_engine()
Session = sessionmaker(bind=engine)
ScopedSession = scoped_session(Session)