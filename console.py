#!/usr/bin/python3
"""
HBNBCommand console module
"""

import json
from models import storage
import cmd
import re
from models.base_model import BaseModel
'''from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place'''



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
    
    def do_create(self, arg):
        """Creatd a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = getattr(__import__("__main__"), arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """print the string reps of an instance"""
        args = arg.split()
        if not args:
            print("** class name is missing **")
        else:
            try:
                class_name = args[0]
                instance_id = args[1]
                key = f"{class_name}.{instance_id}"
                
                instance = storage.all().get(key)

                if instance:
                    print(instance)
                else:
                    print("* No instance found *")

            except IndexError:
                print("* Instance id missing *")

            except NameError:
                print("* class doesnt exist *")

    def do_destroy(sef, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name is missing **")
        else:
            try:
                class_name: args[0]
                instance_id = args[1]
                key = f"{class_name}.{instance_id}"

                instances = storage.all()
                instance = instance.get(key)

                if instance:
                    del instance[key]
                    storage.save()
                else:
                    print("no instance found!")
            except IndexError:
                print("* instance id missing *")
            except NameError:
                print("* class doesn't exist *")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        classes = [cls.__name__ for cls in storage.classes.values()]

        if not arg:
            print([str(instance) for instance in storage.all().values()])
        elif arg in classes:
            print([str(instance) for instance in storage.all(arg).values()])
        else:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
