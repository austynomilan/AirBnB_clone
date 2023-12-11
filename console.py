#!/usr/bin/python3
"""
HBNBCommand console module
"""
import sys
import cmd
import re
from models import *


class HBNBCommand(cmd.Cmd):
    """ implementation of HBNBCommand class """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def emptyline(self):
        """ when an empty line is entered """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
