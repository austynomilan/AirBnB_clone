#!/usr/bin/python3
"""
module for base_model
"""
import uuid
from datetime import datetime


class BaseModel:
    """ implementing BaseModel class """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at":
                    formatted = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, formatted)
                if key == "updated_at":
                    formatted = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, formatted)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ overriding __str__ method """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ updates updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ dictionary containing all keys/values of __dict__ """
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        
        return_dict = {
                "__class__": self.__class__.__name__,
                "updated_at": self.updated_at,
                "create_at": self.created_at
                }

        for key, value in self.__dict__.items():
            return_dict[key] = value

        return return_dict
