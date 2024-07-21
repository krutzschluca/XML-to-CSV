import unittest
import os
import sys

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.storage.csv_storage import CSVStorage

class TestCSVStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_output.csv'
        self.storage = CSVStorage(self.file_path)
        self.data = [
            {'entity_id': '1', 'CategoryName': 'Test', 'sku': '123', 'name': 'Test Product', 'description': '', 'shortdesc': 'Short description', 'price': '10.00', 'link': 'http://example.com', 'image': 'http://example.com/image.jpg', 'Brand': 'Brand', 'Rating': '5', 'CaffeineType': '', 'Count': '', 'Flavored': '', 'Seasonal': '', 'Instock': 'Yes', 'Facebook': '1', 'IsKCup': '0'}
        ]

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_write(self):
        self.storage.write(self.data)
        self.assertTrue(os.path.exists(self.file_path))

if __name__ == '__main__':
    unittest.main()
