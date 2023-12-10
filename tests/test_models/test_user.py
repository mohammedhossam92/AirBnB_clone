#!/usr/bin/python3
import unittest
from datetime import datetime  # Importing the datetime module
from models.user import User


class TestUser(unittest.TestCase):
    def test_init(self):
        """Test the initialization of the User instance."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_str(self):
        """Test the __str__ method of the User instance."""
        user = User()
        user.first_name = "John"
        user.last_name = "Doe"
        str_representation = str(user)
        self.assertIn("[User]", str_representation)
        self.assertIn("'id':", str_representation)
        self.assertIn("'created_at':", str_representation)
        self.assertIn("'updated_at':", str_representation)
        self.assertIn("'email':", str_representation)
        self.assertIn("'password':", str_representation)
        self.assertIn("'first_name':", str_representation)
        self.assertIn("'last_name':", str_representation)
        self.assertIn("John", str_representation)
        self.assertIn("Doe", str_representation)


if __name__ == '__main__':
    unittest.main()
