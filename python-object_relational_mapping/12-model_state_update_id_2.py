#!/usr/bin/python3
"""
changes the name of a State object from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.id == 2).\
        update({State.name: 'New Mexico'}, synchronize_session=False)
    session.commit()

    states = session.query(State).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
