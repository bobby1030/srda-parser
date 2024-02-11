import os
from functools import lru_cache

from flask import Flask, jsonify
from flask import request as req
from sqlalchemy import select, or_
from sqlalchemy.orm import joinedload, contains_eager
import openai

from ..db.models import Codebook, Variable
from ..db.database import ScopedSession

api = Flask(__name__)


@api.get("/api/codebooks/")
def get_codebooks():
    with ScopedSession() as session:
        query = select(Codebook)
        codebooks = session.scalars(query).all()

        return codebooks


@api.get("/api/variables/")
@api.get("/api/variables/search/") # fallback for empty search term
def get_variables():
    offset = req.args.get("offset", 0)
    limit = req.args.get("limit", 10)

    with ScopedSession() as session:
        query = select(Variable).limit(limit).offset(offset)
        variables = session.scalars(query).all()

        return jsonify(variables)


@api.get("/api/variables/<int:variableid>")
def get_variable(variableid):
    with ScopedSession() as session:
        query = select(Variable).where(Variable.id == variableid)
        variable = session.scalars(query).one()

        return jsonify(variable)

@lru_cache
def get_openai_embedding(search_term):
    client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.embeddings.create(input=search_term, model="text-embedding-3-small")
    return response.data[0].embedding

@api.get("/api/variables/search/<search_term>")
def search_variable(search_term):
    limit = req.args.get("limit", 10)
    offset = req.args.get("offset", 0)

    with ScopedSession() as session:
        query = (
            select(Variable)
            .order_by(Variable.embedding.l2_distance(get_openai_embedding(search_term)), Variable.id)
            .limit(limit)
            .offset(offset)
        )
        variables = session.scalars(query).all()

        return jsonify(variables)


@api.get("/api/variables/similar/<variableid>")
def similar_variable(variableid):
    limit = req.args.get("limit", 10)
    offset = req.args.get("offset", 0)

    with ScopedSession() as session:
        query = select(Variable).where(Variable.id == variableid)
        variable = session.scalars(query).one()

        vec = variable.embedding

        query_similar = (
            select(Variable)
            .order_by(Variable.embedding.l2_distance(vec))
            .limit(limit)
            .offset(offset)
        )

        similar_variables = session.scalars(query_similar).all()

        return jsonify(similar_variables)


if __name__ == "__main__":
    api.run(debug=True)
