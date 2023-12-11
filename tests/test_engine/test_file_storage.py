#!/usr/bin/python3
"""importing modules """
import unittest
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """class test file"""
    def setUp(self):
        """class to test"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """class testt tear"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_empty(self):
        """class test test """
        result = self.storage.all()
        self.assertEqual(result, {})

    def test_new_object_added(self):
        """class test user """
        user = User()
        self.storage.new(user)
        result = self.storage.all()
        self.assertEqual(len(result), 1)
        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertIn(key, result)

    def test_save_and_reload(self):
        """class test sava and reload """
        user = User()
        self.storage.new(user)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        result = new_storage.all()
        self.assertEqual(len(result), 1)
        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertIn(key, result)

    def test_obj_to_dict(self):
        """class test obj """
        user = User()
        result = self.storage.obj_to_dict(user)
        expected = user.to_dict() if hasattr(user, 'to_dict') \
            else user.__dict__
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
