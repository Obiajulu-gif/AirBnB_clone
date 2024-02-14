#!/usr/bin/python3
"""
this is the user module
"""
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """String representation of the User class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Save method"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Dictionary representation of the User class"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
