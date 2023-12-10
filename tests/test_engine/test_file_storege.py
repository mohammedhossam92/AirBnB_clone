#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    """test class storage"""
    def setUp(self):
        """test method"""
        try:
            os.remove(storage._FileStorage__file_path)
        except FileNotFoundError:
            pass
        storage.reload()

    def tearDown(self):
        """test"""
        try:
            os.remove(storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """test all functions"""
        self.assertEqual(storage.all(), {})

    def test_new(self):
        """test adding new suer"""
        user = User()
        storage.new(user)
        self.assertIn("User." + user.id, storage.all())

    def test_save_reload(self):
        """test saving data"""
        user = User()
        user_key = "User." + user.id

        storage.new(user)
        storage.save()

        del storage.all()[user_key]

        storage.reload()

        self.assertIn(user_key, storage.all())


if __name__ == '__main__':
    unittest.main()
