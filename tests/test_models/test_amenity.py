#!/usr/bin/python3
import os
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test class for amenity"""
    def test_init(self):
        """method test for constructor"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_str(self):
        """test string method"""
        amenity = Amenity()
        str_representation = str(amenity)
        self.assertIn("[Amenity]", str_representation)
        self.assertIn("'id':", str_representation)
        self.assertIn("'created_at':", str_representation)
        self.assertIn("'updated_at':", str_representation)
        self.assertIn("'name':", str_representation)

    def test_name(self):
        """test the name of the amenity"""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")


if __name__ == '__main__':
    unittest.main()
