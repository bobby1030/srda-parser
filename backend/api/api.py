from flask import Flask, make_response, request
from sqlalchemy import select, or_
from sqlalchemy.orm import joinedload

from ..db.models import Codebook, Variable
from ..db.database import ScopedSession

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.get("/api/codebooks")
def get_codebooks():
    session = ScopedSession()
    query = select(Codebook)
    codebooks = session.scalars(query).all()

    result = [codebook.__dict__ for codebook in codebooks]
    res = make_response(result)
    res.mimetype = "text/plain"

    return res


@app.get("/api/variables")
def get_variables():
    session = ScopedSession()
    query = select(Variable)
    variables = session.scalars(query).all()

    result = [f"{variable.name} {variable.description}" for variable in variables]
    res = "\n".join(result)

    return res


@app.get("/api/variables/search/<search_term>")
def search_variable(search_term):
    session = ScopedSession()
    query = (
        select(Variable)
        .where(
            or_(
                Variable.name.ilike(f"%{search_term}%"),
                Variable.description.ilike(f"%{search_term}%"),
            )
        )
        .options(joinedload(Variable.codebook))
    )
    variables = session.scalars(query).all()

    result = [
        {
            "id": variable.id,
            "codebook": variable.codebook.title,
            "date": variable.codebook.date,
            "name": variable.name,
            "description": variable.description,
        }
        for variable in variables
    ]

    return result


@app.get("/api/variables/similar/<variableid>")
def similar_variable(variableid):
    session = ScopedSession()
    query = select(Variable).where(Variable.id == variableid)
    variable = session.scalars(query).one()

    vec = variable.embedding

    limit = request.args.get("limit", 10)
    query_similar = (
        select(Variable)
        .options(joinedload(Variable.codebook))
        .order_by(Variable.embedding.l2_distance(vec))
        .limit(limit)
    )

    similar_variables = session.scalars(query_similar).all()

    result = [
        {
            "id": variable.id,
            "codebook": variable.codebook.title,
            "date": variable.codebook.date,
            "name": variable.name,
            "description": variable.description,
        }
        for variable in similar_variables
    ]

    return result


if __name__ == "__main__":
    app.run()
