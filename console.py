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

        elif args not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes()[args]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an
        instance based on the class name"""

        if not args:
            print("** class name missing **")
            return
        else:
            args_list = line.split(' ')
            if args_lis[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args_list[0], args_lis[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])


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
            else:
                var = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(var)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""

        if args == "" or args is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, args)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

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

    def do_count(self, args):
        """Counts the total instances of a class.
        """
        args = line.split(' ')
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    args[0] + '.')]
            print(len(matches))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
