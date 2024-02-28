#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage
"""


import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Tear down test environment."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_new(self):
        """Test adding a new object to storage."""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_save(self):
        """Test saving objects to file."""
        obj = BaseModel()
        obj.name = "Test"
        self.storage.new(obj)
        self.storage.save()
        with open("file.json", "r") as f:
            data = f.read()
            self.assertIn("BaseModel.{}".format(obj.id), data)

    def test_reload(self):
        """Test reloading objects from file."""
        obj = BaseModel()
        obj.name = "Test"
        self.storage.new(obj)
        self.storage.save()
        # Clear the current storage to simulate reloading
        self.storage._FileStorage__objects = {}
        # Reload the storage
        self.storage.reload()
        # Check if the reloaded object is in the storage
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), all_objs)

if __name__ == '__main__':
    unittest.main()
