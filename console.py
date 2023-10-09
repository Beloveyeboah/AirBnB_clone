#!/usr/bin/python3

"""this module defines the point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """this class creates the base console"""

    def quit(self):
        """ths exits the console of airbnb"""



    def EOF(self):
        """exits with crtl + d""""














if __name__ == '__main__':
    HBNBCommand().cmdloop()
