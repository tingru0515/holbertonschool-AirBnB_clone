#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_successfully_create_obj(self):
        obj = Place()
        expected = Place
        actual_value = obj.__class__
        self.assertEqual(actual_value, expected)

    def test_class_attribute(self):
        obj = Place()
        expected = obj.name
        actual_value = ''
        self.assertEqual(actual_value, expected)
        expected = obj.city_id
        actual_value = ''
        self.assertEqual(actual_value, expected)
        expected = obj.user_id
        actual_value = ''
        self.assertEqual(actual_value, expected)
        expected = obj.description
        actual_value = ''
        self.assertEqual(actual_value, expected)
        expected = obj.number_rooms
        actual_value = 0
        self.assertEqual(actual_value, expected)
        expected = obj.number_bathrooms
        actual_value = 0
        self.assertEqual(actual_value, expected)
        expected = obj.max_guest
        actual_value = 0
        self.assertEqual(actual_value, expected)
        expected = obj.price_by_night
        actual_value = 0
        self.assertEqual(actual_value, expected)
        expected = obj.latitude
        actual_value = 0.0
        self.assertEqual(actual_value, expected)
        expected = obj.longitude
        actual_value = 0.0
        self.assertEqual(actual_value, expected)
        expected = obj.amenity_ids
        actual_value = []
        self.assertEqual(actual_value, expected)

    def test_create_from_dict(self):
        obj_d = {
            'id': '1fcfb4ae-6d4a-4d51-96af-e7182db6ebdb',
            'created_at': "2024-02-28T15:16:01.780000",
            'updated_at': "2024-02-28T15:16:01.780000"}

        obj = Place(**obj_d)
        expected = '1fcfb4ae-6d4a-4d51-96af-e7182db6ebdb'
        actual_value = obj.id
        self.assertEqual(actual_value, expected)


if __name__ == '__main__':
    unittest.main()
