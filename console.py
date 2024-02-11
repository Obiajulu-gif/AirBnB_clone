#!/usr/bin/python3
"""
this is the entry point for the console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Quit command to exit the program"""
        print()
        return True

    def help_quit(self):
        """Help command to show the help"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help command to show the help"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help command to show the help"""
        print("Quit command to exit the program")

    def do_help(self, arg: str) -> bool | None:
        """Help command to show the help"""
        return super().do_help(arg)

    def emptyline(self):
        """Empty line command"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
