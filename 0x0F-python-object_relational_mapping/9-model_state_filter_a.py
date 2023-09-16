#!/usr/bin/python3
"""Lists State objects with letter 'a' from database."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage: ./9-model... username password database')
        sys.exit(0)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
                           username, password, database))

    thisSession = sessionmaker(bind=engine)
    session = thisSession()

    states = session.query(State).filter(State.name.like(
             '%a%')).order_by(State.id).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()
