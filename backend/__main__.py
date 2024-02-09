import os

from . import logger
from .db.database import check_db_exist
from .db.createdb import createdb
from .db.embedding import embedding

# build database schema and load data
if not check_db_exist():
    logger.info("Database does not exist")
    createdb()
elif os.environ.get("REBUILD_DB") == "1":
    logger.info("Rebuild of database requested")
    createdb()
else:
    logger.info("Database found")

# fill embeddings
logger.info("Requesting embeddings...")
embedding()
