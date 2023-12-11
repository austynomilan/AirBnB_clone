#!/usr/bin/python3

import sys
import cmd
import re
from models import *

""" the Console which handles the main program """


class HBNBCommand(cmd.Cmd):
    """ the command line interpreter """
    prompt = '(hbnb)  '

    def do_exit(self, line):
        """ Exit the program """
        sys.exit()

    def do_quit(self, line):
        """ Quit command to exit the program """
        self.do_exit(line)

    def do_EOF(self, line):
        """ Exit the program """
        sys.exit()

    def emptyline(self):
        """ when an empty line is entered """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
