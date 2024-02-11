#!/usr/bin/python3
"""Command interpreter module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for EOF command"""
        print("EOF command to exit the program")

    def help_help(self):
        """Help message for help command"""
        print("Help command to display available commands")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
