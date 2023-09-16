#!/usr/bin/python3
""" Lists all Statte objects from database."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage: ./7-model_state_fetch_all.py username password db')
        sys.exit(0)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
                           username, password, database))

    thisSession = sessionmaker(bind=engine)
    session = thisSession()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()
