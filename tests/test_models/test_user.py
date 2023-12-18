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

    def test_user(self):
        """Test user attribute initialization"""

        user = User()
        user.email = "airbnb@email.com"
        user.password = "Airbnbpass"
        user.first_name = "Air"
        user.last_name = "Bnb"

        self.assertEqual(user.email, "airbnb@email.com")
        self.assertEqual(user.password, "Airbnbpass")
        self.assertEqual(user.first_name, "Air")
        self.assertEqual(user.last_name, "Bnb")


if __name__ == '__main__':
    unittest.main()
