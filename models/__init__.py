#!/usr/bin/python3
"""module to switch storage depending on situation"""
import os


new_storage = os.getenv('HBNB_TYPE_STORAGE')

if new_storage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
    Base = {}