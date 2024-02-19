#!/usr/bin/python3
"""Class definition of a state and an instance
Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A class containing link to MySQL table 'states'
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
