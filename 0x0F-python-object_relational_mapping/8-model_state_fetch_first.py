#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_first_get.py\
<username> <password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]

        engine = create_engine(f'mysql+mysqldb://{username}:{password}\
@localhost:3306/{database_name}')

        Session = sessionmaker(bind=engine)

        session = Session()

        first_state = session.query(State).order_by(State.id).first()

        if first_state is None:
            print("Nothing")
        else:
            print(f"{first_state.id}: {first_state.name}")

        session.close()
