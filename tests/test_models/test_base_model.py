#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime
from time import sleep

class TestBaseModel(unittest.TestCase):
    def test_id_generation(self):
        # Test if each instance has a unique id
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)
        print("ID generation test passed.")

    def test_created_at_type(self):
        # Test if created_at attribute is of type datetime
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        print("Created_at type test passed.")

    def test_updated_at_type(self):
        # Test if updated_at attribute is of type datetime
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)
        print("Created_at type test passed.")

    def test_save_updates_updated_at(self):
        # Test if save() method updates updated_at attribute
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        print("Save updates updated_at test passed.")

    def test_str_representation(self):
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 89
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_to_dict_contains_all_attributes(self):
        # Test if to_dict() method returns dictionary with all required attributes
        model = BaseModel()
        model.name = "Test"
        model.number = 123
        model_dict = model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('number', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        print("to_dict contains all attributes test passed.")

class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Tear down test environment."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save()

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

if __name__ == '__main__':
    unittest.main()
