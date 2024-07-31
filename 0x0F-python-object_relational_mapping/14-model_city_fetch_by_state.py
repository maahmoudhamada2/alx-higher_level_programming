#!/usr/bin/python3
"""Script that prints all City"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker, aliased

if __name__ == '__main__':
    path = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(argv[1], argv[2], argv[3])
    engine = create_engine(path)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.name, City.id, City.name).join(State).all()
    for st_name, ct_id, ct_name in query:
        print("{}: ({}) {}".format(st_name, ct_id, ct_name))
