#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

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

if __name__ == '__main__':
    unittest.main()
