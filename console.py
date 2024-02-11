#!/usr/bin/python3
"""Command interpreter module"""

import cmd
from models.base_model import BaseModel
from models import storage


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
        """Called when an empty line entered"""
        pass

    def do_create(self, arg):
        """Create command to create a new instance"""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show command to print string representation of instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroy command to delete an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """All command to print all instances"""
        if arg:
            try:
                cls = eval(arg)
            except NameError:
                print("** class doesn't exist **")
                return
            objs = [str(obj)
                    for key, obj in storage.all().items()
                    if arg == key.split('.')[0]]
        else:
            objs = [str(obj) for obj in storage.all().values()]
        print(objs)

    def do_update(self, arg):
        """Update command to update an instance attribute"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        storage.save()

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for EOF command"""
        print("EOF command to exit the program")

    def help_help(self):
        """Help message for help command"""
        print("Help command to display available commands")

    def help_create(self):
        """Help message for create command"""
        print("Create command to create a new instance")

    def help_show(self):
        """Help message for show command"""
        print("Show command to print string representation of instance")

    def help_destroy(self):
        """Help message for destroy command"""
        print("Destroy command to delete an instance")

    def help_all(self):
        """Help message for all command"""
        print("All command to print all instances")

    def help_update(self):
        """Help message for update command"""
        print("Update command to update an instance attribute")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
