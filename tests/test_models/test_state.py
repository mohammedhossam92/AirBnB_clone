#!/usr/bin/python3
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    def test_init(self):
        """
        Test the __init__ method of the State class
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_str(self):
        """
        Test the __str__ method of the State class
        """
        state = State()
        str_representation = str(state)
        self.assertIn("[State]", str_representation)
        self.assertIn("'id':", str_representation)
        self.assertIn("'created_at':", str_representation)
        self.assertIn("'updated_at':", str_representation)
        self.assertIn("'name':", str_representation)

    def test_name(self):
        """
        Test setting the name attribute of the State class
        """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()
