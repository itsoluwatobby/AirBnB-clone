#!/usr/bin/python3
"""
This defines a BaseModel class Model for the AirBnB_clone project
"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """
    This is a base class of all the other classes in this project
    """

    def __init__(self, *args, **kwargs):
        """
        initializes an instance of the baseModel class

        Args:
            *args(any): Unused parameter.
            **kwargs(dict): Key/value pairs of attributes.
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        updates the instance undated_at attribute with current time
        and saves an instance
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """
        Returns string representation of the object
        """
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def to_dict(self):
        """
        Returns a dictionary containing a representation of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
