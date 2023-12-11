#!/usr/bin/python3
# Import the unittest module and the Place class
import unittest
from models.place import Place
from models.base_model import BaseModel


# Create a subclass of unittest.TestCase
class TestPlace(unittest.TestCase):

    # Use the setUp method to create an instance of the Place class
    # and assign some values to its attributes
    def setUp(self):
        self.place = Place()
        self.place.city_id = "1"
        self.place.user_id = "2"
        self.place.name = "My place"
        self.place.description = "A cozy apartment"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 40.0
        self.place.longitude = -3.0
        self.place.amenity_ids = ["3", "4"]

    # Use the assert methods to check the expected behavior of the
    # Place class and its attributes
    def test_place(self):
        # Check that the place instance is an object of the Place class
        self.assertIsInstance(self.place, Place)
        # Check that the place instance inherits from the BaseModel class
        self.assertTrue(issubclass(self.place.__class__, BaseModel))
        # Check that the place instance has the eleven attributes
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        # Check that the attributes have the correct types
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)
        # Check that the attributes have the correct values
        self.assertEqual(self.place.city_id, "1")
        self.assertEqual(self.place.user_id, "2")
        self.assertEqual(self.place.name, "My place")
        self.assertEqual(self.place.description, "A cozy apartment")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 40.0)
        self.assertEqual(self.place.longitude, -3.0)
        self.assertEqual(self.place.amenity_ids, ["3", "4"])


# Use the unittest.main function to run the tests
if __name__ == "__main__":
    unittest.main()
