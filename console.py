#!/usr/bin/python3
import cmd

'''the Console which handles the main program'''

class HBNBCommand(cmd.Cmd):
    '''the command line interpreter'''
    prompt = 'Airbnb cmd: '
    intro = "Simple command processor example."


if __name__ == '__main__':
    HBNBCommand().cmdloop()
