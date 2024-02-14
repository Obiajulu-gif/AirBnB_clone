#!/usr/bin/python3
"""Test for place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test Place class"""

    def test_place(self):
        """Test Place class"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.city_id, str)
        self.assertEqual(place.city_id, "")
        self.assertIsInstance(place.user_id, str)
        self.assertEqual(place.user_id, "")
        self.assertIsInstance(place.name, str)
        self.assertEqual(place.name, "")
        self.assertIsInstance(place.description, str)
        self.assertEqual(place.description, "")
        self.assertIsInstance(place.number_rooms, int)
        self.assertEqual(place.number_rooms, 0)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertIsInstance(place.max_guest, int)
        self.assertEqual(place.max_guest, 0)
        self.assertIsInstance(place.price_by_night, int)
        self.assertEqual(place.price_by_night, 0)
        self.assertIsInstance(place.latitude, float)
        self.assertEqual(place.latitude, 0.0)
        self.assertIsInstance(place.longitude, float)
        self.assertEqual(place.longitude, 0.0)
        self.assertIsInstance(place.amenity_ids, list)
        self.assertEqual(place.amenity_ids, [])
