#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
"""
from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    location = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id,).all()

    for state, city in location:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
