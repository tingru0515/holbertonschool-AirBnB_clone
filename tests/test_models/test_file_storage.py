#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Remove file.json if it exists before each test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        # Remove file.json after each test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_new(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), storage.all())

    def test_save(self):
        storage = FileStorage()
        obj = BaseModel()
        obj.name = "Test"
        storage.new(obj)
        storage.save()
        with open("file.json", "r") as f:
            data = f.read()
            self.assertIn("BaseModel.{}".format(obj.id), data)

    def test_reload(self):
        storage = FileStorage()
        obj = BaseModel()
        obj.name = "Test"
        storage.new(obj)
        storage.save()
        storage.reload()
        all_objs = storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), all_objs)

if __name__ == '__main__':
    unittest.main()
