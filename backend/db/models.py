from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from pgvector.sqlalchemy import Vector


class Base(DeclarativeBase):
    pass


class Codebook(Base):
    __tablename__ = "codebook"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    date: Mapped[int]
    description: Mapped[Optional[str]]


class Variable(Base):
    __tablename__ = "variable"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    codebook_id: Mapped[int] = mapped_column(ForeignKey(Codebook.id))
    codebook: Mapped[Codebook] = relationship(Codebook, backref="variables")
    description: Mapped[Optional[str]]
    field: Mapped[Optional[str]]
    name: Mapped[str]
    note: Mapped[Optional[str]]
    q_id: Mapped[Optional[str]]
    values: Mapped[Optional[str]]
    embedding = mapped_column(Vector[1536], nullable=True)
