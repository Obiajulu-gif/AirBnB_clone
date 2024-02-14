#!/usr/bin/python3
"""
This is the city module
"""
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class City(BaseModel):
    """
    This is the City class
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        This is the __init__ method
        """
        super().__init__(*args, **kwargs)
