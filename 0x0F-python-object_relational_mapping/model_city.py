#!/usr/bin/python3
"""Class definition of a state and an instance
Base = declarative_base()"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    A class containing link to MySQL table 'cities'
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
