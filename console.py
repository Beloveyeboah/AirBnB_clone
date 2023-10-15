#!/usr/bin/python3
"""Defines a Class HBNBCommand"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Defines all atrributes and method
    the class HBNBCommand"""

    prompt = '(hbnb) '
    allowed_classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_quit(self, arg):
        """Exits the Console by typing 'quit'"""
        return True

    def do_EOF(self, arg):
        """Exits the Console by typing 'ctr + d'"""
        return True

    def emptyline(self):
        """Does nothing when empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and prints the id"""

        splarg = arg.split()
        if len(splarg) == 0:
            print("** class name missing **")
        elif splarg[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.allowed_classes[splarg[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints a string represention of class and id"""

        splarg = arg.split()
        if len(splarg) == 0:
            print("** class name missing **")
        elif splarg[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif len(splarg) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(splarg[0], splarg[1])
            if key in storage.all().keys():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes a specified instance of an Object"""

        splarg = arg.split()
        if len(splarg) == 0:
            print("** class name missing **")
        elif splarg[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif len(splarg) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(splarg[0], splarg[1])
            if key in storage.all().keys():
                instances = storage.all()
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints a list of all instances of all classes, or all
            instances of a specified class"""

        splarg = arg.split()
        inst_list = []
        if len(splarg) == 0:
            for instance in storage.all().values():
                inst_list.append(str(instance))
            print(inst_list)
        elif splarg[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if key.split('.')[0] == splarg[0]:
                    inst_list.append(str(value))
            print(inst_list)

    def do_update(self, arg):
        """ Updates the specified attribute of a class, only one
        attribute can be updated at a time"""

        splarg = arg.split()
        if len(splarg) == 0:
            print("** class name missing **")
        elif len(splarg) < 2:
            print("** instance id missing **")
        elif len(splarg) < 3:
            print("** attribute name missing **")
        elif len(splarg) < 4:
            print("** value missing **")
        elif splarg[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            key = "{}.{}".format(splarg[0], splarg[1])
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
            else:
                if splarg[3].isdigit():
                    splarg[3] = int(splarg[3])
                elif splarg[3].replace('.', '', 1).isdigit():
                    splarg[3] = float(splarg[3])
                instance = instances[key]
                setattr(instance, splarg[2], splarg[3])
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
