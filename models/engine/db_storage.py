#!/usr/bin/python3

"""DBStorage Class """

from models.base_model import BaseModel, Base
import os
from sqlalchemy import create_engine
from sqlalchemy import orm
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.user import User

HBNB_MYSQL_USER = "hbnb_dev"
HBNB_MYSQL_PWD = "hbnb_dev_pwd"
HBNB_MYSQL_HOST = "localhost"
HBNB_MYSQL_DB = "hbnb_dev_db"


class DBStorage():
    """This class manages the storage of the data"""

    __engine = None
    __session = None

    def __init__(self):
        """inits the attr for dbstorage"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

    def all(self, cls=None):
        """Returns a dictionary with all objects in the database."""
        classes = {'State': State, 'City': City, 'User': User, 'Place': Place,
                   'Review': Review, 'Amenity': Amenity}
        obj_dic = {}
        if cls is None:
            for cls_name, cls_type in classes.items():
                data = self.__session.query(cls_type).all()
                for inst in data:
                    key = '{}.{}'.format(cls_name, inst.id)
                    obj_dic[key] = inst
        else:
            for inst in self.__session.query(cls).all():
                key = '{}.{}'.format(cls.__name__, inst.id)
                obj_dic[key] = inst
        return obj_dic

    def new(self, obj):
        """adds objects to the current database session"""
        self.__session.add(obj)
        self.save()

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads database and create new session"""
        Base.metadata.create_all(self.__engine)

        factory = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        """Close class session"""
        self.__session.close()
