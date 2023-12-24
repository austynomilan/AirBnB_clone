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
        testing BaseModel.all() commandd
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
            result = HBNBCommand().onecmd(" BaseModel")
        self.assertTrue(f.getvalue().strip())
        
    def test_BaseModel_count(self):
        """
        testing BaseModel.all() commandd
        """
        all_instances = BaseModel.count()
        self.assertIn(BaseModel(), all_instances)

    def test_Review_count(self):
        """
        testing Review.all() command
        """
        all_instances = Review.count()
        self.assertIn(Review(), all_instances)

    def test_User_count(self):
        """
        testing User.all() command
        """
        all_instances = User.count()
        self.assertIn(User(), all_instances)
        
    def test_State_count(self):
        """
        testing destroy BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("destroy BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_City_count(self):
        """
        testing destroy BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("destroy BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_Amenity_count(Self):
        """
        testing destroy BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("destroy BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_Place_count(self):
        """
        testing destroy BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd(" BaseModel")
        self.assertTrue(f.getvalue().strip())
        
    def test_BaseModel_show(self):
        """
        testing BaseModel.show() commandd
        """
        all_instances = BaseModel.show()
        self.assertIn(BaseModel(), all_instances)

    def test_Review_show(self):
        """
        testing Review.show() command
        """
        all_instances = Review.show()
        self.assertIn(Review(), all_instances)

    def test_User_show(self):
        """
        testing User.show() command
        """
        all_instances = User.show()
        self.assertIn(User(), all_instances)
        
    def test_State_show(self):
        """
        testing destroy BaseModel command
        """
        all_instances = State.show()
        self.assertIn(State(), all_instances)

    def test_City_show(self):
        """
        testing destroy BaseModel command
        """
        all_instances = City.show()
        self.assertIn(City(), all_instances)

    def test_Amenity_show(Self):
        """
        testing destroy BaseModel command
        """
        all_instances = Amenity.show()
        self.assertIn(Amenity(), all_instances)

    def test_Place_show(self):
        """
        testing destroy BaseModel command
        """
        all_instances = Place.show()
        self.assertIn(Place(), all_instances)
        
    def test_BaseModel_destroy(self):
        """
        testing BaseModel.destroy() commandd
        """
        all_instances = BaseModel.destroy()
        self.assertIn(BaseModel(), all_instances)

    def test_Review_destroy(self):
        """
        testing Review.destroy() command
        """
        all_instances = Review.destroy()
        self.assertIn(Review(), all_instances)

    def test_User_destroy(self):
        """
        testing User.destroy() command
        """
        all_instances = User.destroy()
        self.assertIn(User(), all_instances)
        
    def test_State_destroy(self):
        """
        testing destroy BaseModel command
        """
        all_instances = State.destroy()
        self.assertIn(State(), all_instances)

    def test_City_destroy(self):
        """
        testing destroy BaseModel command
        """
        all_instances = City.destroy()
        self.assertIn(City(), all_instances)

    def test_Amenity_destroy(Self):
        """
        testing destroy BaseModel command
        """
        all_instances = Amenity.destroy()
        self.assertIn(Amenity(), all_instances)

    def test_Place_destroy(self):
        """
        testing destroy BaseModel command
        """
        all_instances = Place.destroy()
        self.assertIn(Place(), all_instances)
        
    def test_BaseModel_update(self):
        """
        testing BaseModel.update() commandd
        """
        all_instances = BaseModel.update()
        self.assertIn(BaseModel(), all_instances)

    def test_Review_update(self):
        """
        testing Review.all() command
        """
        all_instances = Review.update()
        self.assertIn(Review(), all_instances)

    def test_User_update(self):
        """
        testing User.all() command
        """
        all_instances = User.update()
        self.assertIn(User(), all_instances)
        
    def test_State_update(self):
        """
        testing update BaseModel command
        """
        all_instances = State.update()
        self.assertIn(State(), all_instances)

    def test_City_update(self):
        """
        testing update BaseModel command
        """
        all_instances = City.update()
        self.assertIn(City(), all_instances)

    def test_Amenity_update(Self):
        """
        testing update BaseModel command
        """
        all_instances = Amenity.update()
        self.assertIn(Amenity(), all_instances)

    def test_Place_update(self):
        """
        testing update BaseModel command
        """
        all_instances = Place.update()
        self.assertIn(Place(), all_instances)


if __name__ == '__main__':
    unittest.main()
