#!/usr/bin/python3

"""DBStorage Class """

import os
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy import orm
from sqlalchemy.orm import sessionmaker, scoped_session



class DBStorage():
    """This class manages the storage of the data"""

    __engine = None
    __session = None

    def __init__(self):
        """inits the attr for dbstorage"""

        try:
            user = os.getenv('HBNB_MYSQL_USER')
            pwd = os.getenv('HBNB_MYSQL_PWD')
            host = os.getenv('HBNB_MYSQL_HOST')
            db = os.getenv('HBNB_MYSQL_DB')
            self.__engine = create_engine(
                f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)
        except Exception as i:
            print(f"Error during database engine initialization: {i}")

    def all(self, cls=None):
        """Returns a dictionary with all objects in the database."""
    

        try:
            all_classes = [User, State, City, Amenity, Place, Review]
        
            if cls is None:
                objects = []
                for cls in all_classes:
                    objects += self.__session.query(cls).all()
            else:
                objects = self.__session.query(cls).all()

            obj_dict = {}
            for obj in objects:
                obj_dict[f'{obj.__class__.__name__}.{obj.id}'] = obj

            return obj_dict
        except Exception as a:
            print(f"Error during database query: {a}")
            return {}

    def new(self, obj):
        """adds objects to the current database session"""
        if self.__session is not None:
            self.__session.add(obj)
        else:
            print("Error, no data session.")
            return

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads database and create new session"""


        try:        
            Base.metadata.create_all(self.__engine)

            factory = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
            Session = scoped_session(factory)
            self.__session = Session()
        except Exception as r:
            print(f"Error during database reload: {r}")
