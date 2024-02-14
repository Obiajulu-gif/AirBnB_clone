#!/usr/bin/python3
"""
This is the state module
"""
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class State(BaseModel):
    """
    This is the State class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        This is the __init__ method
        """
        super().__init__(*args, **kwargs)
