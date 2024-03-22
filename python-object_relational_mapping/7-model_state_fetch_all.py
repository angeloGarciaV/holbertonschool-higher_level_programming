#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id).all()
    for state in results:
        print(f'{state.id}: {state.name}')
    session.close()
