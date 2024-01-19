#!/usr/bin/python3
"""  FileStorage that serializes instances to a JSON file and deserializes JSON
file to instances:"""

import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the direction object"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        json_obj = {}
        for k in self.__objects:
            json_obj[k] = self.__objects[k].to_dict()

        with open(FileStorage.__file_path, 'w')as f:
            json.dump(json_obj, f)

    def reload(self):
         """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                # jlo = json.load(f)
                for key, value in json.load(f).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass
