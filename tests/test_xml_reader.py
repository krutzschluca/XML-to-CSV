import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from xml_reader import read_xml
from io import StringIO

class TestXMLReader(unittest.TestCase):
    def test_read_local_xml(self):
        xml_content = '''<?xml version="1.0"?>
        <catalog>
            <item>
                <entity_id>1</entity_id>
                <CategoryName>Test</CategoryName>
                <sku>123</sku>
                <name>Test Product</name>
                <description></description>
                <shortdesc>Short description</shortdesc>
                <price>10.00</price>
                <link>http://example.com</link>
                <image>http://example.com/image.jpg</image>
                <Brand>Brand</Brand>
                <Rating>5</Rating>
                <CaffeineType></CaffeineType>
                <Count></Count>
                <Flavored></Flavored>
                <Seasonal></Seasonal>
                <Instock>Yes</Instock>
                <Facebook>1</Facebook>
                <IsKCup>0</IsKCup>
            </item>
        </catalog>'''
        with open('test.xml', 'w') as f:
            f.write(xml_content)

        data = read_xml('test.xml')
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['entity_id'], '1')
        os.remove('test.xml')

if __name__ == '__main__':
    unittest.main()
