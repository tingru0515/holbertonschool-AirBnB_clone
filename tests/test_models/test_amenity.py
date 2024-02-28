#!/usr/bin/python3
"""
This modules provides TestAmenity class inherited from unittest.TestCase.
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    This class provides Amenity class related tests.
    """

    def test_successfully_create_obj(self):
        """
        Testing if obj will be successfully created.
        """
        obj = Amenity()
        expected = Amenity
        actual_value = obj.__class__
        self.assertEqual(actual_value, expected)

    def test_class_attribute(self):
        """
        Testing if the attrs will be expected.
        """
        obj = Amenity()
        expected = obj.name
        actual_value = ''
        self.assertEqual(actual_value, expected)

    def test_create_from_dict(self):
        """
        Testing if obj will be successfully created from dict.
        """
        obj_d = {
            'id': '1fcfb4ae-6d4a-4d51-96af-e7182db6ebdb',
            'created_at': "2024-02-28T15:16:01.780000",
            'updated_at': "2024-02-28T15:16:01.780000"}

        obj = Amenity(**obj_d)
        expected = '1fcfb4ae-6d4a-4d51-96af-e7182db6ebdb'
        actual_value = obj.id
        self.assertEqual(actual_value, expected)


if __name__ == '__main__':
    unittest.main()
