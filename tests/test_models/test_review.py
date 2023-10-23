#!/usr/bin/python3
"""Defines the Review Test class."""
from models.base_model import BaseModel
from models.review import Review
import unittest
import os


class TestReview(unittest.TestCase):
    """
    Tests that the BaseModel works okay
    """

    def setUp(self):
        """
        Set up method
        It renames the file_storage file to avoid conflicting with data
        """
        if os.path.isfile("file.json"):
            os.rename("file.json", "backup.json")

        self.model_1 = Review()
        self.model_2 = Review()

    def tearDown(self):
        """
        Tear down method
        Does clean up and renames the json file back to the original name
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("backup.json"):
            os.rename("backup.json", "file.json")

        del self.model_1
        del self.model_2

    def test_attributes_types(self):
        """
        Test that all attributes are of the correct type
        """
        self.assertIsInstance(self.model_1.text, str)
        self.assertIsInstance(self.model_1.place_id, str)
        self.assertIsInstance(self.model_1.user_id, str)

    def test_attributes_exist(self):
        """
        Test that class Review has all the required attributes
        and methods
        """
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))

    def test_isinstance(self):
        """
        Check that the created instance is an instance of the
        BaseModel class
        """
        self.assertIsInstance(self.model_1, BaseModel)

    def test_is_subclass(self):
        """
        it checks whether the Review instance is a subclass of basemodel
        """
        self.assertTrue(issubclass(self.model_1.__class__, BaseModel))

    def test_has_inherited_attributes(self):
        """
        affirms that all the attributes were imported from the BaseModel
        Also checks if the Review's attributes are present
        """
        self.assertTrue('id' in self.model_1.__dict__)
        self.assertTrue('created_at' in self.model_1.__dict__)
        self.assertTrue('updated_at' in self.model_1.__dict__)


if __name__ == "__main__":
    unittest.main()
