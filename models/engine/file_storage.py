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
        for key, obj in self.__objects.items():
           s_objects[key] = obj.to_dictionary()

        with open(self.__file_path, 'w') as f:
            json.dump(s_objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects 
            if file exists: otherwise do nothing
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                s = f.read()
                try:
                    loaded_objects = json.loads(s)
                    self.__objects = {}
                    for key, value in loaded_objects.items():
                        class_obj = globals()[class_name]
                        obj = class_obj(**value)
                        self.__objects[key] = obj
                except FileNotFoundError:
                    pass

