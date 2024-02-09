from . import logger
from .db.createdb import createdb

# build database schema and load data
try:
    logger.info("Building database schema and loading data...")
    createdb()
except Exception as e:
    logger.error(e)