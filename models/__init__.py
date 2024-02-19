#!/usr/bin/python3
""" This model creates a unique file storage instance for our application
"""
from os import getenv

storageType = getenv("HBNB_TYPE_STORAGE")
if storageType == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    try:
        from models.engine.file_storage import FileStorage
        print('Active')
    except ImportError:
        print('Inactive')
    storage = FileStorage()
storage.reload()