#!/usr/bin/python3
"""Defines tests for BaseModel serialization and deserialization."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestSaveReloadBaseModel(unittest.TestCase):
    """Tests for saving and reloading BaseModel instances."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.test_file = 'file.json'
        try:
            os.remove(cls.test_file)
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Tear down test environment."""
        try:
            os.remove(cls.test_file)
        except FileNotFoundError:
            pass

    def test_save_reload_base_model(self):
        """Test saving and reloading BaseModel instances."""
        # Create a new BaseModel instance
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        # Check if the object is saved in storage
        all_objs = FileStorage().all()
        found_id = any(val.id == my_model.id for val in all_objs.values())
        self.assertTrue(found_id)

        # Create another BaseModel instance
        my_model2 = BaseModel()
        my_model2.name = "My_Second_Model"
        my_model2.my_number = 42
        my_model2.save()

        # Check if the object is saved in storage
        all_objs = FileStorage().all()
        found_id = any(val.id == my_model2.id for val in all_objs.values())
        self.assertTrue(found_id)

        # Reload storage to clear in-memory objects
        FileStorage().reload()

        # Check if objects are reloaded from file
        all_objs = FileStorage().all()
        found_id = any(val.id == my_model.id for val in all_objs.values())
        found_id2 = any(val.id == my_model2.id for val in all_objs.values())
        self.assertTrue(found_id)
        self.assertTrue(found_id2)


if __name__ == '__main__':
    unittest.main()
