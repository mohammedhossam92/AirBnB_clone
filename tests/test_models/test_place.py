#!/usr/bin/python3
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_init(self):
        """
        Test the __init__ method of the Place class
        """
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertEqual(place.city_id, "")
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertEqual(place.user_id, "")
        self.assertTrue(hasattr(place, 'name'))
        self.assertEqual(place.name, "")
        self.assertTrue(hasattr(place, 'description'))
        self.assertEqual(place.description, "")
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertEqual(place.number_rooms, 0)
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertEqual(place.max_guest, 0)
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertEqual(place.price_by_night, 0)
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertEqual(place.latitude, 0.0)
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(place.amenity_ids, [])

    def test_str(self):
        """
        Test the __str__ method of the Place class
        """
        place = Place()
        str_representation = str(place)
        self.assertIn("[Place]", str_representation)
        self.assertIn("'id':", str_representation)
        self.assertIn("'created_at':", str_representation)
        self.assertIn("'updated_at':", str_representation)
        self.assertIn("'city_id':", str_representation)
        self.assertIn("'user_id':", str_representation)
        self.assertIn("'name':", str_representation)

    def test_name(self):
        """
        Test setting the name attribute of the Place class
        """
        place = Place()
        place.name = "Cozy Cottage"
        self.assertEqual(place.name, "Cozy Cottage")


if __name__ == '__main__':
    unittest.main()
