#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    
    
    __tablename__ = "states"

    if models.new_storage == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                          cascade="all, delete")
    else:
        name = ""

    if models.new_storage != "db":
        
        @property
        def cities(self):

            from models.city import City
            cities = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities