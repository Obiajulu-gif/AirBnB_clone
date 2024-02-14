#!/usr/bin/python3
"""Test for city"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test City class"""

    def test_city(self):
        """Test City class"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
