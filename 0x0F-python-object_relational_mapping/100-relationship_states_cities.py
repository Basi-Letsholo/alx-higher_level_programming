#!/usr/bin/python3
"""Creates a new state with a city in the database."""


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

    Base.metadata.create_all(engine)

    thisSession = sessionmaker(bind=engine)
    session = thisSession()

    new_state = State(name='California')
    session.add(new_state)
    session.commit()

    new_state_id = session.query(State.id).filter(
                   State.name == 'California').first()
    new_city = City(name='San Francisco', state_id=new_state_id[0])
    session.add(new_city)
    session.commit()

    session.close()
