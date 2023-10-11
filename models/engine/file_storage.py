#!/usr/bin/python3

"""serializes instances to a JSON file and deserializes JSON file to instances"""
import json
import os
import datetime


class FileStorage:
    """this creates the path to the json files"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all dictionaries"""

        return self.__objects

    def new(self, obj):
        """sets key and values"""

        key = obj.__class__.name__+ "." + obj.id
        self.__objects[key] = obj

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def save(self):
        """serializes python objects into json"""

        json_objects = {}

        for key, obj in self.__objects.items():
            json_objects[key] = obj.to_dict()

            with open(self.__file_path, 'w', encoding="utf-8") as file:
                json.dump(json_objects, file)

    def reload(self):
        """loads from the save json files"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                json_objects = json.load(file)

                for key, obj_dict in json_objects.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    obj = class_obj(**obj_dict)
                    self.__objects[key] = obj
