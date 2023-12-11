#!/usr/bin/python3
"""
test_base_model module
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    implementation of test case for BaseModel class
    """

    def test_module_document(self):
        """ Test for module documentation """
        doc_len = len(BaseModel.__module__.__doc__)
        self.assertGreaterEqual(doc_len, 5)

    def test_class_document(self):
        """ Test for class documentation """
        doc_len = len(BaseModel.__doc__)
        self.assertGreaterEqual(doc_len, 5)

    def test_init_document(self):
        """ Test for __init__ method documentation """
        doc_len = len(BaseModel.__init__.__doc__)
        self.assertGreaterEqual(doc_len, 5)

    def test_str_document(self):
        """ Test for __str__ method documentation """
        doc_len = len(BaseModel.__str__.__doc__)
        self.assertGreaterEqual(doc_len, 5)

    def test_save_document(self):
        """ Test for save method documentation """
        doc_len = len(BaseModel.save.__doc__)
        self.assertGreaterEqual(doc_len, 5)

    def test_to_dict_document(self):
        """ Test for to_dict method documentation """
        doc_len = len(BaseModel.to_dict.__doc__)
        self.asserGreaterEqual(doc_len, 5)


    def test_init_method(self):
        """ Test the init method """
        values = {
                'name': 'AirBnB',
                'my_number': 89
                }
        obj = BaseModel(**values)

        for key, value in values.items():
            self.assertEqual(getattr(obj, key), value)

        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)


    def test_str_method(self):
        """Test the string representation"""
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(model.__str__(), expected_str)

    def test_save_method(self):
        """Test the save method updates 'updated_at'"""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method functionality"""
        obj = BaseModel()
        obj.name = "AirBnB"
        obj.number = 89

        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIsInstance(obj_dict['name'], str)
        self.assertIsInstance(obj_dict['number'], int)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertIsInstance(obj_dict['__class__'], str)
        self.assertIsInstance(obj_dict['id'], str)


if __name__ == '__main__':
    unittest.main()
