#!/usr/bin/python3
"""
Contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """
    Class definition of a City.
    Inherits from Base.
    Links to the MySQL table cities.
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(
                'states.id'), nullable=False)
