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
            print("** class name is missing **")
        else:
            try:
                class_name = args[0]
                instance_id = args[1]
                
                storage.delete_by_id(class_name, instance_id)

            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        classes = [cls.__name__ for cls in storage.classes.values()]

        if not arg:
            print([str(instance) for instance in storage.all().values()])
        elif arg in classes:
            print([str(instance) for instance in storage.all(arg).values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                instance_id = args[1]
                attribute_name = args[2]
                attribute_value = args[3]

                key = f"{class_name}.{instance_id}"
                instances = storge.all()
                instance = instances.get(key)

                if not instance:
                    print("** no instance found **")
                    return

                if hasattr(instance, attribute_name) and \
			attribute_name not in ["id", "created_at", "updated_at"]:
                    attribute_type = type(getattr(instance, attribute_name))
                    setattr(instance, attribute_name, attribute_type(attribute_value))
                    instance.save()
                else:
                    print("** attribute name missing **")
            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")
            except ValueError:
                print("** value missing **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
