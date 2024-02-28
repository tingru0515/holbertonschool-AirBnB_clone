#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_successfully_create_obj(self):
        obj = State()
        expected = State
        actual_value = obj.__class__
        self.assertEqual(actual_value, expected)

    def test_class_attribute(self):
        obj = State()
        expected = obj.name
        actual_value = ''
        self.assertEqual(actual_value, expected)

    def test_create_from_dict(self):
        obj_d = {
            'id': '1fcfb4ae-6d4a-4d51-96af-e7182db6ebdb',
            'created_at': "2024-02-28T15:16:01.780000",
            'updated_at': "2024-02-28T15:16:01.780000"}

        obj = State(**obj_d)
        expected = '1fcfb4ae-6d4a-4d51-96af-e7182db6ebdb'
        actual_value = obj.id
        self.assertEqual(actual_value, expected)


if __name__ == '__main__':
    unittest.main()
