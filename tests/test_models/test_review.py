#!/usr/bin/python3
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    def test_init(self):
        """Test the initialization of the Review instance."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, "")

    def test_str(self):
        """Test the __str__ method of the Review instance."""
        review = Review()
        str_representation = str(review)
        self.assertIn("[Review]", str_representation)
        self.assertIn("'id':", str_representation)
        self.assertIn("'created_at':", str_representation)
        self.assertIn("'updated_at':", str_representation)
        self.assertIn("'place_id':", str_representation)
        self.assertIn("'user_id':", str_representation)
        self.assertIn("'text':", str_representation)

    def test_text(self):
        """Test the 'text' attribute of the Review instance."""
        review = Review()
        review.text = "Great experience!"
        self.assertEqual(review.text, "Great experience!")


if __name__ == '__main__':
    unittest.main()
