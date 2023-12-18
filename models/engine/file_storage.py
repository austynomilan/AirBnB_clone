#!/usr/bin/python3
"""
Module for FileStorage
"""
import json
import os


class FileStorage:
    """ implementation of class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key
            <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file
            (path: __file_path)
        """
        s_objects = {}
        for key, v in FileStorage.__objects.items():
            s_objects[key] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(s_objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects
            if file exists: otherwise do nothing
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                s = f.read()
                objects_dict = json.loads(s)
                from models.base_model import BaseModel
                from models.user import User
                for key, value in objects_dict.items():
                    cls_name = value["__class__"]
                    if cls_name == "User":
                        FileStorage.__object[key] = User(**value)
                    else:
                        FileStorage.__objects[key] = BaseModel(**value)
