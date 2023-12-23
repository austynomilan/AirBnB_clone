#!/usr/bin/python3
"""
module for test_console
"""
from unittest import TestCase
import sys
import io
from unittest.mock import patch
from console import HBNBCommand


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

    def test_BaseModel_all(self):
        """
        testing BaseModel.all() command
        """
        all_instances = BaseModel.all()
        self.assertIn(BaseModel(), all_instances)

    def test_Review_all(self):
        """
        testing Review.all() command
        """
        all_instances = Review.all()
        self.assertIn(Review(), all_instances)

    def test_User_all(self):
        """
        testing User.all() command
        """
        all_instances = User.all()
        self.assertIn(User(), all_instances)
    def test_State_all(self):
        """
        testing destroy BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("destroy BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_City_all(self):
        """
        testing destroy BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("destroy BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_Amenity_all(Self):
        """
        testing destroy BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("destroy BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_Place_All(self):
        """
        testing destroy BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("destroy BaseModel")
        self.assertTrue(f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
