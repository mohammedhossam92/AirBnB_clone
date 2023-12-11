#!/usr/bin/python3

import os
import time
import unittest
from unittest import mock
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""
    def test_init(self):
        """Test the initialization of the BaseModel instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method of the BaseModel instance."""
        my_model = BaseModel()
        str_representation = str(my_model)
        self.assertIn("[BaseModel]", str_representation)
        self.assertIn("'id':", str_representation)
        self.assertIn("'created_at':", str_representation)
        self.assertIn("'updated_at':", str_representation)

    # def test_save(self):
    #     """Test the save method of the BaseModel instance."""
    #     my_model = BaseModel()
    #     original_updated_at = my_model.updated_at
    #     time.sleep(0.01)
    #     my_model.save()
    #     self.assertNotEqual(original_updated_at, my_model.updated_at)

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        time.sleep(0.01)
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel instance."""
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_custom_attributes(self):
        """Test the addition of custom attributes to the BaseModel instance."""
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.number = 89
        self.assertEqual([my_model.name, my_model.number], ["ALX", 89])


if __name__ == '__main__':
    unittest.main()
