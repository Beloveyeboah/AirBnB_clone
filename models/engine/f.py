#!/usr/bin/python3

"""serializes instances to a JSON file and
deserializes JSON file to instances"""

import json
import os
import datetime


class FileStorage:
    """this creates the path to the json files"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all dictionaries"""

        return FileStorage.__objects

    def new(self, obj):
        """sets key and values"""

        key = obj.__class__.name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes python objects into json"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, file)

    def reload(self):
        """loads from the save json files"""

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes

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
