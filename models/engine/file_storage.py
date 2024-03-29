#!/usr/bin/python3
"""
FileStorage module that create a unique FileStorage instance for my
Application
"""
import json
from os.path import exists, isfile


class FileStorage:
    """FileStorage class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return type(self).__objects

    def new(self, obj):
        """Sets in __object the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        try:
            serialized_objs = {key: value.to_dict()
                               for key, value in type(self).__objects.items()}
            with open(type(self).__file_path, "w", encoding="UTF-8") as f:
                json.dump(serialized_objs, f, indent=4)
        except (IOError, OSError) as e:
            print("Error saving to file: {}".format(e))

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if exists(type(self).__file_path) and isfile(type(self).__file_path):
            try:
                with open(self.__file_path, "r", encoding="UTF-8") as f:
                    serialized_objs = json.load(f)
                    for key, value in serialized_objs.items():
                        class_name = value.get('__class__')
                        if class_name:
                            self.__objects[key] = eval(class_name)(**value)
            except (IOError, OSError) as e:
                print("Error loading from file: {}".format(e))
        else:
            print("File not found")
            return

    def serialize(self):
        """Return the dictionary __objects."""
        return {key: value.to_dict()
                for key, value in type(self).__objects.items()}
    
    def deserialize(self, serialized_objs):
        """Deserializes the JSON file to __objects."""
        for key, value in serialized_objs.items():
            class_name = value.get('__class__')
            if class_name:
                self.__objects[key] = eval(class_name)(**value)
   


storage = FileStorage()
storage.reload()
