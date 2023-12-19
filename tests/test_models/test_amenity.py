#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class
    """
    def test_amenity_attr(self):
        """
        Test if attribute is created
        """
        attr = Amenity()
        self.assertEqual(attr.name, "")


if __name__ == '__main__':
    unittest.main()
