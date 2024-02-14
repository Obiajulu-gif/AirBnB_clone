#!/usr/bin/python3
"""
This is the amenity module
"""
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class Amenity(BaseModel):
    """
    This is the Amenity class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        This is the __init__ method
        """
        super().__init__(*args, **kwargs)
