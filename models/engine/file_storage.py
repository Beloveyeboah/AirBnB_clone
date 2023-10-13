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

        obj_dict = {}

        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

            with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
                json.dump(obj_dict, file)

    def reload(self):
        """loads from the save json files"""

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
