#!/usr/bin/python3
"""Defines the Place Test class."""
from models.base_model import BaseModel
from models.place import Place
import unittest
import os


class TestPlace(unittest.TestCase):
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

        self.model_1 = Place()
        self.model_2 = Place()

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
        self.assertIsInstance(self.model_1.name, str)
        self.assertIsInstance(self.model_1.city_id, str)
        self.assertIsInstance(self.model_1.user_id, str)
        self.assertIsInstance(self.model_1.description, str)
        self.assertIsInstance(self.model_1.number_rooms, int)
        self.assertIsInstance(self.model_1.number_bathrooms, int)
        self.assertIsInstance(self.model_1.max_guest, int)
        self.assertIsInstance(self.model_1.price_by_night, int)
        self.assertIsInstance(self.model_1.latitude, float)
        self.assertIsInstance(self.model_1.longitude, float)
        self.assertIsInstance(self.model_1.amenity_ids, list)

    def test_attributes_exist(self):
        """
        Test that class Place has all the required attributes
        and methods
        """
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_isinstance(self):
        """
        Check that the created instance is an instance of the
        BaseModel class
        """
        self.assertIsInstance(self.model_1, BaseModel)

    def test_is_subclass(self):
        """
        it checks whether the Place instance is a subclass of basemodel
        """
        self.assertTrue(issubclass(self.model_1.__class__, BaseModel))

    def test_has_inherited_attributes(self):
        """
        affirms that all the attributes were imported from the BaseModel
        Also checks if the Place's attributes are present
        """
        self.assertTrue('id' in self.model_1.__dict__)
        self.assertTrue('created_at' in self.model_1.__dict__)
        self.assertTrue('updated_at' in self.model_1.__dict__)


if __name__ == "__main__":
    unittest.main()
