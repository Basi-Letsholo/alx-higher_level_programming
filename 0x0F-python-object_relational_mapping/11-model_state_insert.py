#!/usr/bin/python3
"""Adds new State object to the database."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage: ./11-model... username password databse.')
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
                            username, password, database))

    thisSession = sessionmaker(bind=engine)
    session = thisSession()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    state = session.query(State).filter(State.name == 'Louisiana').first()
    print(state.id)

    session.close()
