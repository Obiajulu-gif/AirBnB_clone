#!/usr/bin/python3
import unittest
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        del self.storage

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_save(self, mock_open):
        obj1 = BaseModel()
        obj1.id = '1'
        obj1.name = 'Object 1'

        obj2 = BaseModel()
        obj2.id = '2'
        obj2.name = 'Object 2'

        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        mock_open.assert_called_with('file.json', 'w', encoding='UTF-8')

    @patch('builtins.open',
           new_callable=unittest.mock.mock_open,
           read_data='{"BaseModel.1": {"id": "1", "name": "Object 1"}}')
    def test_reload(self, mock_open):
        self.storage.reload()
        self.assertIn('BaseModel.1', self.storage.all())


if __name__ == '__main__':
    unittest.main()
