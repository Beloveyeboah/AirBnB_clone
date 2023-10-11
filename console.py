#!/usr/bin/python3

"""this module defines the point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """this class creates the base console"""

    prompt = "(hbnb)"

    def do_create(self, args):
        """creates an instance of BaseModel"""

        if args == "" or args is None:
            print("** class name missing **")
            return

        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)

        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an
        instance based on the class name"""

        if not args:
            print("** class name missing **")
            return
        args_list = args.split()

        try:
            class_name = args_list[0]
        except IndexError:
            print("** class name missing **")
            return

        try:
            obj_id = args_list[1]
        except IndexError:
            print("** instance id missing **")
            return

        obj_dict = storage.all()

        key = class_name + '.' + obj_id

        if key not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""

        if args == "" or args is None:
            print("** class name missing **")
            return
        else:
            args_list = args.split(' ')
            if args_list[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args_list[0], args_list[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, args):
        """Prints all string representation of all 
        instances based or not on the class name"""


        if args is not None:
            args_list = args.split()
            if args_list[0] not in storage.classes:
                print("** class doesn't exist **")
                return
            objs = models.storage.get_all(args_list)
        else:
            objs = models.storage.all()
        print([str(obj) for obj in objs.values()])


    def do_update(self, args):
        """Updates an instance based on the class name and id"""

        if args == "" or args is None:
            print("** class name missing **")
            return





    def quit(self):
        """ths exits the console of airbnb"""

        return True


    def EOF(self):
        """exits with crtl + d"""

        print()
        return True

    def emptyline(self):
        """handles empty lines received on the console"""

        pass














if __name__ == '__main__':
    HBNBCommand().cmdloop()
