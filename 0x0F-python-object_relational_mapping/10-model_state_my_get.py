#!/usr/bin/python3
"""
Print the State object with the name passed as an argument
from the database `hbtn_0e_6_usa`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        search_name = sys.argv[4]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(State.name == search_name).first()

        if state is None:
            print("Not found")
        else:
            print(state.id)

        session.close()
    else:
        print("Usage: ./10-model_state_my_get.py \
                <username> <password> <database> <state_name>")
