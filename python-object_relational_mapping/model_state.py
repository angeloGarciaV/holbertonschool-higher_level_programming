#!/usr/bin/python3
"""file that contains the class definition of a State"""

from sys import argv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    Class State that inherits from Base

    Args:
        Base (class): declarative_base
    """
    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True,
                autoincrement=True)
    name = Column("name", String(128), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
