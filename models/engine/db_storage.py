#!/usr/bin/python3

"""DBStorage Class """

from models.base_model import BaseModel, Base

HBNB_MYSQL_USER = "hbnb_dev"
HBNB_MYSQL_PWD = "hbnb_dev_pwd"
HBNB_MYSQL_HOST = "localhost"
HBNB_MYSQL_DB = "hbnb_dev_db"


class DBStorage():
    """This class manages the storage of the data"""

    __engine = None
    __sesion = None

    def __init__(self):
        """inits the attr for dbstorage"""
