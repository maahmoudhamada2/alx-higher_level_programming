#!/usr/bin/python3
"""Script that adds the State object “Louisiana”"""
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

    s1 = State(name='Louisiana')
    session.add(s1)
    session.commit()
    print("{}".format(s1.id))
