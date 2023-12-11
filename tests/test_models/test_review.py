#!/usr/bin/python3
# Import the unittest module and the Review class
import unittest
from models.review import Review
from models.base_model import BaseModel


# Create a subclass of unittest.TestCase
class TestReview(unittest.TestCase):

    # Use the setUp method to create an instance
    # of the Review class and assign some values to its attributes
    def setUp(self):
        self.review = Review()
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "Nice place"

    # Use the assert methods to check the expected behavior
    # of the Review class and its attributes
    def test_review(self):
        # Check that the review instance is an object of the Review class
        self.assertIsInstance(self.review, Review)
        # Check that the review instance inherits from the BaseModel class
        self.assertTrue(issubclass(self.review.__class__, BaseModel))
        # Check that the review instance has the three attributes
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        # Check that the attributes are strings
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)
        # Check that the attributes have the correct values
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text, "Nice place")


# Use the unittest.main function to run the tests
if __name__ == "__main__":
    unittest.main()
