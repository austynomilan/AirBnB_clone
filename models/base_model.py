#!/usr/bin/python3
"""
module for base_model
"""
import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """ implementing BaseModel class """
    def __init__(self, *args, **kwargs):
        """ intialization of BaseModel class """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        formatted = datetime.fromisoformat(value)
                        setattr(self, key, formatted)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """ overriding __str__ method """
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates updated_at with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ dictionary containing all keys/values of __dict__ """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
