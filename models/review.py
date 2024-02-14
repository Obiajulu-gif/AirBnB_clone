#!/usr/bin/python3
"""
This is the review module
"""
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class Review(BaseModel):
    """
    This is the Review class
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        This is the __init__ method
        """
        super().__init__(*args, **kwargs)
