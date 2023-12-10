#!/usr/bin/python3
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_init(self):
        """Test the initialization of the City instance."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")

    def test_str(self):
        """Test the __str__ method of the City instance."""
        city = City()
        str_representation = str(city)
        self.assertIn("[City]", str_representation)
        self.assertIn("'id':", str_representation)
        self.assertIn("'created_at':", str_representation)
        self.assertIn("'updated_at':", str_representation)
        self.assertIn("'state_id':", str_representation)
        self.assertIn("'name':", str_representation)

    def test_state_id(self):
        """Test the 'state_id' attribute of the City instance."""
        city = City()
        city.state_id = "CA"
        self.assertEqual(city.state_id, "CA")

    def test_name(self):
        """Test the 'name' attribute of the City instance."""
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")


if __name__ == '__main__':
    unittest.main()
