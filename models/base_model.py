#!/usr/bin/env python3
"""
BaseModel module
it defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


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

    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = id if id else str(uuid.uuid4())
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def update(self):
        """Update update_at with current datetime"""
        self.updated_at = datetime.now()

    def save(self):
        """Return a updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()

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
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)


if __name__ == '__main__':
    base_model = BaseModel()

    print(base_model.to_dict())
    base_model.save()
    print(base_model.to_dict())
