#!/usr/bin/python3
""" Console module for AirBnB """
import cmd



class HBNBCommand(cmd.Cmd):
    """Class for the console AirBnB"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exit the program
        """
        return True

    def do_EOF(self, arg):
        """Ctrl + D to exit the program
        """
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldnt execute anything
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
