#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """Returns a list of City objects linked to state from storage"""
        return self.cities
