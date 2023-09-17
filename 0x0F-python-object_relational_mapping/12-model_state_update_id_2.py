#!/usr/bin/python3
"""Updates the name of a State object in the databse."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage: ./12-model... username password database.')
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
                            username, password, database))

    thisSession = sessionmaker(bind=engine)
    session = thisSession()

    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()
    else:
        print('State with id = 2 not found')

    session.close()
