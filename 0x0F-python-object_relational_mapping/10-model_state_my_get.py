#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

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

    row = session.query(State.id).filter_by(name=argv[4]).first()
    if row is None:
        print("Not found")
    else:
        print("{}".format(row.id))
