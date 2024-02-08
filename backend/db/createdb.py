import os, json, pathlib

from sqlalchemy import (
    create_engine,
    URL,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    text,
)

from sqlalchemy_utils import database_exists, create_database

# Directories with json files ready to load into the database
INPUT_DIR = ["resources/mu_codebook/out/"]


def read_json_codebook(dir):
    input_files = pathlib.Path(dir).rglob("*.json")

    def read(filepath):
        with open(filepath, "r") as f:
            codebook = json.load(f)

            return codebook

    return [read(file) for file in input_files]


def get_db_engine():
    db_url = URL.create(
        "postgresql+psycopg2",
        host=os.environ["POSTGRES_HOST"],
        port=os.environ["POSTGRES_PORT"],
        username=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        database=os.environ["POSTGRES_DB"],
    )

    if not database_exists(db_url):
        create_database(db_url)

    return create_engine(db_url)

def createdb():
    # load codebook and variables into database
    with get_db_engine().connect() as conn:
        metadata = MetaData()

        codebook_table = Table(
            "codebook",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("title", String),
            Column("date", Integer),
            Column("description", String),
        )

        variables_table = Table(
            "variables",
            metadata,
            Column("id", Integer, primary_key=True, autoincrement=True),
            Column("codebook_id", Integer, ForeignKey("codebook.id")),
            Column("description", String),
            Column("field", String),
            Column("name", String),
            Column("note", String),
            Column("q_id", String),
            Column("values", String),
        )

        metadata.drop_all(conn)
        metadata.create_all(conn)

        # loop through codebooks and insert into database
        codebooks = read_json_codebook(INPUT_DIR[0])

        for idx, codebook in enumerate(codebooks):
            codebook_id = idx + 1

            conn.execute(
                codebook_table.insert().values(
                    id=codebook_id,
                    title=codebook["title"],
                    date=codebook["date"],
                    description=codebook["description"],
                )
            )

            for variable in codebook["variables"]:
                conn.execute(
                    variables_table.insert().values(
                        codebook_id=codebook_id,
                        description=variable["description"],
                        field=variable["field"],
                        name=variable["name"],
                        note=variable["note"],
                        q_id=variable["q_id"],
                        values=variable["values"],
                    )
                )

        # commit changes
        conn.commit()

if __name__ == "__main__":
    createdb()