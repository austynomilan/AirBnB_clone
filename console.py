#!/usr/bin/python3
"""
HBNBCommand console module
"""

import json
from models import storage
import cmd
import re
import shlex
from ast import literal_eval
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


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

    def parse_arg(self, arg):
        '''Parse argument string using shlex to handle double quotes.'''
        try:
            return shlex.split(arg)
        except ValueError as e:
            print(f"Argument parsing error: {e}")
            return []

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = self.parse_arg(arg)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """print the string reps of an instance"""
        args = self.parse_arg(arg)
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
        try:
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            instance = storage.all().get(key)

            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except Exception as e:
            print(f"An error occured: {e}")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = self.parse_arg(arg)
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
        try:
            args = shlex.split(arg)
        except ValueError as e:
            print(f"Argument parsing error: {e}")

        if not args:
            print([str(instance) for instance in storage.all().values()])
        elif len(args) == 1:
            class_name = args[0]
            classes = [key.split('.')[0] for key in storage.all().keys()]
            if class_name in classes:
                print([str(instance)
                       for key, instance in storage.all().items()
                       if key.startswith(f"{class_name}.")
                       ])
            else:
                print("** class doesn't exist **")
        else:
            print("** too many argument **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = self.parse_arg(arg)

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

        if len(args) > 4:
            print("** only one attribute can be updated at a time **")
            return

        try:
            casted_value = str(attribute_value)
            setattr(instance, attribute_name, casted_value)
            instance.save()
            print(f"Attribute {attribute_name} of {class_name} instance "
                  f"{instance_id} updated to {casted_value}.")
        except ValueError:
            print("** invalid attribute value **")

    def default(self, arg):
        """ Handle arbitrary input """

        try:
            class_name, method_call = arg.split(".", 1)

            """ handles show() command """
            if method_call.startswith("show(") and method_call.endswith(")"):
                instance_id = method_call[6:-2]
                key = f"{class_name}.{instance_id}"
                instances = storage.all()
                instance = instances.get(key)
                classes = [key.split('.')[0] for key in storage.all().keys()]
                if class_name in classes:
                    if instance:
                        print(instance)
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif method_call.startswith("all(") and method_call.endswith(")"):
                """ handles all() command """

                classes = [key.split('.')[0] for key in storage.all().keys()]
                if class_name in classes:
                    print([str(instance)
                           for key, instance in storage.all().items()
                           if key.startswith(f"{class_name}.")
                           ])
                else:
                    print("** class doesn't exist **")
            elif method_call.startswith("destroy("):
                """ handles destroy() command """

                instance_id = method_call[9:-2]
                key = f"{class_name}.{instance_id}"
                instances = storage.all()
                instance = instances.get(key)
                classes = [key.split('.')[0] for key in storage.all().keys()]

                if class_name in classes:
                    if key in instances:
                        del instances[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif method_call.startswith("update("):
                """ handles update() command """

                getArg = method_call[7:-1]
                getParam = [arg.strip(' "\'') for arg in getArg.split(',', 2)]
                """getParam = [arg for arg in getArg.split(',', 1)]"""
                classes = [key.split('.')[0] for key in storage.all().keys()]
                if "{" in getArg and "}" in getArg:
                    print("Dictionary is present")
                if class_name not in classes:
                    print("** class doesn't exist **")
                    return

                if len(getParam) < 1:
                    print("** instance id is missing **")
                    return

                instance_id = getParam[0]
                key = f"{class_name}.{instance_id}"
                instances = storage.all()
                instance = instances.get(key)

                if not instance:
                    print("** no instance found **")
                    return

                if "{" in getArg and "}" in getArg:
                    comma_index = getArg.index(',')

                    instance_id = getArg[:comma_index].strip(' "\'')
                    dicts = getArg[comma_index + 1:].strip()
                    my_dict = literal_eval(dicts)
                    for key, value in my_dict.items():
                        casted_value = str(value)
                        setattr(instance, key, casted_value)
                        instance.save()
                        """print(f"Attribute {attr_name} of "
                                f"{class_name} instance "
                                 f"{instance_id} updated "
                                 f"to {casted_value}.")"""
                    return

                if len(getParam) < 2:
                    print("** attribute name missing **")
                    return

                attr_name = getParam[1]

                if len(getParam) < 3:
                    print("** value missing **")
                    return

                attr_value = getParam[2]

                if len(getParam) > 3:
                    print("** only one attribute can be updated at a time **")
                    return
                try:
                    casted_value = str(attr_value)
                    setattr(instance, attr_name, casted_value)
                    instance.save()
                    """print(f"Attribute {attr_name} of {class_name} instance "
                            f"{instance_id} updated to {casted_value}.")"""
                except ValueError:
                    print("** invalid attribute value **")
            elif method_call.startswith("count("):
                """ handles count() command """
                classes = [key.split('.')[0] for key in storage.all().keys()]
                instances = storage.all()
                if class_name in classes:
                    instance_count = 0
                    for className in storage.all():
                        if className.split('.')[0] == class_name:
                            instance_count += 1
                    print("{}".format(instance_count))
                else:
                    print("** class doesn't exist **")
                    return
            else:
                print("*** Unknown command: {}".format(arg))
        except Exception as e:
            print(f"An error occured: {e}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
