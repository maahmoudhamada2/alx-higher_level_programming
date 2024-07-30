#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter a"""

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

    records = session.query(State).all()
    for row in records:
        if 'a' in row.name:
            session.delete(row)
    session.commit()
