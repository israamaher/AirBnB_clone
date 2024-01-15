#!/usr/bin/python3
"""_summary_
"""
import cmd
import models

from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the command interpreter.
        that handles the "quit" command"""
        return True

    def do_EOF(self, arg):
        """Ctrl+D on Unix-like systems or Ctrl+Z on Windows,
            indicating the end of input.
            The purpose of do_EOF is to handle the end of input gracefully.
        """
        print()
        return True

    def do_help(self, arg):
        """help information."""
        super().do_help(arg)

    def emptyline(self):
        """nothing on an empty line."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the ID."""
        if not arg:
            print("** class name missing **")
            return

        if arg not in globals():
            print("** class doesn't exist **")
            return

        try:
            class_name = globals()[arg]
            new_obj = class_name()
            models.storage.save()
            print(new_obj.id)
        except Exception as e:
            print("** {}".format(str(e)))

    def do_show(self, arg):
        """print"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        id_arg = args[1]

        key = "{}.{}".format(class_name, id_arg)
        if key not in models.storage.all():
            print("** no instance found **")
            return

        obj_dict = storage.all()[key]
        print(obj_dict)

    def do_destroy(self, arg):
        """delete in obj based on the class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id_arg = args[1]

        key = "{}.{}".format(class_name, id_arg)
        obj = models.storage.all()

        if key not in obj:
            print("** no instance found **")
            return
        del obj[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all obj"""
        args = arg.split()

        if not args:
            for obj in storage.all().values():
                print(str(obj))
        else:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return

            for key, obj in storage.all().items():
                if key.startswith(class_name):
                    print(str(obj))

    def do_update(self, arg):
        """update in class"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        name_attri = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        value_attri_str = args[3]

        if name_attri not in getattr(globals()[class_name], "__dict__"):
            print("** attribute doesn't exist **")
            return

        instance = instances[key]

        attribute_type = type(getattr(instance, name_attri))

        try:
            value_attri = attribute_type(value_attri_str)
        except ValueError:
            print("** invalid value **")
            return

        setattr(instance, name_attri, value_attri)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
