#!/usr/bin/python3
# Import the unittest module and the BaseModel class
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models


# Create a subclass of unittest.TestCase
class TestBaseModel(unittest.TestCase):

    # Use the setUp method to create an instance of the BaseModel class and
    # assign some values to its attributes
    def setUp(self):
        self.base = BaseModel()

    # Use the assert methods to check the expected behavior of
    # the BaseModel class and its attributes and methods
    def test_base_model(self):
        # Check that the base instance is an object of the BaseModel class
        self.assertIsInstance(self.base, BaseModel)
        # Check that the base instance has the id, created_at,
        # and updated_at attributes
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))
        # Check that the id attribute is a string and unique
        self.assertIsInstance(self.base.id, str)
        self.assertNotEqual(self.base.id, BaseModel().id)
        # Check that the created_at and
        # updated_at attributes are datetime objects
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)
        # Check that the number attribute is an

    def test_save(self):
        # Check that the save method updates the updated_at attribute
        old_updated_at = self.base.updated_at
        self.base.save()
        new_updated_at = self.base.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        # Check that the save method saves the object to the storage
        self.assertIn(self.base, models.storage.all().values())

    def test_to_dict(self):
        time = datetime.utcnow()
        # Check that the to_dict method returns a dictionary
        self.assertIsInstance(self.base.to_dict(), dict)
        # Check that the dictionary has the correct keys and values
        self.assertEqual(self.base.to_dict()["__class__"], "BaseModel")
        self.assertEqual(self.base.to_dict()["id"], self.base.id)
        self.assertEqual(self.base.to_dict()["created_at"],
                         self.base.created_at.strftime(time))
        self.assertEqual(self.base.to_dict()["updated_at"], self.base.
                         updated_at.strftime(time))
        # Check that the dictionary does not have the _sa_instance_state key
        self.assertNotIn("_sa_instance_state", self.base.to_dict())

    def test_delete(self):
        # Check that the delete method removes the object from the storage
        self.base.delete()
        self.assertNotIn(self.base, models.storage.all().values())


# Use the unittest.main function to run the tests
if __name__ == "__main__":
    unittest.main()
