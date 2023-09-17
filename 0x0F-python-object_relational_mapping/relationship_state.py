#!/usr/bin/python3
"""Defines class of a state."""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ State class which inherits from Base.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')
