#!/usr/bin/python3
"""
module for test_console
"""
from unittest import TestCase
import sys
import io
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel

class TestHBNBCommand(TestCase):
    """
    implementation of test for Console class
    """
    def test_quit(self):
        """
        testing the quit command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("quit")
        self.assertTrue(result)

    def test_EOF(self):
        """
        testing the EOF command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("EOF")
        self.assertTrue(result)

    def test_help(self):
        """
        testing the help command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("help")
        self.assertNotEqual(result, "")

    def test_emptyline(self):
        """
        testing the emptyline command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertEqual(f.getvalue().strip(), "")

    def test_create_BaseModel(self):
        """
        testing create BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertTrue(f.getvalue().strip())

    def tes_show_BaseModel(self):
        """
        testing show BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_destroy_BaseModel(self):
        """
        testing destroy BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("destroy BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_all_BaseModel(self):
        """
        testing all BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("all BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_update_BaseModel(self):
        """
        testing update BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("update BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_all(self):
        """
        testing all() command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            BaseModel = HBNBCommand().onecmd("BaseModel.all()")
            Review = HBNBCommand().onecmd("Review.all()")
            User = HBNBCommand().onecmd("User.all()")
            State = HBNBCommand().onecmd("State.all()")
            City = HBNBCommand().onecmd("City.all()")
            Amenity = HBNBCommand().onecmd("Amenity.all()")
            Place = HBNBCommand().onecmd("Place.all()")
        self.assertTrue(f.getvalue().strip())

    def test_count(self):
        """
        testing count() command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            BaseModel = HBNBCommand().onecmd("BaseModel.count()")
            Review = HBNBCommand().onecmd("Review.count()")
            User = HBNBCommand().onecmd("User.count()")
            State = HBNBCommand().onecmd("State.count()")
            City = HBNBCommand().onecmd("City.count()")
            Amenity = HBNBCommand().onecmd("Amenity.count()")
            Place = HBNBCommand().onecmd("Place.count()")
        self.assertTrue(f.getvalue().strip())

    def test_show(self):
        """
        testing show("id") command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            BaseModel = HBNBCommand().onecmd('BaseModel.show("id")')
            Review = HBNBCommand().onecmd('Review.show("id")')
            User = HBNBCommand().onecmd('User.show("id")')
            State = HBNBCommand().onecmd('State.show("id")')
            City = HBNBCommand().onecmd('City.show("id")')
            Amenity = HBNBCommand().onecmd('Amenity.show("id")')
            Place = HBNBCommand().onecmd('Place.show("id")')

    def test_destroy(Self):
        """
        testing destroy("id") command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            BaseModel = HBNBCommand().onecmd('BaseModel.destroy("id")')
            Review = HBNBCommand().onecmd('Review.destroy("id")')
            User = HBNBCommand().onecmd('User.destroy("id")')
            State = HBNBCommand().onecmd('State.destroy("id")')
            City = HBNBCommand().onecmd('City.destroy("id")')
            Amenity = HBNBCommand().onecmd('Amenity.destroy("id")')
            Place = HBNBCommand().onecmd('Place.destroy("id")')

    def test_update_attrs_value(Self):
        """
        testing update("id", "attribute_name",
                        "string_value")
                        command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            BaseModel = HBNBCommand().onecmd('BaseModel.update("id", "name", "AirBnB")')
            Review = HBNBCommand().onecmd('Review.update("id", "name", "AirBnB")')
            User = HBNBCommand().onecmd('User.update("id", "name", "AirBnB")')
            State = HBNBCommand().onecmd('State.update("id", "name", "AirBnB")')
            City = HBNBCommand().onecmd('City.update("id", "name", "AirBnB")')
            Amenity = HBNBCommand().onecmd('Amenity.update("id", "name", "AirBnB")')
            Place = HBNBCommand().onecmd('Place.update("id", "name", "AirBnB")')

    def test_update_with_dict(Self):
        """
        testing update() command with dictonary
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            BaseModel = HBNBCommand().onecmd('BaseModel.update("id", { "name", "AirBnB" })')
            Review = HBNBCommand().onecmd('Review.update("id", { "name", "AirBnB" })')
            User = HBNBCommand().onecmd('User.update("id", { "name", "AirBnB" })')
            State = HBNBCommand().onecmd('State.update("id", { "name", "AirBnB" })')
            City = HBNBCommand().onecmd('City.update("id", { "name", "AirBnB" })')
            Amenity = HBNBCommand().onecmd('Amenity.update("id", { "name", "AirBnB" })')
            Place = HBNBCommand().onecmd('Place.update("id", { "name", "AirBnB" })')


if __name__ == '__main__':
    unittest.main()
