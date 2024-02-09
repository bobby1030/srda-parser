import json, pathlib

from sqlalchemy import text
from .database import engine, Session
from .models import Base, Codebook, Variable

from .. import logger

# Directories with json files ready to load into the database
INPUT_DIR = ["resources/mu_codebook/out/"]


def read_json_codebook(dir):
    input_files = pathlib.Path(dir).rglob("*.json")

    def read(filepath):
        with open(filepath, "r") as f:
            codebook = json.load(f)

            return codebook

    return [read(file) for file in input_files]


def createdb():
    logger.info("Building database schema and loading data...")

    # enable vector extension
    with Session() as session:
        session.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        session.commit()

    # build schema
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # load codebook and variables into database
    with Session() as session:
        json_codebooks = read_json_codebook(INPUT_DIR[0])

        for idx, codebook in enumerate(json_codebooks):
            codebook_id = idx + 1
            codebook_row = Codebook(
                id=codebook_id,
                title=codebook["title"],
                date=codebook["date"],
                description=codebook["description"],
            )
            session.add(codebook_row)

            for variable in codebook["variables"]:
                variable_row = Variable(
                    codebook_id=codebook_id,
                    description=variable["description"],
                    field=variable["field"],
                    name=variable["name"],
                    note=variable["note"],
                    q_id=variable["q_id"],
                    values=variable["values"],
                )
                session.add(variable_row)

        # commit changes
        session.commit()
