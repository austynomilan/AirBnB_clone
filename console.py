#!/usr/bin/python3
import cmd
import sys

'''the Console which handles the main program'''

class HBNBCommand(cmd.Cmd):
    '''the command line interpreter'''
    prompt = 'Airbnb cmd: '
    intro = "command processor for the Airbnb Enjoy...."

    def do_exit(self, line):
        '''Exit the program'''
        print('Exited!')
        sys.exit()

    def do_quit(self, line):
        '''Exit the program'''
        self.do_exit(line)

    def do_EOF(self, line):
        '''Exit the program'''
        print('Exited!')
        sys.exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
