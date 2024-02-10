#!/usr/bin/env python3
"""
BaseModel module
it defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
from models.engine.file_storage import storage


class BaseModel:
    """
    BaseModel:
    Represents a base model with common attributes
    and methods for other models.

    Attributes:
        id (str): a unique identifier for the object.
        created_at (datetime): date and time when the object was created.
        updated_at(datetime):date and time when the object was last updated.
    """

    format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key,
                                datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def update(self):
        """Update update_at with current datetime"""
        self.updated_at = datetime.now()

    def save(self):
        """Return a updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the object"""
        obj_dict = {
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'name': self.__dict__.get('name', None),
            'my_number': self.__dict__.get('my_number', None),
        }
        return obj_dict

    def __str__(self):
        """String Representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
