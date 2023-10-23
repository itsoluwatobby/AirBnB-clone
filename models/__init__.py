#!/usr/bin/python3
"""
Initializing an instance of the File_storage class
Then reloads the stored instance
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
