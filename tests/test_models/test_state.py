#!/usr/bin/python3
"""
Unittest for state.py
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for State class
    """
    def test_state_attr(self):
        """
        Test if attribute is created
        """
        attr = State()
        self.assertEqual(attr.name, "")

if __name__ == '__main__':
    unittest.main()
