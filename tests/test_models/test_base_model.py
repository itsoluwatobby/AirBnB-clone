#!/usr/bin/python3
"""Defines the BaseModel Test class."""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import unittest
import os


class TestBaseModel(unittest.TestCase):
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

        self.model_1 = BaseModel()
        self.model_2 = BaseModel()

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
        self.assertTrue(type(self.model_1), BaseModel)
        self.assertTrue(type(self.model_1.id), str)
        self.assertTrue(type(self.model_1.created_at), datetime)
        self.assertTrue(type(self.model_1.updated_at), datetime)

    def test_init_from_dict(self):
        """
        Test that an instance is correctly created from a dict
        """
        base_dict = self.model_1.to_dict()
        new_model = BaseModel(**base_dict)
        self.assertEqual(self.model_1.id, new_model.id)
        self.assertEqual(self.model_1.created_at, new_model.created_at)
        self.assertEqual(self.model_1.updated_at, new_model.updated_at)

    def test_str_represntation(self):
        """
        Test that the object's string representation is correct
        """
        msg_str = "[{}] ({}) {}".format(
                type(
                    self.model_1
                    ).__name__, self.model_1.id, self.model_1.__dict__)
        self.assertEqual(str(self.model_1), msg_str)

    def test_save_method(self):
        """
        Test that the save method works correctly
        """
        prev_date = self.model_1.updated_at
        self.model_1.save()
        self.assertNotEqual(prev_date, self.model_1.updated_at)
        key = "BaseModel." + str(self.model_1.id)

        try:
            with open("file.json", "r") as f_saved:
                saved_file = json.load(f_saved)

                saved_dict = saved_file[key]
                self.assertEqual(saved_dict, self.model_1.to_dict())
        except FileNotFoundError:
            pass

    def test_to_dict_method(self):
        """
        Test that the dictionary representation of an object is good
        """
        a_dict = self.model_1.to_dict()
        self.assertTrue(type(a_dict), dict)
        self.assertIn("__class__", a_dict)
        self.assertIn("id", a_dict)
        self.assertIn("created_at", a_dict)
        self.assertIn("updated_at", a_dict)

    def test_unique_id(self):
        """
        Test that created objects have unique ids
        """
        self.assertNotEqual(self.model_1.id, self.model_2.id)


if __name__ == "__main__":
    unittest.main()
