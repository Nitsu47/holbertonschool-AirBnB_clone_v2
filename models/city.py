#!/usr/bin/python3
""" City Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models

class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    @property
    def places(self):
        """Getter for places"""
        if models.storage.__class__.__name__ == "DBStorage":
            from models.place import Place
            places_list = []
            for place in models.storage.all(Place).values():
                if place.city_id == self.id:
                    places_list.append(place)
            return places_list
        return []
