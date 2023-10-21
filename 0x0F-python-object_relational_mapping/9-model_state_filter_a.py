#!/usr/bin/python3
"""
Lists all State objects that contain the letter
'a' from the database hbtn_0e_6_usa.
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <username>\
<password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        engine = create_engine(f'mysql+mysqldb://{username}:{password}\
@localhost:3306/{database_name}')
        Session = sessionmaker(bind=engine)
        session = Session()
        states_with_a = session.query(State).filter(
                State.name.like('%a%')).order_by(State.id).all()
        for state in states_with_a:
            print(f"{state.id}: {state.name}")
        session.close()
