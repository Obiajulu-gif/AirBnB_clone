#!/usr/bin/python3
"""Test for state"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test State class"""

    def test_state(self):
        """Test State class"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.name, str)
        self.assertEqual(state.name, "")
        self.assertEqual(state.__class__.__name__, "State")
        self.assertEqual(state.__class__.__name__, "State")
