#!/usr/bin/python3
"""Test for review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review class"""

    def test_review(self):
        """Test Review class"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
