#!/usr/bin/python3
# Import the unittest module and the State class
import unittest
from models.state import State
from models.base_model import BaseModel


# Create a subclass of unittest.TestCase
class TestState(unittest.TestCase):

    # Use the setUp method to create an
    # instance of the State class and assign a value to its name attribute
    def setUp(self):
        self.state = State()
        self.state.name = "California"

    # Use the assert methods to check the
    # expected behavior of the State class and its attribute
    def test_state(self):
        # Check that the state instance is an object of the State class
        self.assertIsInstance(self.state, State)
        # Check that the state instance inherits from the BaseModel class
        self.assertTrue(issubclass(self.state.__class__, BaseModel))
        # Check that the state instance has a name attribute
        self.assertTrue(hasattr(self.state, "name"))
        # Check that the name attribute is a string
        self.assertIsInstance(self.state.name, str)
        # Check that the name attribute has the correct value
        self.assertEqual(self.state.name, "California")


# Use the unittest.main function to run the tests
if __name__ == "__main__":
    unittest.main()
