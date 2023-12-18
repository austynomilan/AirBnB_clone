#!/usr/bin/python3
""" module for test_user """
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ implementing test class for User """

    def test_module_document(self):
        """ Test for module documentation """
        doc_len = len(User.__module__.__doc__)
        self.assertGreaterEqual(doc_len, 5)

    def test_class_document(self):
        """ Test for class documentation """
        doc_len = len(User.__doc__)
        self.assertGreaterEqual(doc_len, 5)

    def setup(self):
        """Test user attribute initialization"""
        User.email = "airbnb@email.com"
        User.password = "Airbnbpass"
        User.first_name = "Air"
        User.last_name = "Bnb"

        self.assertEqual(User.email, "airbnb@email.com")
        self.assertEqual(User.password, "Airbnbpass")
        self.assertEqual(User.first_name, "Air")
        self.assertEqual(User.last_name, "Bnb")


if __name__ == '__main__':
    unittest.main()
