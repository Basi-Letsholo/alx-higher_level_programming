#!/usr/bin/python3
"""Prints the State object with the name passed as argument."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys

if __name__ == '__main__':

    if len(sys.argv) != 5:
        print('Usage: ./10-model... username password database state.')
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_search = sys.argv[4]

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
                           username, password, database))

    thisSession = sessionmaker(bind=engine)
    session = thisSession()

    state = session.query(State).filter(State.name == state_search).first()
    if state is None:
        print('Not found')
    else:
        print(state.id)

    session.close()
