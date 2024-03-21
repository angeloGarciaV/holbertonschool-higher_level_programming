#!/usr/bin/python3
"""File that contains the class definition of a State"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Class State that inherits from Base """
    __tablename__ = "state"
    id = Column("id", Integer, primary_key=True,
                autoincrement=True)
    name = Column("name", String(128), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)
