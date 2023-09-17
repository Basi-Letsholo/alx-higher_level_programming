#!/usr/bin/python3
"""Prints all cities objects from database."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City
import sys

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage: ./14-model... username password database.')
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
                            username, password, database))

    thisSession = sessionmaker(bind=engine)
    session = thisSession()

    cities = session.query(City, State).filter(
             City.state_id == State.id).order_by(City.id).all()

    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
