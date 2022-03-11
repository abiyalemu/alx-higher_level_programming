#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

import sqlalchemy
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for consul in session.query(State).order_by(State.id):
        print("{}: {}".format(consul.id, consul.name))
    session.close()
