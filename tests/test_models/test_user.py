# Import the unittest module and the User class
import unittest
from models.user import User
from models.base_model import BaseModel


# Create a subclass of unittest.TestCase
class TestUser(unittest.TestCase):

    # Use the setUp method to create an instance
    # of the User class and assign some values to its attributes
    def setUp(self):
        self.user = User()
        # self.user.email = "user@example.com"
        # self.user.password = "123456"
        # self.user.first_name = "John"
        # self.user.last_name = "Doe"

    # Use the assert methods to check the expected
    # behavior of the User class and its attributes
    def test_user(self):
        # Check that the user instance is an object of the User class
        self.assertIsInstance(self.user, User)
        # Check that the user instance inherits from the BaseModel class
        self.assertTrue(issubclass(self.user.__class__, BaseModel))
        # Check that the user instance has the four attributes
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        # Check that the attributes are strings
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        # Check that the attributes have the correct values
        # self.assertEqual(self.user.email, "user@example.com")
        # self.assertEqual(self.user.password, "123456")
        # self.assertEqual(self.user.first_name, "John")
        # self.assertEqual(self.user.last_name, "Doe")


# Use the unittest.main function to run the tests
if __name__ == "__main__":
    unittest.main()
