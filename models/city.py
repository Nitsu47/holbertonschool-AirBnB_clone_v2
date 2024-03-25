#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    name = Column(str(128), nullable=False)

    state_id = Column(str(60), nullable=False, foreignkey='states.id')
