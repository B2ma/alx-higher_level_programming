#!/usr/bin/python3
"""
   State Class module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Represents a state in the states table of the database.
    Attributes:
        id (int): Auto-generated unique identifier for the state (primary key).
        name (str): Name of the state, maximum 128 characters.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
