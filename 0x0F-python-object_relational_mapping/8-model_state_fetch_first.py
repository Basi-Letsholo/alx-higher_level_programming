#!/usr/bin/python3
"""Prints the first State object from the database."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("Usage: ./8-model... username password database.")
        sys.exit(0)

    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
                          user, password, db))

    thisSession = sessionmaker(bind=engine)
    session = thisSession()

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print('Nothing')
    else:
        print('{}: {}'.format(state.id, state.name))

    session.close()
