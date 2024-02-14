#!/usr/bin/python3
"""Command interpreter module"""
import cmd
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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

    def do_create(self, arg):
        """Creates a new instance of the specified class, saves it, and prints its id"""
        if not arg:
            print("** class name missing **")
            return

        class_names = {"BaseModel", "State", "City", "Amenity", "Place", "Review"}
        arg = arg.split()
        class_name = arg[0]
        if class_name not in class_names:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        arg = arg.split()
        class_name = arg[0]
        if class_name not in {"State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        obj_id = arg[1]
        key = class_name + "." + obj_id
        all_objects = storage.all()
        obj = all_objects.get(key, None)

        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        arg = arg.split()
        class_name = arg[0]
        if class_name not in {"State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        obj_id = arg[1]
        key = class_name + "." + obj_id
        all_objects = storage.all()
        obj = all_objects.get(key, None)

        if obj is None:
            print("** no instance found **")
        else:
            del all_objects[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        all_classes = {"State", "City", "Amenity", "Place", "Review"}
        if not arg:
            all_objects = storage.all()
            for obj in all_objects.values():
                if obj.__class__.__name__ in all_classes:
                    print(obj)
        else:
            arg = arg.split()
            class_name = arg[0]
            if class_name not in all_classes:
                print("** class doesn't exist **")
                return

            all_objects = storage.all()
            filtered_objs = [str(obj) for obj in all_objects.values() if type(obj).__name__ == class_name]
            print(filtered_objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if not arg:
            print("** class name missing **")
            return

        arg = arg.split()
        class_name = arg[0]
        if class_name not in {"State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        obj_id = arg[1]
        key = class_name + "." + obj_id
        all_objects = storage.all()
        obj = all_objects.get(key, None)

        if obj is None:
            print("** no instance found **")
            return

        if len(arg) < 3:
            print("** attribute name missing **")
            return

        if len(arg) < 4:
            print("** value missing **")
            return

        attr_name = arg[2]
        attr_value = arg[3]

        if hasattr(obj, attr_name):
            attr_value = type(getattr(obj, attr_name))(attr_value)
            setattr(obj, attr_name, attr_value)
            storage.save()
        else:
            print("** attribute doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
