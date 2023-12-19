#!/usr/bin/python3
"""
Unittest for place
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for Place class
    """
    def test_place_attr(self):
        """
        Test if attribute is created
        """
        attr = Place()
        self.assertEqual(attr.city_id, "")
        self.assertEqual(attr.user_id, "")
        self.assertEqual(attr.name, "")
        self.assertEqual(attr.description, "")
        self.assertEqual(attr.number_rooms, 0)
        self.assertEqual(attr.number_bathrooms, 0)
        self.assertEqual(attr.max_guest, 0)
        self.assertEqual(attr.price_by_night, 0)
        self.assertEqual(attr.latitude, 0.0)
        self.assertEqual(attr.longitude, 0.0)
        self.assertEqual(attr.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
