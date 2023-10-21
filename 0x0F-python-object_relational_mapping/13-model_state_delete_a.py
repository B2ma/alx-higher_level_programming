#!/usr/bin/python3
"""
Deletes all State objects with a name containing the
letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <username>\
<password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        engine = create_engine(f'mysql+mysqldb://{username}:{password}\
@localhost:3306/{database_name}')
        Session = sessionmaker(bind=engine)
        session = Session()

        states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()
        for state in states_to_delete:
            session.delete(state)
        session.commit()

        session.close()
