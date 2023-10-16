#!/usr/bin/python3
""" Console module for AirBnB """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Class for the console AirBnB"""
    prompt = "(hbnb) "

    all_class = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]

   
    attr_float = ["latitude", "longitude"]
    attr_int = ["number_rooms", "number_bathrooms",
                "max_guest", "price_by_night"]
    attr_str = ["name", "amenity_id", "place_id", "state_id",
                "user_id", "city_id", "description", "text",
                "email", "password", "first_name", "last_name"]

    def do_quit(self, arg):
        """exit the program
        """
        return True

    def do_EOF(self, arg):
        """Ctrl + D to exit the program
        """
        print("")
        return True

    def emptyline(self):
        """An empty line + ENTER shouldnt execute anything
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it 
        (to the JSON file) and prints the id
        Usage: create <class name>
        """
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        if self.valid(arg):
            args = arg.split()
            if args[0] in classes:
                new = classes[args[0]]()
            storage.save()
            print(new.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based
        on the class name and id
        Usage: show <class name> <id>
        """
        if self.valid(arg, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            print(storage.all()[_key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        Usage: destroy <class name> <id>
        """
        if self.valid(arg, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            del storage.all()[_key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name
        Usage: all OR all <class name>
        """
        args = arg.split()
        _len = len(args)
        my_list = []
        if _len >= 1:
            if args[0] not in HBNBCommand.all_class:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if args[0] in key:
                    my_list.append(str(value))
        else:
            for key, value in storage.all().items():
                my_list.append(str(value))
        print(my_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"

        """
        pass

    def do_clear(self, arg):
        """Clear data storage :
        Usage: clear
        """
        storage.all().clear()
        self.do_all(arg)
        print("** All data been clear! **")

    def valid(self, arg, _id_flag=False, _att_flag=False):
        """validation of argument that pass to commands
        """
        args = arg.split()
        _len = len(arg.split())
        if _len == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.all_class:
            print("** class doesn't exist **")
            return False
        if _len < 2 and _id_flag:
            print("** instance id missing **")
            return False
        if _id_flag and args[0]+"."+args[1] not in storage.all():
            print("** no instance found **")
            return False
        if _len == 2 and _att_flag:
            print("** attribute name missing **")
            return False
        if _len == 3 and _att_flag:
            print("** value missing **")
            return False
        return True

    def casting(self, arg):
        """cast string to float or int if possible"""
        try:
            if "." in arg:
                arg = float(arg)
            else:
                arg = int(arg)
        except ValueError:
            pass
        return arg

    def count(self, arg):
        """the number of instances of a class
        Usage: <class name>.count()
        """
        count = 0
        for key in storage.all():
            if arg[:-1] in key:
                count += 1
        print(count)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
