#!/usr/bin/python3
"""Lists all State objects  contain the letter a from the database"""

import sqlalchemy
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for letter in session.query(State).filter(State.name.like('%a%')) \
            .order_by(State.id):
        print("{}: {}".format(letter.id, letter.name))
    session.close()
