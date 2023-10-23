#!/usr/bin/python3
"""
Defines the FileStorage Test class.
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """
    Unit tests for attributes and methods
    Methods:
        setup() - Sets up the environment for testing
        teardown() - restores the environment and restores files to their
                    previous state
        test_has_attributes() - Checks if all methods and attribute
                                are present
        test_private_attributes - Tests violating access to private attribute
        test_all() - tests if the 'new' and 'all' method works as expected
        test_reload() - check if contents of file.json are properly
                        deserialised
    """

    def setUp(self):
        """
        Set up method
        It renames the file_storage file to avoid conflicting with data
        """
        if os.path.isfile("file.json"):
            os.rename("file.json", "backup_file.json")

        self.model1 = BaseModel()
        self.storage1 = FileStorage()()

    def tearDown(self):
        """
        Tear down method
        Does clean up and renames the json file back to the original name
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("backup_file.json"):
            os.rename("backup_file.json", "file.json")

        del self.model1
        del self.stotrage1

    def test_attributes(self):
        """
        Test that all attributes are present
        """
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))
        self.assertTrue(hasattr(self.storage1, 'all'))
        self.assertTrue(hasattr(self.storage1, 'save'))
        self.assertTrue(hasattr(self.storage1, 'new'))
        self.assertTrue(hasattr(self.storage1, 'reload'))
        self.assertTrue(type(self.storage1.all), dict)
        self.assertTrue(hasattr(self.storage1, '_FileStorage__file_path'))

    def test_private_attributes(self):
        """
        tests for illegal access of private attributes

        Raise an error when a private attr is accessed
        """
        with self.assertRaises(AttributeError):
            FileStorage.__objects
            FileStorage.__file_path

    def test_all(self):
        """
        tests both new and all
        """
        new_dict = self.storage1.all()
        self.assertIsNotNone(new_dict)
        new_id = 'BaseModel.' + self.model1.id
        self.assertIsInstance(new_dict, dict)
        self.assertIn(new_id, new_dict)

    def test_reload(self):
        """
        tests whether contents of file.json are deserialised properly
        """
        self.model1.save()
        self.assertTrue(os.path.isfile('file.json'))
        new_obj = BaseModel()
        new_id = 'BaseModel.' + new_obj.id
        new_obj.save()
        del self.storage1._FileStorage__objects[new_id]
        self.storage1.reload()
        self.assertIn(new_id, self.storage1.all())


if __name__ == "__main__":
    unittest.main()
