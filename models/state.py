#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)

        cities = relationship("City", backref="state",
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

    @property
    def cities(self):
        """Returns a list of City objects linked to state from storage"""
        city_list = []
        from models import storage
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
