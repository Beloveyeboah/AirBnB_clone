#!/usr/bin/python3
"""Create a Class HBNBCommand"""

import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from typing import Tuple, Optional
import inspect
import shlex
import re

class_names_str = ["Amenity", "City",
                   "Place", "Review", "State",
                   "BaseModel", "User"
                   ]
all_data = storage.all()


class HBNBCommand(cmd.Cmd):
    """Command-line interface for the AIRBNB project."""

    classe = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
              "Place": Place, "State": State, "User": User, 'Review': Review}

    prompt = "(hbnb) "

    def do_quit(self, args: str) -> bool:
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, args: str) -> bool:
        """
        Handle the end-of-file event (Ctrl+D).
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def help_quit(self):
        """
        Display help message for quit command.
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Display help message for EOF command.
        """
        print("Exit the console with EOF (Ctrl+D).")

    def help_help(self):
        """
        Display help message for help command.
        """
        print("Display help information.")

    def do_create(self, args: str) -> None:
        """
        Create a new instance of a given class.
        """
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return
        class_name = arg_list[0]
        if class_name not in class_names_str:
            print("** class doesn't exist **")
            return

        # Process
        new_instance = eval(class_name)()

        new_instance.save()
        print(new_instance.id)

    def do_show(self, args: str) -> None:
        """
        Show the string representation of an instance.
        """
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return

        class_name = arg_list[0]

        if class_name not in class_names_str:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]

        # Process
        model = all_data.get(f"{class_name}.{instance_id}", None)

        if model is None:
            print("** no instance found **")
            return

        print(model)

    def do_all(self, args: Optional[str]) -> None:
        """
        Show the string representation of all instances of a given class.
        """
        arg_list = args.split()
        if arg_list and arg_list[0] not in class_names_str:
            print("** class doesn't exist **")
            return
        try:  # if only write all
            class_name = arg_list[0]
        except Exception:
            pass

        # Process
        objects = [str(obj) for obj in all_data.values()  # if only write all
                   if args == "" or str(obj).startswith(f"[{class_name}]")]

        print(objects)

    def do_destroy(self, args: str) -> None:
        """
        Delete an instance based on the class name and ID.
        """
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return

        class_name = arg_list[0]

        if class_name not in class_names_str:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]

        # Process
        try:
            all_data.pop(f"{class_name}.{instance_id}")
        except KeyError:
            print("** no instance found **")
            return

        storage.save()

    def do_update(self, args: str) -> None:
        """
        Update an instance based on the class name and ID.
        """
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return

        class_name = arg_list[0]

        if class_name not in class_names_str:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]

        instance = all_data.get(f"{class_name}.{instance_id}", None)

        if instance is None:
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        if len(arg_list) < 4:
            print("** value missing **")
            return

        is_dict = False
        for i in args:
            if i == '{':
                is_dict = True

        if is_dict:
            dicty = "".join(arg_list[2:])
            dictionary = eval(dicty)

            if (isinstance(dictionary, dict)):
                for key, value in dictionary.items():
                    setattr(instance, key, value)

                instance.save()
                return

        attribute_name = arg_list[2]
        attribute_value = eval(arg_list[3])

        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** this attribute can't be change **")
            return

        setattr(instance, attribute_name, attribute_value)

        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
