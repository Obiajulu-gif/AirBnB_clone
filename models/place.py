#!/usr/bin/python3
"""
This is the place module
"""
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class Place(BaseModel):
    """
    This is the Place class
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        This is the __init__ method
        """
        super().__init__(*args, **kwargs)
