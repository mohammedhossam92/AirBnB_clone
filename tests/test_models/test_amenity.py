#!/usr/bin/python3
# Import the unittest module and the Amenity class
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


# Create a subclass of unittest.TestCase
class TestAmenity(unittest.TestCase):

    # Use the setUp method to create an instance of the Amenity
    # class and assign a value to its name attribute
    def setUp(self):
        self.amenity = Amenity()
        # self.amenity.name = "Pool"

    # Use the assert methods to check the expected behavior
    # of the Amenity class and its attribute
    def test_amenity(self):
        # Check that the amenity instance is an object of the Amenity class
        self.assertIsInstance(self.amenity, Amenity)
        # Check that the amenity instance inherits from the BaseModel class
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))
        # Check that the amenity instance has a name attribute
        self.assertTrue(hasattr(self.amenity, "name"))
        # Check that the name attribute is a string
        self.assertIsInstance(self.amenity.name, str)
        # Check that the name attribute has the correct value
        # self.assertEqual(self.amenity.name, "Pool")


# Use the unittest.main function to run the tests
if __name__ == "__main__":
    unittest.main()
