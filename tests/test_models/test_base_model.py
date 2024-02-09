#!/usr/bin/env python3
import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.default_base_model = BaseModel()
        self.custom_base_model = BaseModel(id="custom_id",
                                           created_at=datetime(2022, 1, 1),
                                           updated_at=datetime(2022, 1, 2))

    def test_default_values(self):
        """test for default values"""
        self.assertIsNotNone(self.default_base_model.id)
        self.assertIsInstance(self.default_base_model.created_at, datetime)
        self.assertIsInstance(self.default_base_model.updated_at, datetime)

    def test_custom_values(self):
        """test for custom value"""
        expected_date = datetime(2022, 1, 2)
        self.assertEqual(self.custom_base_model.id, "custom_id")
        self.assertEqual(self.custom_base_model.created_at,
                         datetime(2022, 1, 1))
        self.assertEqual(self.custom_base_model.updated_at,
                         expected_date)

    def test_update_method(self):
        """test for update()"""
        initial_updated_at = self.default_base_model.updated_at

        import time
        time.sleep(1)

        self.default_base_model.update()
        self.assertNotEqual(self.default_base_model.updated_at,
                            initial_updated_at)

    def test_save_method(self):
        """test for save()"""
        self.assertTrue(len(self.custom_base_model.save.__doc__) > 0)
        initial_updated_at = self.default_base_model.updated_at
        custom_updated_at = self.custom_base_model.updated_at
        self.default_base_model.save()
        self.assertNotEqual(custom_updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """test for to_dict() """
        custom_dict = self.custom_base_model.to_dict()
        self.assertTrue(len(custom_dict.__doc__) > 0)
        self.assertIsInstance(custom_dict, dict)
        self.assertIn('_id', custom_dict)
        self.assertIn('_created_at', custom_dict)
        self.assertIn('_updated_at', custom_dict)
        self.assertIn('__class__', custom_dict)
        self.assertEqual(custom_dict['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
