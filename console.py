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
    """AirBnB console """
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
        if self.valid(arg, True, True):
            args = arg.split()
            _key = args[0] + "." + args[1]
            if args[3].startswith('"'):
                match = re.search(r'"([^"]+)"', arg).group(1)
            elif args[3].startswith("'"):
                match = re.search(r'\'([^\']+)\'', arg).group(1)
            else:
                match = args[3]
            if args[2] in HBNBCommand.attr_str:
                setattr(storage.all()[_key], args[2], str(match))
            elif args[2] in HBNBCommand.attr_int:
                setattr(storage.all()[_key], args[2], int(match))
            elif args[2] in HBNBCommand.attr_float:
                setattr(storage.all()[_key], args[2], float(match))
            else:
                setattr(storage.all()[_key], args[2], self.casting(match))
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
