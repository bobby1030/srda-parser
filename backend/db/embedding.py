import os
from openai import OpenAI

from sqlalchemy import select, update

from .. import logger
from .database import Session
from .models import Variable


def get_embedding_from_openai(input: list[str]):
    """
    Get embeddings from OpenAI API.
    """

    logger.info("Getting embeddings from OpenAI")

    # get embedding using OpenAI API
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    chunks = [input[i : i + 2000] for i in range(0, len(input), 2000)]
    embeddings = []

    for idx, chunk in enumerate(chunks):
        logger.info(f"Embedding chunk {idx + 1} of {len(chunks)}")

        response = client.embeddings.create(input=chunk, model="text-embedding-3-small")
        embeddings += [d.embedding for d in response.data]

    return embeddings


def get_rows_from_db(session):
    """
    Get rows to be embedded from database.
    """

    query = select(Variable).where(Variable.embedding.is_(None))
    result = session.scalars(query).all()

    return result


def append_embedding_to_db(session, rows, embeddings: list[str]):
    logger.info("Appending embeddings to database")

    assert len(rows) == len(embeddings), "Number of rows and embeddings must match"

    # add column of embeddings to database
    for idx, row in enumerate(rows):
        logger.debug(f"Adding embedding to row {idx + 1} of {len(rows)}")
        row.embedding = embeddings[idx]

    logger.debug("Committing changes")
    session.commit()


def embedding():
    """
    High-level embedding creation. Get embeddings from OpenAI and append them to the database.
    """
    
    session = Session()
    rows = get_rows_from_db(session)

    if len(rows) > 0:
        logger.info(f"Found {len(rows)} rows without embeddings")

        texts = [f"{row.name} {row.description}" for row in rows]
        embeddings = get_embedding_from_openai(texts)

        append_embedding_to_db(session, rows, embeddings)
    else:
        logger.warning("No rows without embeddings found")


if __name__ == "__main__":
    embedding()
