#!/usr/bin/python3
"""contains the entry point of the command interpreter."""
import cmd

class HBNBCommand(cmd.Cmd):
    """The class that implements the console
    for the AirBnB clone web application

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_EOF(self, argv):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()