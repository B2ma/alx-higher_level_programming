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
    if len(sys.argv) != 4:
        print("Usage: ./10-model_state_my_get.py <username> <password>\
<database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        engine = create_engine(f'mysql+mysqldb://{username}:{password}\
@localhost:3306/{database_name}')
        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()

        print(new_state.id)

        session.close()
