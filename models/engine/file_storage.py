#!/usr/bin/python3
"""
Defines a File storage class that serializes instances to JSON file and
    "deserializes JSON file to instances
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Represents an instance of the FileStorage class

    Attributes:
        __file_path: A path to the JSON file
        __objects: A dict to store all objects
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns a dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Args:
            obj: object to set to __object
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as new_file:
            new_file.write(json.dumps(new_dict))

    def reload(self):
        """
        deserializes the JSON file to __objects (
        only if the JSON file (__file_path) exists);

        Raises:
            an exception If the file doesn’t exist
        """
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }
        try:
            with open(FileStorage.__file_path, "r") as loaded_f:
                fetched_dicts = json.load(loaded_f)
                for key, obj in fetched_dicts.items():
                    self.all()[key] = classes[obj['__class__']](**obj)
        except FileNotFoundError:
            return
