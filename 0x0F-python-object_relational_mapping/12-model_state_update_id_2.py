#!/usr/bin/python3
"""script that changes the name of a State"""

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

    row = session.query(State).filter(State.id == 2).first()
    row.name = 'New Mexico'
    session.commit()
