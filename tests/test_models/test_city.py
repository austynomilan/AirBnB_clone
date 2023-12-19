#!/usr/bin/python3
"""
Unittest for city.py
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for City class
    """
    def test_city_attr(self):
        """
        Test if attribute is created
        """
        attr = City()
        self.assertEqual(attr.state_id, "")
        self.assertEqual(attr.name, "")


if __name__ == '__main__':
    unittest.main()
