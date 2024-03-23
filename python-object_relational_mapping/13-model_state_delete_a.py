#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        or_(State.name.like('%a%'), State.name.like('A%'))).all()
    for state in states:
        session.delete(state)
    session.commit()

    states = session.query(State).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
