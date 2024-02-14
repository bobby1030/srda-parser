import os, time

from .. import logger
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import OperationalError

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
    for _ in range(10):
        try:
            if not check_db_exist():
                create_database(db_url)

            engine = create_engine(db_url)
            return engine
        except OperationalError:
            logger.warning("Connection to database failed. Retrying in 5 seconds...")
            time.sleep(5)
            continue
    else:
        logger.error("Connection to database failed. Exiting...")
        raise SystemExit(1)


engine = get_db_engine()
Session = sessionmaker(bind=engine)
ScopedSession = scoped_session(Session)
