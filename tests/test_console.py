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


if __name__ == '__main--':
    unittest.main()
