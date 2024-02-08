#!/usr/bin/python3
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
        self.assertIsNotNone(self.default_base_model.id)
        self.assertIsInstance(self.default_base_model.created_at, datetime)
        self.assertIsInstance(self.default_base_model.updated_at, datetime)

    def test_custom_values(self):
        expected_date = datetime(2022, 1, 2)
        self.assertEqual(self.custom_base_model.id, "custom_id")
        self.assertEqual(self.custom_base_model.created_at,
                         datetime(2022, 1, 1))
        self.assertEqual(self.custom_base_model.updated_at,
                         expected_date)

    def test_update_method(self):
        initial_updated_at = self.default_base_model.updated_at

        import time
        time.sleep(1)

        self.default_base_model.update()
        self.assertNotEqual(self.default_base_model.updated_at,
                            initial_updated_at)


if __name__ == '__main__':
    unittest.main()
