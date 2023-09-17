#!/usr/bin/python3
"""Lists all State objects, and corresponding City objects."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
import sys

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage: ./100-rel... username password database.')
        sys.exit(1)

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
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))

    session.close()
