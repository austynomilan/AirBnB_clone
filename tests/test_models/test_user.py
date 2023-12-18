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
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
