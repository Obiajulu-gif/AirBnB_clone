#!/usr/bin/python3
"""Test for amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    def test_amenity(self):
        """Test Amenity class"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.name, str)
        self.assertEqual(amenity.name, "")
