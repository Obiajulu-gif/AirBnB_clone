#!/usr/bin/python3
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
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        """Assign a unique ID if not provided"""
        self._id = value if value else str(uuid.uuid4())

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Assign current datetime if not provided"""
        self._created_at = value if value else datetime.now()

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Assign current datetime if not provided"""
        self._updated_at = value if value else datetime.now()

    def update(self):
        """Update update_at with current datetime"""
        self.updated_at = datetime.now()

    def save(self):
        """Return a updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the object"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        
        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)


if __name__ == '__main__':
    base_model = BaseModel()

    print(base_model.to_dict())
    base_model.save()
    print(base_model.to_dict())
