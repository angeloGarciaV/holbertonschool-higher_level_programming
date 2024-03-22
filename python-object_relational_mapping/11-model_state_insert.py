#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format('root', '', 'hbtn_0e_6_usa'),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print('{0}'.format(new_state.id))
    session.close()
