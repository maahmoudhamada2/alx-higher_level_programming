#!/usr/bin/python3
"""script that lists all State objects that contain the letter a"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    path = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(argv[1], argv[2], argv[3])
    engine = create_engine(path)

    Session = sessionmaker(bind=engine)
    session = Session()

    records = session.query(State.id, State.name).order_by(State.id).all()
    for id, name in records:
        if 'a' in name:
            print("{}: {}".format(id, name))
