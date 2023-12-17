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
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)() 
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """print the string reps of an instance"""
        args = arg.split()
        if not args:
            print("** class name is missing **")
            return
        
        class_name = args[0]
        classes = [key.split('.')[0] for key in storage.all().keys()]
        
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id is missing**")
            return
        try:
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"         
            instance = storage.all().get(key)

            if instance:
                print(instance)
            else:
                print("** No instance found **")
        except Exception as e:
            print(f"An error occured: {e}")
        
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        classes = [key.split('.')[0] for key in storage.all().keys()]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
           print("** instance id missing **")
           return
           
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instances = storage.all()

        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        classes = [key.split('.')[0] for key in storage.all().keys()]

        if not arg:
            print([str(instance) for instance in storage.all().values()])
        elif arg in classes:
            print([str(instance) for key, instance in storage.all().items() if key.startswith(f"{arg}.")])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        
        classes = [key.split('.')[0] for key in storage.all().keys()]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instances = storage.all()
        instance = instances.get(key)

        if not instance:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
    
        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        try:
            casted_value = str(attribute_value)
            setattr(instance, attribute_name, casted_value)
            instance.save()
            print(f"Attribute {attribute_name} of {class_name} instance {instance_id} updated to {casted_value}.")
        except ValueError:
            print("** invalid attribute value **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
