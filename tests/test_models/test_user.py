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

        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")


if __name__ == '__main__':
    unittest.main()
