#!/usr/bin/env python3
import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel
import time


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.default_base_model = BaseModel()

    def test_default_values(self):
        """test for default values"""
        self.assertIsNotNone(self.default_base_model.id)
        self.assertIsInstance(self.default_base_model.created_at, datetime)
        self.assertIsInstance(self.default_base_model.updated_at, datetime)

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
        self.assertTrue(len(self.default_base_model.save.__doc__) > 0)
        inital_updated_at = self.default_base_model.updated_at
        time.sleep(0.01)
        self.default_base_model.save()
        default_base_model_updated_at = self.default_base_model.updated_at
        self.assertNotEqual(inital_updated_at, default_base_model_updated_at)
        self.assertIsInstance(default_base_model_updated_at, datetime)

    def test_to_dict_method(self):
        """test for to_dict() """
        custom_dict = self.default_base_model.to_dict()
        default_BM_Created = self.default_base_model.created_at.isoformat()
        default_BM_Updated = self.default_base_model.updated_at.isoformat()
        self.assertTrue(len(custom_dict.__doc__) > 0)
        self.assertIsInstance(custom_dict, dict)
        self.assertIn('id', custom_dict)
        self.assertIn('created_at', custom_dict)
        self.assertIn('updated_at', custom_dict)
        self.assertIn('__class__', custom_dict)
        self.assertIn('name', custom_dict)
        self.assertIn('my_number', custom_dict)
        self.assertEqual(custom_dict['__class__'], 'BaseModel')
        self.assertEqual(custom_dict['created_at'], default_BM_Created)
        self.assertEqual(custom_dict['updated_at'], default_BM_Updated)


if __name__ == '__main__':
    unittest.main()
