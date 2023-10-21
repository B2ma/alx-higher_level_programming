#!/usr/bin/python3
"""
Prints the State object with the name passed as
argument from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <username> <password>\
<database_name> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]
        engine = create_engine(f'mysql+mysqldb://{username}:{password}\
@localhost:3306/{database_name}')
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter(State.name == state_name).first()
        if state is None:
            print("Not found")
        else:
            print(state.id)

        session.close()
