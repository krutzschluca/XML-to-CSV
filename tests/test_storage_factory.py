import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from storage.storage_factory import StorageFactory
from storage.csv_storage import CSVStorage
from storage.sqlite_storage import SQLiteStorage

class TestStorageFactory(unittest.TestCase):
    def test_csv_storage(self):
        storage = StorageFactory.get_storage('csv', 'test.csv')
        self.assertIsInstance(storage, CSVStorage)

    def test_sqlite_storage(self):
        storage = StorageFactory.get_storage('sqlite', 'test.db')
        self.assertIsInstance(storage, SQLiteStorage)

    def test_invalid_storage(self):
        with self.assertRaises(ValueError):
            StorageFactory.get_storage('invalid', 'test')

if __name__ == '__main__':
    unittest.main()
