#!/usr/bin/python3
"""
Unittest for review.py
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for Review class
    """
    def test_review_attr(self):
        """
        Test if attribute is created
        """
        attr = Review()
        self.assertEqual(attr.place_id, "")
        self.assertEqual(attr.user_id, "")
        self.assertEqual(attr.text, "")

if __name__ == '__main__':
    unittest.main()
