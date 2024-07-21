import unittest
import os
import sys
import sqlite3
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.storage.sqlite_storage import SQLiteStorage

class TestSQLiteStorage(unittest.TestCase):
    def setUp(self):
        self.db_path = 'test_output.db'
        self.storage = SQLiteStorage(self.db_path)
        self.data = [
            {'entity_id': '1', 'CategoryName': 'Test', 'sku': '123', 'name': 'Test Product', 'description': '', 'shortdesc': 'Short description', 'price': '10.00', 'link': 'http://example.com', 'image': 'http://example.com/image.jpg', 'Brand': 'Brand', 'Rating': '5', 'CaffeineType': '', 'Count': '', 'Flavored': '', 'Seasonal': '', 'Instock': 'Yes', 'Facebook': '1', 'IsKCup': '0'}
        ]

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_write(self):
        self.storage.write(self.data)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
        conn.close()

if __name__ == '__main__':
    unittest.main()
