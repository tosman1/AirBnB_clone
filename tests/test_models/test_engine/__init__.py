#!/usr/bin/python3
"""
__init__ magic method for models directory
to create a unique FileStorage instance for this application
to store and reload
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
