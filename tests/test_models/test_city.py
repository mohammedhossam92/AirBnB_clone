#!/usr/bin/python3
# Import the unittest module and the City class
import unittest
from models.city import City
from models.base_model import BaseModel


# Create a subclass of unittest.TestCase
class TestCity(unittest.TestCase):

    # Use the setUp method to create an instance of the City class
    # and assign some values to its attributes
    def setUp(self):
        self.city = City()
        self.city.state_id = "1"
        self.city.name = "New York"

    # Use the assert methods to check the expected behavior of the City
    # class and its attributes
    def test_city(self):
        # Check that the city instance is an object of the City class
        self.assertIsInstance(self.city, City)
        # Check that the city instance inherits from the BaseModel class
        self.assertTrue(issubclass(self.city.__class__, BaseModel))
        # Check that the city instance has the two attributes
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        # Check that the attributes are strings
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)
        # Check that the attributes have the correct values
        self.assertEqual(self.city.state_id, "1")
        self.assertEqual(self.city.name, "New York")


# Use the unittest.main function to run the tests
if __name__ == "__main__":
    unittest.main()
