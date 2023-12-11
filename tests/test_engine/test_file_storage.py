#!/usr/bin/python3
"""importing modules """
import unittest
import json
import os
from models.base_model import BaseModel
# from models.amenity import Amenity
# from models.city import City
from models.place import Place
# from models.review import Review
# from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage

# Create a subclass of unittest.TestCase


class TestFileStorage(unittest.TestCase):

    # Use the setUp method to create an instance
    # of FileStorage and some sample objects
    def setUp(self):
        self.storage = FileStorage()
        self.obj1 = BaseModel()
        self.obj2 = User()
        self.obj3 = Place()

    # Use the assert methods to check the expected
    # behavior of the FileStorage methods and variables
    def test_all(self):
        # Check that the all method returns a dictionary of objects
        self.assertIsInstance(self.storage.all(), dict)
        # Check that the dictionary is initially empty
        self.assertEqual(len(self.storage.all()), 0)

    def test_new(self):
        # Check that the new method adds an object to the __objects dictionary
        self.storage.new(self.obj1)
        self.assertIn("BaseModel.{}".format(self.obj1.id), self.storage.all())
        self.storage.new(self.obj2)
        self.assertIn("User.{}".format(self.obj2.id), self.storage.all())
        self.storage.new(self.obj3)
        self.assertIn("Place.{}".format(self.obj3.id), self.storage.all())
        # Check that the new method does nothing if the object is None
        self.storage.new(None)
        self.assertEqual(len(self.storage.all()), 3)

    def test_save(self):
        # Check that the save method creates a file.json file
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        # Check that the file.json file contains the correct data
        with open("file.json", "r") as f:
            data = json.load(f)
            self.assertEqual(data, self.storage.all())

    def test_reload(self):
        # Check that the reload method loads the data from the file.json file
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})
        self.storage.new(self.obj1)
        self.storage.new(self.obj2)
        self.storage.new(self.obj3)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 3)
        # Check that the reload method creates
        # the correct objects from the data
        for key, value in self.storage.all().items():
            self.assertIsInstance(value, eval(value.__class__.__name__))
        # Check that the reload method does
        # nothing if the file.json file does not exist
        os.remove("file.json")
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 3)

    def test_obj_to_dict(self):
        # Check that the obj_to_dict method
        # returns a dictionary representation of an object
        self.assertIsInstance(self.storage.obj_to_dict(self.obj1), dict)
        self.assertEqual(self.storage.obj_to_dict(self.obj1),
                         self.obj1.to_dict())
        # Check that the obj_to_dict method
        # returns the __dict__ attribute of an object
        # if it does not have a to_dict method
        self.assertIsInstance(self.storage.obj_to_dict(self.storage), dict)
        self.assertEqual(self.storage.obj_to_dict(self.storage),
                         self.storage.__dict__)

    # Use the tearDown method to delete the file.json file after each test
    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

# Use the unittest.main function to run the tests


if __name__ == "__main__":
    unittest.main()
